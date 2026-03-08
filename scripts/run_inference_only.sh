#!/bin/bash
# 仅运行 mini-swe-agent 推理
# 用法: ./run_inference_only.sh [start_idx] [end_idx]

set -e

START=${1:-0}
END=${2:-5}
WORK_DIR="${WORK_DIR:-~/swe-eval}"
MODEL="${MODEL:-dashscope/qwen3-max}"
DATASET="${DATASET:-AmazonScience/SWE-PolyBench_Verified}"

echo "=========================================="
echo "mini-swe-agent 推理"
echo "=========================================="
echo "实例范围: $START 到 $END"
echo "模型: $MODEL"
echo "=========================================="

cd "$WORK_DIR/mini-swe-agent"
source .venv/bin/activate

# 准备镜像
echo "[准备] 检查 Docker 镜像..."
python "$WORK_DIR/SWE-PolyBench/scripts/prebuild_images.py --limit $((END - START)) --offset $START"

# 推理
echo "[推理] 开始推理..."
mini-extra swebench \
  --model "$MODEL" \
  --subset "$DATASET" \
  --split test \
  --slice ${START}:${END} \
  --workers 1

echo "=========================================="
echo "推理完成!"
echo "输出: $WORK_DIR/mini-swe-agent/preds.json"
echo "=========================================="
