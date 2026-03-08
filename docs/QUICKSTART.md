# SWE-PolyBench 快速开始指南

本文档提供从零开始的完整操作步骤，帮助您快速运行 mini-swe-agent + SWE-PolyBench 评估流程。

## 前置要求

- Python 3.10+
- Docker
- Git
- API Key（阿里云 Dashscope / 通义千问）

---

## 快速开始

### Step 1: 初始化环境（首次运行）

```bash
# 创建工作目录
mkdir -p ~/swe-eval && cd ~/swe-eval

# 克隆仓库
git clone https://github.com/zhaoyb1990/mini-swe-agent.git
git clone https://github.com/zhaoyb1990/SWE-PolyBench.git

# 安装 mini-swe-agent
cd mini-swe-agent
python -m venv .venv
source .venv/bin/activate
pip install -e .

# 配置 API Key
mini-extra config set DASHSCOPE_API_KEY "your-api-key"
mini-extra config set DASHSCOPE_BASE_URL "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 安装 SWE-PolyBench
cd ../SWE-PolyBench
pip install -e .
```

### Step 2: 运行完整评估

```bash
# 设置工作目录
export WORK_DIR=~/swe-eval

# 运行完整流程（实例 0-5）
./scripts/run_full_evaluation.sh 0 5
```

### Step 3: 查看结果

```bash
# 查看汇总结果
cat ~/swe-eval/SWE-PolyBench/results/aggregate_results.json | python -m json.tool

# 查看推理轨迹
cat ~/swe-eval/mini-swe-agent/google__gson-2337/google__gson-2337.traj.json | python -m json.tool
```

---

## 分步运行

如果您需要更细粒度的控制，可以分步运行：

### 仅推理

```bash
# 设置工作目录
export WORK_DIR=~/swe-eval

# 仅运行推理
./scripts/run_inference_only.sh 0 5
```

### 仅验证

```bash
# 使用已有的 preds.json 进行验证
./scripts/run_evaluation_only.sh ~/swe-eval/mini-swe-agent/preds.json
```

---

## 流程图

```
┌─────────────────┐
│  Step 1: 环境准备  │  克隆代码 → 安装依赖 → 配置 API Key
└────────┬────────┘
         ↓
┌─────────────────┐
│  Step 2: 镜像准备  │  GHCR 镜像 → retag → docker.io/swebench/... 格式
└────────┬────────┘
         ↓
┌─────────────────┐
│  Step 3: 推理生成  │  mini-swe-agent → preds.json
└────────┬────────┘
         ↓
┌─────────────────┐
│  Step 4: 格式转换  │  preds.json → predictions.jsonl
└────────┬────────┘
         ↓
┌─────────────────┐
│  Step 5: 验证评估  │  PolyBench → 测试通过率
└────────┬────────┘
         ↓
┌─────────────────┐
│  Step 6: 查看结果  │  aggregate_results.json
└─────────────────┘
```

---

## 文件说明

### 输入文件

| 文件 | 说明 |
|------|------|
| `AmazonScience/SWE-PolyBench_Verified` | HuggingFace 数据集，包含 issue、代码库、测试用例 |

### 中间文件

| 文件 | 说明 |
|------|------|
| `mini-swe-agent/preds.json` | mini-swe-agent 输出的预测结果（嵌套 JSON） |
| `SWE-PolyBench/predictions.jsonl` | 转换后的预测文件（JSONL 格式） |

### 输出文件

| 文件 | 说明 |
|------|------|
| `results/aggregate_results.json` | 汇总评估结果 |
| `results/{instance_id}_result.json` | 单实例详细结果 |
| `run_logs_{language}/{instance_id}_run.log` | 测试运行日志 |

---

## 常用命令

```bash
# 查看当前 mini-swe-agent 配置
mini-extra config list

# 重新处理已完成的实例
mini-extra swebench --model dashscope/qwen3-max --subset ... --redo-existing

# 检查 Docker 镜像
docker images | grep swebench

# 手动转换格式
python scripts/convert_preds.py preds.json -o predictions.jsonl
```

---

## 支持的模型

| 模型 | 配置方式 |
|------|----------|
| 通义千问 (阿里云) | `--model dashscope/qwen3-max` |
| Claude (Anthropic) | `--model anthropic/claude-3-opus-20240229` |
| OpenAI GPT-4 | `--model openai/gpt-4` |

---

## 故障排查

### 镜像拉取失败 404

```bash
# 运行镜像准备脚本
python scripts/prebuild_images.py --limit 5
```

### Docker 容器启动失败

```bash
# 检查镜像是否存在
docker images | grep swebench

# 手动测试容器
docker run --rm docker.io/swebench/sweb.eval.x86_64.google_1776_gson-2337:latest echo "OK"
```

### API 限流

```bash
# 使用单线程
mini-extra swebench ... --workers 1
```

---

## 更多信息

详细文档请参考: [COMPLETE_WORKFLOW.md](./COMPLETE_WORKFLOW.md)
