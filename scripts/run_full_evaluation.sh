#!/bin/bash
# 完整评估流程：镜像准备 -> 推理 -> 转换 -> 验证
# 用法: ./run_full_evaluation.sh [start_idx] [end_idx]

set -e

START=${1:-0}
END=${2:-5}
WORK_DIR="${WORK_DIR:-~/swe-eval}"
MODEL="${MODEL:-dashscope/qwen3-max}"
DATASET="${DATASET:-AmazonScience/SWE-PolyBench_Verified}"

echo "=========================================="
echo "SWE-PolyBench 完整评估流程"
echo "=========================================="
echo "实例范围: $START 到 $END"
echo "工作目录: $WORK_DIR"
echo "模型: $MODEL"
echo "数据集: $DATASET"
echo "=========================================="

# 检查工作目录
if [ ! -d "$WORK_DIR/mini-swe-agent" ]; then
    echo "错误: mini-swe-agent 目录不存在"
    echo "请先运行: git clone https://github.com/zhaoyb1990/mini-swe-agent.git $WORK_DIR/mini-swe-agent"
    exit 1
fi

if [ ! -d "$WORK_DIR/SWE-PolyBench" ]; then
    echo "错误: SWE-PolyBench 目录不存在"
    echo "请先运行: git clone https://github.com/zhaoyb1990/SWE-PolyBench.git $WORK_DIR/SWE-PolyBench"
    exit 1
fi

# Step 1: 激活环境
echo ""
echo "[Step 1/6] 激活虚拟环境..."
cd "$WORK_DIR/mini-swe-agent"
source .venv/bin/activate 2>/dev/null || {
    echo "虚拟环境不存在，正在创建..."
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .
}

# Step 2: 准备镜像
echo ""
echo "[Step 2/6] 准备 Docker 镜像..."
cd "$WORK_DIR/SWE-PolyBench"
LIMIT=$((END - START))
python scripts/prebuild_images.py --limit $LIMIT --offset $START

# Step 3: mini-swe-agent 推理
echo ""
echo "[Step 3/6] mini-swe-agent 推理..."
cd "$WORK_DIR/mini-swe-agent"

# 清理旧的 preds.json（如果需要重新推理）
# rm -f preds.json

mini-extra swebench \
  --model "$MODEL" \
  --subset "$DATASET" \
  --split test \
  --slice ${START}:${END} \
  --workers 1

# Step 4: 格式转换
echo ""
echo "[Step 4/6] 格式转换..."
cd "$WORK_DIR/SWE-PolyBench"
python scripts/convert_preds.py "$WORK_DIR/mini-swe-agent/preds.json" -o predictions.jsonl

echo "转换后的预测数量: $(wc -l < predictions.jsonl)"

# Step 5: PolyBench 验证
echo ""
echo "[Step 5/6] PolyBench 验证..."
mkdir -p results

python -m poly_bench_evaluation.run_evaluation \
  --dataset-path "$DATASET" \
  --predictions-path predictions.jsonl \
  --result-path ./results \
  --num-threads 1 \
  --skip-existing

# Step 6: 显示结果
echo ""
echo "[Step 6/6] 结果汇总..."
echo "----------------------------------------"

if [ -f "results/aggregate_results.json" ]; then
    cat results/aggregate_results.json | python -m json.tool
else
    echo "结果文件不存在，请检查评估日志"
fi

echo ""
echo "=========================================="
echo "评估完成!"
echo "=========================================="
echo "推理结果: $WORK_DIR/mini-swe-agent/preds.json"
echo "预测文件: $WORK_DIR/SWE-PolyBench/predictions.jsonl"
echo "评估结果: $WORK_DIR/SWE-PolyBench/results/"
echo "=========================================="
