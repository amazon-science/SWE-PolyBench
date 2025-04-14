# SWE-PolyBench Submission

This branch contains the logs, trajectories, and predictions of all leaderboard submissions. We follow similar procedure as [SWE-bench](https://www.swebench.com/submit.html) with a few exceptions. To submit please follow the following procedure:

1. Fork the SWE-PolyBench repository.

2. Clone the repository. Consider using `git clone --depth 1` if cloning takes too long.

3. Checkout the `submission` branch using:

```sh
git checkout submission
```

4. Under the split you evaluated on (either `evaluation/PB` or `evaluation/PB500`), create a folder with the submission date and the agent/model name, i.e. `20250402_sweagent_claude-sonnet37`. `PB` is for our full dataset and `PB500` is for our sampled dataset.

5. Within the folder, please include the following files:
    - `all_preds.jsonl` : Model predictions
    - `logs/` : SWE-PolyBench evaluation artifcats
        - Evaluation artifacts mean 500/2110 (PB/PB500) files. The file will be `instance_id_result.json` files (i.e. `microsoft__vscode-1234_result.json`). This is the instance level result file that is generated automatically once you run our evaluation code.
    - `metadata.yaml`: Metadata for how result is shown on website. Please include the following fields:
        - `name`: The name you want in the leaderboard entry
        - `oss`: `true` if your system is open-source
        - `site`: URL/link to more information about your system
        - `pass_rate` : The pass rate (resolved rate) you observed after your evaluation run (i.e. `XX.XX% (123/500)`).
    - `trajs/`: Reasoning trace reflecting how your system solved the problem
        - Submit one reasoning trace per task instance. The reasoning trace should show all of the steps your system took while solving the task. If your system outputs thoughts or comments during operation, they should be included as well.
        - The reasoning trace can be represented with any text based file format (e.g. md, json, yaml)
        - Ensure the task instance ID is in the name of the corresponding reasoning trace file.
    - `README.md`: Include anything you'd like to share about your model here!

6. Create a pull request to the `submission` branch of SWE-PolyBench with the new folder.
```sh
git add .
git commit -m "your message"
git push origin submission
```
Please NOTE that you need to select `submission` as the `Base` branch and the `Compare` will be your forks `submission` branch.

## 📞 Contact
Questions? Please create an issue.

## ✍️ Citation
If you found this repository helpful or are citing the numbers on the leaderboard for academic purposes, please cite:
```
@misc{rashid2025swepolybenchmultilanguagebenchmarkrepository,
      title={SWE-PolyBench: A multi-language benchmark for repository level evaluation of coding agents}, 
      author={Muhammad Shihab Rashid and Christian Bock and Yuan Zhuang and Alexander Buccholz and Tim Esler and Simon Valentin and Luca Franceschi and Martin Wistuba and Prabhu Teja Sivaprasad and Woo Jung Kim and Anoop Deoras and Giovanni Zappella and Laurent Callot},
      year={2025},
      eprint={2504.08703},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2504.08703}, 
}
```
