# mini-swe-agent + SWE-PolyBench 完整评估流程

本文档描述如何使用 mini-swe-agent 进行推理，然后用 SWE-PolyBench 进行验证的完整流程。

## 架构概述

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           整体流程                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Step 1      │    │  Step 2      │    │  Step 3      │              │
│  │  环境准备    │───▶│  镜像准备    │───▶│  mini-swe    │              │
│  │  克隆代码    │    │  retag镜像   │    │  推理生成    │              │
│  └──────────────┘    └──────────────┘    └──────────────┘              │
│                                                   │                     │
│                                                   ▼                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Step 6      │    │  Step 5      │    │  Step 4      │              │
│  │  查看结果    │◀───│  PolyBench   │◀───│  格式转换    │              │
│  │  统计报告    │    │  验证评估    │    │  JSONL转换   │              │
│  └──────────────┘    └──────────────┘    └──────────────┘              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## 核心原理

### 1. 为什么需要两个工具？

| 工具 | 职责 | 输入 | 输出 |
|------|------|------|------|
| **mini-swe-agent** | AI Agent 推理，生成代码修复 patch | issue 描述 + 代码库 | `preds.json` (patch) |
| **SWE-PolyBench** | 验证 patch 是否正确解决问题 | patch + 测试用例 | 测试通过率报告 |

### 2. Docker 镜像的作用

Docker 镜像包含：
- 特定版本的项目代码（base_commit）
- 运行环境（JDK/Node.js/Python 等）
- 测试命令配置

**镜像命名差异（关键理解）**：

| 来源 | 镜像格式 | 示例 |
|------|----------|------|
| PolyBench 官方 (GHCR) | `ghcr.io/timesler/swe-polybench.eval.x86_64.{instance_id}` | `ghcr.io/timesler/swe-polybench.eval.x86_64.google__gson-2337:latest` |
| mini-swe-agent 期望 | `docker.io/swebench/sweb.eval.x86_64.{id}` | `docker.io/swebench/sweb.eval.x86_64.google_1776_gson-2337:latest` |
| PolyBench 本地 | `polybench_{language}_{instance_id}` | `polybench_java_google__gson-2337:latest` |

**注意**: mini-swe-agent 把 `__` 替换成 `_1776_`（Docker 不允许双下划线作为镜像名的一部分）

### 3. 数据格式转换

| 格式 | 用途 | 示例 |
|------|------|------|
| `preds.json` | mini-swe-agent 输出 | `{"instance_id": {..., "model_patch": "..."}}` |
| `predictions.jsonl` | PolyBench 输入 | `{"instance_id": "...", "model_patch": "..."}` (每行一个JSON) |

---

## 完整流程

### Step 1: 环境准备

```bash
# 创建工作目录
mkdir -p ~/swe-eval && cd ~/swe-eval

# 克隆两个仓库
git clone https://github.com/zhaoyb1990/mini-swe-agent.git
git clone https://github.com/zhaoyb1990/SWE-PolyBench.git

# 进入 mini-swe-agent 目录，创建虚拟环境
cd mini-swe-agent
python -m venv .venv
source .venv/bin/activate

# 安装 mini-swe-agent
pip install -e .

# 配置 API Key (使用阿里云 Dashscope / 通义千问)
mini-extra config set DASHSCOPE_API_KEY "your-api-key-here"
mini-extra config set DASHSCOPE_BASE_URL "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 安装 SWE-PolyBench 依赖
cd ../SWE-PolyBench
pip install -e .
```

### Step 2: 准备 Docker 镜像

**原理**: PolyBench 官方已在 GHCR 发布预构建镜像，但 mini-swe-agent 期望不同的命名格式。我们需要 retag。

```bash
cd ~/swe-eval/SWE-PolyBench

# 方法1: 使用预构建脚本（推荐）
# 脚本会自动：1. 检查本地镜像 2. 尝试从 GHCR 拉取 3. Retag 为 mini-swe-agent 格式
python scripts/prebuild_images.py --limit 5

# 方法2: 手动批量 retag（如果已有 GHCR 镜像）
for img in $(docker images --format "{{.Repository}}:{{.Tag}}" | grep "ghcr.io/timesler/swe-polybench.eval.x86_64"); do
    instance_id=$(echo "$img" | sed 's|ghcr.io/timesler/swe-polybench.eval.x86_64.\(.*\):latest|\1|')
    docker_compatible="${instance_id//__/_1776_}"
    docker tag "$img" "docker.io/swebench/sweb.eval.x86_64.${docker_compatible}:latest"
    echo "Tagged: $instance_id -> $docker_compatible"
done

# 验证镜像
docker images | grep swebench
```

