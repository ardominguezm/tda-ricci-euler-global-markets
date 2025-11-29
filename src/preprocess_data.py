"""
preprocess_data.py
-------------------
Align raw CSVs, fill missing values, and compute log-returns.

Outputs:
    data/processed/aligned_prices.csv
    data/processed/log_returns.csv
"""

import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw/")
PROC_DIR = Path("data/processed/")
PROC_DIR.mkdir(parents=True, exist_ok=True)


def load_raw_data():
    dfs = {}
    for file in RAW_DIR.glob("*.csv"):
        name = file.stem
        df = pd.read_csv(file, index_col=0, parse_dates=True)
        dfs[name] = df["Adj Close"]
    return pd.DataFrame(dfs)


def compute_log_returns(df):
    return (df / df.shift(1)).apply(lambda x: np.log(x))


def main():
    aligned = load_raw_data()
    aligned = aligned.sort_index().ffill().bfill()
    aligned.to_csv(PROC_DIR / "aligned_prices.csv")

    log_ret = compute_log_returns(aligned)
    log_ret.to_csv(PROC_DIR / "log_returns.csv")

    print("Preprocessing completed. Files saved in data/processed/")


if __name__ == "__main__":
    import numpy as np
    main()
