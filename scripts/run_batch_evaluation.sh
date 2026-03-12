#!/bin/bash
# 分批运行完整 SWE-PolyBench 评估流程
# 用法: ./run_batch_evaluation.sh [batch_size] [start_idx] [workers]
#
# 参数:
#   batch_size - 每批处理实例数 (默认: 20)
#   start_idx  - 从第几个实例开始，用于断点续传 (默认: 0)
#   workers    - 并发工作进程数 (默认: 4)
#
# 环境变量:
#   MODEL      - 模型名称 (默认: dashscope/qwen3-max)
#   DATASET    - 数据集路径 (默认: AmazonScience/SWE-PolyBench_Verified)
#   WORK_DIR   - 工作目录 (默认: ~/swe-eval)
#
# 环境说明:
#   - mini-swe-agent 需要在其 venv 中运行 (推理阶段)
#   - SWE-PolyBench 使用系统 Python 环境 (镜像构建、格式转换、验证阶段)
#
# 示例:
#   ./run_batch_evaluation.sh 20 0 4        # 从头开始，每批20个，4个worker并发
#   ./run_batch_evaluation.sh 20 60 4       # 从第60个实例继续
#   nohup ./run_batch_evaluation.sh 20 0 4 > evaluation.log 2>&1 &  # 后台运行

set -e

# ==================== 配置参数 ====================
BATCH_SIZE=${1:-20}
START_IDX=${2:-0}
WORKERS=${3:-4}
TOTAL_INSTANCES=${TOTAL_INSTANCES:-382}

MODEL="${MODEL:-dashscope/qwen3-max}"
DATASET="${DATASET:-AmazonScience/SWE-PolyBench_Verified}"
WORK_DIR="${WORK_DIR:-$HOME}"

# 获取脚本所在目录的父目录 (SWE-PolyBench 根目录)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POLYBENCH_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# mini-swe-agent venv 路径
MINISWE_VENV="$WORK_DIR/mini-swe-agent/.venv"

# ==================== 打印配置 ====================
echo "=========================================="
echo "SWE-PolyBench 分批评估流程"
echo "=========================================="
echo "批次大小:   $BATCH_SIZE"
echo "起始索引:   $START_IDX"
echo "并发数:     $WORKERS"
echo "总实例数:   $TOTAL_INSTANCES"
echo "工作目录:   $WORK_DIR"
echo "模型:       $MODEL"
echo "数据集:     $DATASET"
echo "PolyBench:  $POLYBENCH_DIR"
echo "mini-swe venv: $MINISWE_VENV"
echo "=========================================="
echo "开始时间:   $(date)"
echo "=========================================="

# ==================== 环境检查 ====================
if [ ! -d "$WORK_DIR/mini-swe-agent" ]; then
    echo "错误: mini-swe-agent 目录不存在: $WORK_DIR/mini-swe-agent"
    echo "请先运行: git clone https://github.com/zhaoyb1990/mini-swe-agent.git $WORK_DIR/mini-swe-agent"
    exit 1
fi

if [ ! -d "$POLYBENCH_DIR" ]; then
    echo "错误: SWE-PolyBench 目录不存在: $POLYBENCH_DIR"
    exit 1
fi

if [ ! -f "$MINISWE_VENV/bin/activate" ]; then
    echo "警告: mini-swe-agent 虚拟环境不存在: $MINISWE_VENV"
    echo "请先在 mini-swe-agent 目录创建 venv 并安装依赖"
    exit 1
fi

# ==================== 辅助函数 ====================

# 使用系统 Python 执行命令
run_system_python() {
    # 使用系统 Python (不激活 venv)
    /usr/bin/python3 "$@"
}

# 使用 mini-swe-agent venv 执行命令
run_miniswe_python() {
    source "$MINISWE_VENV/bin/activate"
    "$@"
    deactivate
}

# ==================== 初始化 ====================
cd "$POLYBENCH_DIR"

# 创建结果目录
mkdir -p results
mkdir -p build_logs

# 初始化总预测文件 (如果不存在)
PREDICTIONS_ALL="predictions_all.jsonl"
if [ ! -f "$PREDICTIONS_ALL" ]; then
    touch "$PREDICTIONS_ALL"
    echo "创建总预测文件: $PREDICTIONS_ALL"
fi

# 进度日志
PROGRESS_LOG="progress.log"
if [ ! -f "$PROGRESS_LOG" ]; then
    touch "$PROGRESS_LOG"
    echo "创建进度日志: $PROGRESS_LOG"
fi

# ==================== 主循环 ====================
TOTAL_BATCHES=$(( (TOTAL_INSTANCES + BATCH_SIZE - 1) / BATCH_SIZE ))