### Step 3: mini-swe-agent 推理

**原理**: AI Agent 读取 issue 描述，在 Docker 容器中探索代码库，生成修复 patch。

```bash
cd ~/swe-eval/mini-swe-agent
source .venv/bin/activate

# 运行推理（slice 指定要处理的实例范围）
mini-extra swebench \
  --model dashscope/qwen3-max \
  --subset AmazonScience/SWE-PolyBench_Verified \
  --split test \
  --slice 0:5 \
  --workers 1

# 输出文件:
# - preds.json: 包含所有生成的 patch
# - google__gson-2337/google__gson-2337.traj.json: 详细推理轨迹
```

**常用参数说明**:
- `--model`: 模型名称（dashscope/qwen3-max, anthropic/claude-3-opus 等）
- `--subset`: 数据集名称或 HuggingFace 路径
- `--slice`: 实例范围，如 `0:5` 表示前5个，`10:20` 表示第11-20个
- `--workers`: 并行数（建议1，避免API限流）
- `--redo-existing`: 重新处理已完成的实例

### Step 4: 格式转换

**原理**: mini-swe-agent 输出嵌套 JSON 格式，PolyBench 期望 JSONL 格式。

```bash
cd ~/swe-eval/SWE-PolyBench

# 转换格式
python scripts/convert_preds.py ~/swe-eval/mini-swe-agent/preds.json -o predictions.jsonl

# 查看转换结果
cat predictions.jsonl
```

**格式对比**:
```json
// preds.json (mini-swe-agent 输出)
{
  "google__gson-2337": {
    "model_name_or_path": "dashscope/qwen3-max",
    "instance_id": "google__gson-2337",
    "model_patch": "diff --git a/..."
  }
}
```

```json
// predictions.jsonl (PolyBench 输入)
{"instance_id": "google__gson-2337", "model_patch": "diff --git a/..."}
```

### Step 5: PolyBench 验证评估

**原理**: 在 Docker 容器中应用 patch，运行测试用例，统计通过率。

```bash
cd ~/swe-eval/SWE-PolyBench

# 运行评估
python -m poly_bench_evaluation.run_evaluation \
  --dataset-path AmazonScience/SWE-PolyBench_Verified \
  --predictions-path predictions.jsonl \
  --result-path ./results \
  --num-threads 1

# 输出文件:
# - results/google__gson-2337_result.json: 单实例结果
# - results/aggregate_results.json: 汇总结果
```

**常用参数说明**:
- `--dataset-path`: 数据集路径（HuggingFace 或本地 CSV）
- `--predictions-path`: predictions.jsonl 文件路径
- `--result-path`: 结果输出目录
- `--num-threads`: 并行线程数
- `--skip-existing`: 跳过已评估的实例
- `--evaluate-gold`: 评估 gold patch（用于验证环境）

### Step 6: 查看结果

```bash
# 查看汇总结果
cat results/aggregate_results.json | python -m json.tool

# 查看单个实例详细结果
cat results/google__gson-2337_result.json | python -m json.tool

# 结果字段说明:
# - resolved: 是否完全解决（f2p全部通过，p2p全部未通过）
# - passed_tests: 通过的测试
# - failed_tests: 失败的测试
# - patch_applied: patch 是否成功应用
```

---

## 一键脚本

### 完整评估脚本

```bash
#!/bin/bash
# run_full_evaluation.sh
# 用法: ./run_full_evaluation.sh <start_idx> <end_idx>

set -e

START=${1:-0}
END=${2:-5}
WORK_DIR=~/swe-eval

echo "=========================================="
echo "SWE-PolyBench 完整评估流程"
echo "实例范围: $START 到 $END"
echo "=========================================="

# Step 1: 确保环境
cd $WORK_DIR/mini-swe-agent
source .venv/bin/activate

# Step 2: 准备镜像
echo "[Step 2] 准备 Docker 镜像..."
cd $WORK_DIR/SWE-PolyBench
python scripts/prebuild_images.py --limit $((END - START)) --offset $START

# Step 3: mini-swe-agent 推理
echo "[Step 3] mini-swe-agent 推理..."
cd $WORK_DIR/mini-swe-agent
mini-extra swebench \
  --model dashscope/qwen3-max \
  --subset AmazonScience/SWE-PolyBench_Verified \
  --split test \
  --slice ${START}:${END} \
  --workers 1

# Step 4: 格式转换
echo "[Step 4] 格式转换..."
cd $WORK_DIR/SWE-PolyBench
python scripts/convert_preds.py $WORK_DIR/mini-swe-agent/preds.json -o predictions.jsonl

# Step 5: PolyBench 验证
echo "[Step 5] PolyBench 验证..."
python -m poly_bench_evaluation.run_evaluation \
  --dataset-path AmazonScience/SWE-PolyBench_Verified \
  --predictions-path predictions.jsonl \
  --result-path ./results \
  --num-threads 1

# Step 6: 显示结果
echo "[Step 6] 结果汇总..."
cat results/aggregate_results.json | python -m json.tool

echo "=========================================="
echo "评估完成!"
echo "=========================================="
```

