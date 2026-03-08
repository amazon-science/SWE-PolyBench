#!/bin/bash
# 仅运行 PolyBench 验证
# 用法: ./run_evaluation_only.sh [preds.json路径]

set -e

PREDS_PATH=${1:-~/swe-eval/mini-swe-agent/preds.json}
WORK_DIR="${WORK_DIR:-~/swe-eval}"
DATASET="${DATASET:-AmazonScience/SWE-PolyBench_Verified}"

echo "=========================================="
echo "PolyBench 验证"
echo "=========================================="
echo "预测文件: $PREDS_PATH"
echo "数据集: $DATASET"
echo "=========================================="

cd "$WORK_DIR/SWE-PolyBench"

# 检查预测文件是否存在
if [ ! -f "$PREDS_PATH" ]; then
    echo "错误: 预测文件不存在: $PREDS_PATH"
    exit 1
fi

# 转换格式
echo "[转换] 格式转换..."
python scripts/convert_preds.py "$PREDS_PATH" -o predictions.jsonl

echo "预测数量: $(wc -l < predictions.jsonl)"

# 验证
echo "[验证] 开始验证..."
mkdir -p results

python -m poly_bench_evaluation.run_evaluation \
  --dataset-path "$DATASET" \
  --predictions-path predictions.jsonl \
  --result-path ./results \
  --num-threads 1 \
  --skip-existing

# 显示结果
echo ""
echo "=========================================="
echo "验证完成!"
echo "=========================================="

if [ -f "results/aggregate_results.json" ]; then
    cat results/aggregate_results.json | python -m json.tool
fi

echo ""
echo "详细结果: $WORK_DIR/SWE-PolyBench/results/"