for ((start=START_IDX; start<TOTAL_INSTANCES; start+=BATCH_SIZE)); do
    end=$((start + BATCH_SIZE))
    [ $end -gt $TOTAL_INSTANCES ] && end=$TOTAL_INSTANCES

    batch=$((start / BATCH_SIZE + 1))

    echo ""
    echo "=========================================="
    echo "批次 $batch/$TOTAL_BATCHES: 实例 $start - $((end-1))"
    echo "=========================================="
    echo "开始时间: $(date)"

    # 记录批次开始
    echo "$(date '+%Y-%m-%d %H:%M:%S') [BATCH START] Batch $batch: instances $start-$((end-1))" >> "$POLYBENCH_DIR/$PROGRESS_LOG"

    # -------------------- Step 1: 预构建镜像 (系统 Python) --------------------
    echo ""
    echo "[Step 1/6] 预构建 Docker 镜像 (系统 Python)..."
    cd "$POLYBENCH_DIR"

    LIMIT=$((end - start))
    python3 scripts/prebuild_images.py --limit $LIMIT --offset $start

    # -------------------- Step 2: mini-swe-agent 推理 (venv) --------------------
    echo ""
    echo "[Step 2/6] mini-swe-agent 推理 (venv 环境)..."

    # 备份之前的预测文件 (如果存在)
    if [ -f "$WORK_DIR/mini-swe-agent/preds.json" ]; then
        mv "$WORK_DIR/mini-swe-agent/preds.json" "$WORK_DIR/mini-swe-agent/preds_backup_$(date +%Y%m%d_%H%M%S).json"
    fi

    # 激活 mini-swe-agent venv 并运行推理
    source "$MINISWE_VENV/bin/activate"
    cd "$WORK_DIR/mini-swe-agent"

    mini-extra swebench \
        --model "$MODEL" \
        --subset "$DATASET" \
        --split test \
        --slice ${start}:${end} \
        --workers $WORKERS

    deactivate
    cd "$POLYBENCH_DIR"

    # -------------------- Step 3: 格式转换 (系统 Python) --------------------
    echo ""
    echo "[Step 3/6] 格式转换 (系统 Python)..."

    BATCH_PRED="predictions_batch_${batch}.jsonl"
    python3 scripts/convert_preds.py "$WORK_DIR/mini-swe-agent/preds.json" -o "$BATCH_PRED"

    pred_count=$(wc -l < "$BATCH_PRED")
    echo "本批次预测数量: $pred_count"

    # -------------------- Step 4: 追加到总预测文件 --------------------
    echo ""
    echo "[Step 4/6] 追加到总预测文件..."
    cat "$BATCH_PRED" >> "$PREDICTIONS_ALL"
    total_preds=$(wc -l < "$PREDICTIONS_ALL")
    echo "总预测数量: $total_preds"

    # -------------------- Step 5: PolyBench 验证 (系统 Python) --------------------
    echo ""
    echo "[Step 5/6] PolyBench 验证 (系统 Python)..."

    python3 -m poly_bench_evaluation.run_evaluation \
        --dataset-path "$DATASET" \
        --predictions-path "$BATCH_PRED" \
        --result-path ./results \
        --num-threads $WORKERS \
        --delete-image \
        --skip-existing

    # -------------------- Step 6: 清理 --------------------
    echo ""
    echo "[Step 6/6] 清理 Docker 缓存..."

    # 清理悬空镜像
    docker image prune -f 2>/dev/null || true

    # 清理 Docker 系统缓存 (可选，释放更多空间)
    docker system prune -f --volumes 2>/dev/null || true

    # 显示当前磁盘使用情况
    echo "Docker 磁盘使用:"
    docker system df 2>/dev/null || true

    # -------------------- 记录进度 --------------------
    echo "$(date '+%Y-%m-%d %H:%M:%S') [BATCH END] Batch $batch completed" >> "$POLYBENCH_DIR/$PROGRESS_LOG"

    # -------------------- 清理临时文件 (可选) --------------------
    # 保留预测文件用于调试，可取消注释以下行
    # rm -f "$BATCH_PRED"

    echo ""
    echo "批次 $batch 完成!"
    echo "结束时间: $(date)"

done

# ==================== 最终汇总 ====================
echo ""
echo "=========================================="
echo "所有批次完成!"
echo "=========================================="

cd "$POLYBENCH_DIR"

# 汇总结果 (系统 Python)
echo ""
echo "[汇总] 生成最终结果..."

python3 -c "
from poly_bench_evaluation.scoring import aggregate_logs
aggregate_logs(result_path='./results', dataset_path='$DATASET', output_path='./results')
"

# 显示最终结果
echo ""
echo "=========================================="
echo "评估结果汇总"
echo "=========================================="
echo "总预测文件: $POLYBENCH_DIR/$PREDICTIONS_ALL"
echo "总预测数量: $(wc -l < "$PREDICTIONS_ALL")"
echo ""
echo "结果目录: $POLYBENCH_DIR/results/"
ls -la results/*.json 2>/dev/null || echo "无结果文件"

if [ -f "results/result.json" ]; then
    echo ""
    echo "汇总结果:"
    python3 -m json.tool results/result.json 2>/dev/null || cat results/result.json
fi

echo ""
echo "=========================================="
echo "完成时间: $(date)"
echo "=========================================="

# 显示进度日志
echo ""
echo "进度日志:"
cat "$PROGRESS_LOG"