### 仅推理脚本

```bash
#!/bin/bash
# run_inference_only.sh
# 用法: ./run_inference_only.sh <start_idx> <end_idx>

START=${1:-0}
END=${2:-5}

cd ~/swe-eval/mini-swe-agent
source .venv/bin/activate

# 准备镜像
python ~/swe-eval/SWE-PolyBench/scripts/prebuild_images.py --limit $((END - START)) --offset $START

# 推理
mini-extra swebench \
  --model dashscope/qwen3-max \
  --subset AmazonScience/SWE-PolyBench_Verified \
  --split test \
  --slice ${START}:${END} \
  --workers 1
```

### 仅验证脚本

```bash
#!/bin/bash
# run_evaluation_only.sh
# 用法: ./run_evaluation_only.sh <preds.json路径>

PREDS_PATH=${1:-~/swe-eval/mini-swe-agent/preds.json}

cd ~/swe-eval/SWE-PolyBench

# 转换格式
python scripts/convert_preds.py $PREDS_PATH -o predictions.jsonl

# 验证
python -m poly_bench_evaluation.run_evaluation \
  --dataset-path AmazonScience/SWE-PolyBench_Verified \
  --predictions-path predictions.jsonl \
  --result-path ./results \
  --num-threads 1
```

---

## 配置说明

### mini-swe-agent 配置

```bash
# 查看当前配置
mini-extra config list

# 设置 API Key
mini-extra config set DASHSCOPE_API_KEY "sk-xxxxx"

# 设置 Base URL（可选，用于自定义端点）
mini-extra config set DASHSCOPE_BASE_URL "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 配置文件位置
cat ~/.config/mini-swe-agent/.env
```

### 支持的模型

| 模型 | 配置方式 |
|------|----------|
| 通义千问 (阿里云) | `--model dashscope/qwen3-max` |
| Claude (Anthropic) | `--model anthropic/claude-3-opus-20240229` |
| OpenAI | `--model openai/gpt-4` |
| 本地模型 | `--model openai/<model_name>` + 设置 `OPENAI_BASE_URL` |

---

## 常见问题

### Q1: 镜像拉取失败 404
**原因**: mini-swe-agent 尝试从 docker.io 拉取，但 PolyBench 镜像在 ghcr.io
**解决**: 运行 `python scripts/prebuild_images.py` 进行 retag

### Q2: Docker 容器启动失败 (exit code 125)
**原因**: 镜像名格式不匹配
**解决**: 确保镜像 tag 是 `docker.io/swebench/sweb.eval.x86_64.{id}:latest` 格式

### Q3: patch 应用失败
**原因**: patch 格式不正确或与代码版本不匹配
**解决**: 检查 `results/{instance_id}_result.json` 中的错误信息

### Q4: API 限流
**原因**: 请求频率过高
**解决**: 使用 `--workers 1` 降低并发

---

## 目录结构

```
~/swe-eval/
├── mini-swe-agent/
│   ├── .venv/
│   ├── preds.json              # mini-swe-agent 输出
│   ├── google__gson-2337/      # 实例推理轨迹
│   │   └── google__gson-2337.traj.json
│   └── minisweagent.log
│
└── SWE-PolyBench/
    ├── scripts/
    │   ├── prebuild_images.py  # 镜像准备脚本
    │   └── convert_preds.py    # 格式转换脚本
    ├── predictions.jsonl       # PolyBench 输入
    ├── results/                # PolyBench 输出
    │   ├── google__gson-2337_result.json
    │   └── aggregate_results.json
    └── run_logs_java/          # 测试运行日志
        └── google__gson-2337_run.log
```
