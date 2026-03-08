#!/usr/bin/env python3
"""Convert mini-swe-agent preds.json to PolyBench predictions.jsonl format.

mini-swe-agent output (preds.json):
{
  "instance_id": {
    "model_name_or_path": "...",
    "instance_id": "...",
    "model_patch": "..."
  }
}

PolyBench expected (predictions.jsonl):
{"instance_id": "...", "model_patch": "..."}
{"instance_id": "...", "model_patch": "..."}
"""

import json
import argparse
from pathlib import Path


def convert_preds_to_jsonl(preds_path: str, output_path: str = None):
    """Convert mini-swe-agent preds.json to PolyBench predictions.jsonl format.

    Args:
        preds_path: Path to mini-swe-agent preds.json
        output_path: Path to output predictions.jsonl (default: same dir as preds.json)
    """
    preds_path = Path(preds_path)

    if output_path is None:
        output_path = preds_path.parent / "predictions.jsonl"
    else:
        output_path = Path(output_path)

    # Read preds.json
    with open(preds_path, "r") as f:
        preds = json.load(f)

    # Convert to JSONL format
    with open(output_path, "w") as f:
        for instance_id, item in preds.items():
            # Handle both formats: item is dict or item["model_patch"] is the patch
            if isinstance(item, dict):
                model_patch = item.get("model_patch", "")
            else:
                model_patch = item

            record = {
                "instance_id": instance_id,
                "model_patch": model_patch or ""
            }
            f.write(json.dumps(record) + "\n")

    print(f"Converted {len(preds)} predictions")
    print(f"Output: {output_path}")

    return output_path


def convert_jsonl_to_preds(jsonl_path: str, output_path: str = None, model_name: str = ""):
    """Convert PolyBench predictions.jsonl back to mini-swe-agent preds.json format.

    Args:
        jsonl_path: Path to predictions.jsonl
        output_path: Path to output preds.json (default: same dir as jsonl_path)
        model_name: Model name to include in output
    """
    jsonl_path = Path(jsonl_path)

    if output_path is None:
        output_path = jsonl_path.parent / "preds.json"
    else:
        output_path = Path(output_path)

    preds = {}
    with open(jsonl_path, "r") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                instance_id = item["instance_id"]
                preds[instance_id] = {
                    "model_name_or_path": model_name,
                    "instance_id": instance_id,
                    "model_patch": item.get("model_patch", "")
                }

    with open(output_path, "w") as f:
        json.dump(preds, f, indent=2)

    print(f"Converted {len(preds)} predictions")
    print(f"Output: {output_path}")

    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert between mini-swe-agent preds.json and PolyBench predictions.jsonl formats"
    )
    parser.add_argument(
        "input",
        help="Input file path (preds.json or predictions.jsonl)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: same directory as input)"
    )
    parser.add_argument(
        "--to-jsonl",
        action="store_true",
        help="Convert preds.json to predictions.jsonl (for PolyBench evaluation)"
    )
    parser.add_argument(
        "--to-preds",
        action="store_true",
        help="Convert predictions.jsonl to preds.json (for mini-swe-agent)"
    )
    parser.add_argument(
        "--model-name",
        default="",
        help="Model name to include when converting to preds.json"
    )

    args = parser.parse_args()

    input_path = Path(args.input)

    # Auto-detect conversion direction if not specified
    if not args.to_jsonl and not args.to_preds:
        if input_path.suffix == ".json" or "preds" in input_path.name:
            args.to_jsonl = True
        else:
            args.to_preds = True

    if args.to_jsonl:
        convert_preds_to_jsonl(args.input, args.output)
    elif args.to_preds:
        convert_jsonl_to_preds(args.input, args.output, args.model_name)


if __name__ == "__main__":
    main()
