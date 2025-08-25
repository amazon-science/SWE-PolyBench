"""Load SWE-PolyBench dataset and output as JSON lines.

This script loads the dataset from either a CSV file or HuggingFace
and outputs each instance as a JSON line for processing by the bash script.
"""

import sys
import argparse
import pandas as pd
from datasets import load_dataset
import json


def parse_args():
    parser = argparse.ArgumentParser(description="Load SWE-PolyBench dataset and output as JSON lines")
    parser.add_argument("dataset_path", help="HuggingFace dataset name")
    parser.add_argument("--limit", "-l", type=int, help="Limit number of instances to output (for testing)")
    parser.add_argument("--offset", "-o", type=int, default=0, help="Skip first N instances (for resuming uploads)")
    return parser.parse_args()


def main():
    args = parse_args()
    
    dataset_path = args.dataset_path
    limit = args.limit
    offset = args.offset
    
    try:
        # Load dataset based on file extension
        if dataset_path.endswith('.csv'):
            print(f"Loading CSV dataset from {dataset_path}...", file=sys.stderr)
            df = pd.read_csv(dataset_path)
        else:
            print(f"Loading HuggingFace dataset from {dataset_path}...", file=sys.stderr)
            df = load_dataset(dataset_path, split="test").to_pandas()
        
        print(f"Loaded {len(df)} instances", file=sys.stderr)
        
        # Apply offset if specified
        if offset and offset > 0:
            df = df.iloc[offset:]
            print(f"Skipped first {offset} instances, {len(df)} remaining", file=sys.stderr)
        
        # Apply limit if specified
        if limit and limit > 0:
            df = df.head(limit)
            print(f"Limited to {len(df)} instances", file=sys.stderr)
        
        # Verify required columns exist
        required_columns = ['instance_id', 'language', 'repo', 'base_commit', 'Dockerfile']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}", file=sys.stderr)
            sys.exit(1)
        
        # Output each row as JSON
        for _, row in df.iterrows():
            print(json.dumps(row.to_dict()))
        
    except Exception as e:
        print(f"Error loading dataset: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()