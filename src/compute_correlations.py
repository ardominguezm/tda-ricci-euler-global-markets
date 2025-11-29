"""
compute_correlations.py
------------------------
Compute:
    - Annual correlation matrices
    - Full-period correlation matrix
    - Optionally sliding-window correlations
"""

import pandas as pd
from pathlib import Path

PROC_DIR = Path("data/processed/")
OUT = PROC_DIR
WINDOW = 90  # days for sliding window


def annual_correlations(df):
    matrices = {}
    for year in range(2017, 2023):
        mask = df.index.year == year
        matrices[year] = df.loc[mask].corr()
    return matrices


def sliding_window(df, window=WINDOW):
    mats = {}
    for i in range(window, len(df)):
        end = df.index[i]
        window_df = df.iloc[i-window:i]
        mats[end] = window_df.corr()
    return mats


def main():
    df = pd.read_csv(PROC_DIR / "log_returns.csv", index_col=0, parse_dates=True)

    # Annual
    annual = annual_correlations(df)
    writer = pd.ExcelWriter(OUT / "correlation_matrices_2017_2022.xlsx")
    for year, mat in annual.items():
        mat.to_excel(writer, sheet_name=str(year))
    writer.save()

    # Sliding window (optional)
    # sw = sliding_window(df)
    # for date, mat in sw.items():
    #     mat.to_pickle(OUT / f"corr_window_{date.date()}.pkl")

    print("Correlation matrices saved.")


if __name__ == "__main__":
    main()
