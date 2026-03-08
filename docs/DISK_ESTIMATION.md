# SWE-PolyBench Docker 镜像磁盘占用估算

本文档估算 SWE-PolyBench Verified 数据集完整镜像所需的磁盘空间。

## 数据集概况

| 指标 | 数值 |
|------|------|
| **总实例数** | 382 |
| **仓库数** | 20 |
| **Java 实例** | 69 (18%) |
| **JavaScript 实例** | 100 (26%) |
| **TypeScript 实例** | 100 (26%) |
| **Python 实例** | 113 (30%) |

### 按仓库分布

| 仓库 | 实例数 | 语言 |
|------|--------|------|
| huggingface/transformers | 72 | Python |
| mui/material-ui | 70 | TypeScript |
| sveltejs/svelte | 46 | JavaScript |
| serverless/serverless | 33 | JavaScript |
| microsoft/vscode | 23 | TypeScript |
| keras-team/keras | 22 | Python |
| google/gson | 19 | Java |
| apache/rocketmq | 18 | Java |
| prettier/prettier | 17 | JavaScript |
| apache/dubbo | 15 | Java |
| langchain-ai/langchain | 13 | Python |
| trinodb/trino | 11 | Java |
| yt-dlp/yt-dlp | 5 | Python |
| apolloconfig/apollo | 4 | Java |
| mrdoob/three.js | 4 | JavaScript |
| tailwindlabs/tailwindcss | 3 | TypeScript |
| coder/code-server | 3 | TypeScript |
| google/guava | 2 | Java |
| angular/angular | 1 | TypeScript |
| Significant-Gravitas/AutoGPT | 1 | Python |

## 磁盘占用估算

### 两种估算方案

| 方案 | 大小 | 说明 |
|------|------|------|
| **优化估计** | **~140 GB** | Docker layer 共享（同仓库实例共享 base layer） |
| **保守估计** | **~1.8 TB** | 无共享（每个实例独立镜像） |

**实际占用会接近优化估计**，因为：
- 同语言的实例共享语言 base 镜像（Java/JS/TS）
- 同仓库的多个实例共享项目依赖层

### 按语言分解（优化估计）

| 语言 | Base 镜像 | 实例镜像增量 | 合计 |
|------|----------|-------------|------|
| Java | 2.5 GB | ~10 GB | **~13 GB** |
| JavaScript | 3.1 GB | ~23 GB | **~26 GB** |
| TypeScript | 3.4 GB | ~36 GB | **~40 GB** |
| Python | - | ~50 GB | **~50 GB** |
| **总计** | **9 GB** | **~119 GB** | **~140 GB** |

### Base 镜像说明

| 语言 | Base 镜像名称 | 大小 | 包含内容 |
|------|--------------|------|----------|
| Java | `polybench_java_base` | 2.5 GB | Amazon Linux + JDK 8/11/17 + Maven |
| JavaScript | `polybench_javascript_base` | 3.1 GB | Ubuntu + Node.js 4/6/8/12/16/18/20 + 浏览器 |
| TypeScript | `polybench_typescript_base` | 3.4 GB | Ubuntu + Node.js + 构建工具 + 浏览器 |
| Python | 无独立 base | - | 每个 Python 实例独立构建 |

## 主要存储大户

按仓库估算的存储占用：

| 仓库 | 实例数 | 预估大小 | 原因 |
|------|--------|----------|------|
| huggingface/transformers | 72 | ~60 GB | Python 无共享 + ML 依赖大 |
| mui/material-ui | 70 | ~20 GB | TypeScript + 前端依赖 |
| microsoft/vscode | 23 | ~15 GB | TypeScript + Electron 依赖 |
| mrdoob/three.js | 4 | ~25 GB | JavaScript + 3D 库 + WebGL 依赖 |

## 实际镜像大小参考

以下是从 GHCR 拉取的实际镜像大小：

| 镜像 | 大小 |
|------|------|
| `polybench_python_huggingface__transformers-3716` | 8.03 GB |
| `polybench_javascript_mrdoob__three.js-18648` | 6.13 GB |
| `polybench_typescript_base` | 3.38 GB |
| `polybench_javascript_base` | 3.06 GB |
| `polybench_java_base` | 2.54 GB |
| `polybench_java_google__gson-2337` | 2.69 GB |
| `polybench_python_significant-gravitas__autogpt-4652` | 1.07 GB |

## 建议

### 1. 磁盘规划

```bash
# 建议预留空间
最小配置: 200 GB  (运行部分实例)
推荐配置: 500 GB  (运行大部分实例)
完整配置: 1 TB    (运行所有实例)
```

### 2. 按需拉取

```bash
# 只拉取需要的实例镜像
python scripts/prebuild_images.py --limit 10  # 只准备前 10 个

# 按语言过滤
python scripts/prebuild_images.py --lang Python --limit 20
```

### 3. 清理策略

```bash
# 查看当前 Docker 占用
docker system df

# 清理未使用的镜像
docker image prune -a

# 清理所有未使用资源
docker system prune -a
```

### 4. 分批评估

```bash
# 分批运行，避免一次性拉取所有镜像
# 第一批
./scripts/run_full_evaluation.sh 0 50

# 第二批
./scripts/run_full_evaluation.sh 50 100

# 以此类推...
```

## 镜像来源

SWE-PolyBench 官方已预构建并发布镜像到 GitHub Container Registry：

```
ghcr.io/timesler/swe-polybench.eval.x86_64.{instance_id}:latest
```

示例：
```
ghcr.io/timesler/swe-polybench.eval.x86_64.google__gson-2337:latest
ghcr.io/timesler/swe-polybench.eval.x86_64.huggingface__transformers-3716:latest
```

## 查看命令

```bash
# 查看磁盘空间
df -h

# 查看 Docker 镜像占用
docker system df

# 列出所有 polybench 相关镜像
docker images | grep -E "polybench|swe-polybench"

# 查看特定镜像详情
docker image inspect ghcr.io/timesler/swe-polybench.eval.x86_64.google__gson-2337:latest
```
