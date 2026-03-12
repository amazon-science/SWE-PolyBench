# SWE-PolyBench Evaluation Runner
# 用于运行 PolyBench 评估的最小环境

FROM python:3.10-slim

# 安装 Docker CLI 和 Git
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app/SWE-PolyBench

# 先复制依赖文件，利用 Docker 缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 安装项目
RUN pip install -e .

# 默认命令
CMD ["python", "-m", "poly_bench_evaluation.run_evaluation"]
