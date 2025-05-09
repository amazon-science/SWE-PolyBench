## SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents

<div align="center">
  
[![Website](https://img.shields.io/badge/Website-Visit-blue?style=for-the-badge)](https://amazon-science.github.io/SWE-PolyBench/)
[![Paper](https://img.shields.io/badge/Paper-arXiv-red?style=for-the-badge)](https://arxiv.org/abs/2504.08703)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow?style=for-the-badge)](https://huggingface.co/datasets/AmazonScience/SWE-PolyBench)

</div>

Hello! We are delighted to announce SWE-PolyBench! A multi language repo level software engineering benchmark. It contains 2110 curated issues in four languages (Java, JavaScript, TypeScript, and Python). In addition, it contains a stratified subset of 500 issues (SWE-PolyBench500) for the purpose of rapid experimentation. Please find more details below.

## Datasets
The datasets are available on Huggingface. We have the full dataset (PB) (`AmazonScience/SWE-PolyBench`) with 2110 instances and a sampled dataset (total 500 instances) called `PB500` (`AmazonScience/SWE-PolyBench_500`) where we have 125 instances from each language and a good distribution of task categories, i.e. Bug Fix, Feature, and Refactoring (40-40-20 split). We also ensured we have representation from all repos.

## Evaluation
The main file to run is `src/poly_bench_evaluation/run_evaluation.py`. These are the following parameters it takes:
- `--dataset-path` (required): The path to the datasets.
- `--predictions-path`: The model generated `.jsonl` predictions file. The file at the minimum needs to have `instance_id` and `model_patch` keys. The `model_patch` key should ONLY be a string (str).
- `--result-path` (required): This is the directory path to output the instance level results.
- `--num-threads`: Default is 1. For a machine with 16 cores CPU and 64GB Ram, 10-12 threads are recommended.
- `--evaluate-gold`: Whether to run the gold code patch evaluator. If this flag is used, the `predictions-path` parameter is not required and will be overwritten even if provided. To evaluate a model generated patch, please do not use the `evaluate-gold` flag.
- `--repo-path`: The directory to store base repos.
- `--delete-image`: Whether to delete the instance level image. Please note that, deleting the image is recommended if you do not have storage. Please use the `delete-image` flag to set it to True.
- `--skip-existing`: Whether to skip existing evaluations in `result-path`. If set to true, the instances that are available in result-path already will be skipped.
- `--metrics-only` : This flag, when set will only compute the file retrieval metrics and the pass rate will not be computed. Typically this flag may be used after the pass rates are computed.
- `--node-metrics`: If you also want to compute node retrieval metrics (this will increase time of running evaluation)

## Docker images
The dockerfiles have been tested on a `x86_64` Linux machine. Please create an issue if any of the dockerfile fails to build. After built, the docker images size varies, but it can take upto 5TB storage for all instances if `--delete-image` is omited. For `PB500` instances, the total docker image size is 1.2TB. No extra storage is necessary if delete-image is set to True as the docker images are deleted once the instance evaluation is done.

## Steps to run
Using a conda environment with python=3.11 is recommended.

1. Git clone this repo.
2. Cd into the cloned directory and from root folder install the requirements in a conda environment with python>3.10 with `pip install -r requirements.txt`
3. Run `pip install -e .` from root folder.
4. Run the evaluation using:
```sh
python3 src/poly_bench_evaluation/run_evaluation.py --dataset-path <dataset_path_or_hf_path> --result-path ./eval_logs
```

A sample run command to evaluate gold code patches (from root directory of package):
```sh
python3 src/poly_bench_evaluation/run_evaluation.py --dataset-path AmazonScience/SWE-PolyBench --result-path ./eval_logs/ --num-threads 9 --repo-path ~/repos --delete-image --evaluate-gold
```

A sample run command to evaluate model generated patches (from root directory of package):
```sh
python3 src/poly_bench_evaluation/run_evaluation.py --dataset-path AmazonScience/SWE-PolyBench --result-path ./eval_logs/ --num-threads 9 --repo-path ~/repos --delete-image --predictions-path ./model_generated_predictions.jsonl --skip-existing
```
## Results

The instance level results of each instance will be stored in `--result-path`. Instance level results include the list of passing tests and failing tests. The combined result will be outputted in the root directory `./result.json` file. In the terminal, the pass rate alongside the total number of "resolved" instances will also be printed.

The test run logs of each instance will also be stored in `./run_logs_{language}` directory. The raw output from the test run can be found here.

## Run time
If you are building all images and they are not available locally, then please expect a long running time. As we use instance specific docker image, they take some time to build. If you have storage, please do not set `delete-image`. This will reduce the runtime drastically the next time you run.

For running the sampled dataset, we expect the runtime to be ~7-8 hours (with 7-8 threads) if building images locally.

## Submission
To make a submission to SWE-PolyBench leaderboard, please follow this [README](https://github.com/amazon-science/SWE-PolyBench/blob/submission/README.md).

## ✍️ Citation
If you find our work helpful, please use the following citation.
```
@misc{rashid2025swepolybenchmultilanguagebenchmarkrepository,
      title={SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents}, 
      author={Muhammad Shihab Rashid and Christian Bock and Yuan Zhuang and Alexander Buchholz and Tim Esler and Simon Valentin and Luca Franceschi and Martin Wistuba and Prabhu Teja Sivaprasad and Woo Jung Kim and Anoop Deoras and Giovanni Zappella and Laurent Callot},
      year={2025},
      eprint={2504.08703},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2504.08703}, 
}
```

## Troubleshooting
If you get container conflict error (which may happen if you terminate your running code and run again), then please execute this command in terminal:
```sh
docker rm -f $(docker ps -a -q)
```
Caution: This will remove ALL running containers, so please proceed with caution.
