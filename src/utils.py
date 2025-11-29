"""
utils.py
---------
Helper functions used across modules.
"""

import numpy as np
import pandas as pd


def corr_to_dist(C):
    return np.sqrt(2 * (1 - C))


def tag_period(date):
    if date < pd.Timestamp("2020-01-01"):
        return "Pre-COVID"
    elif date <= pd.Timestamp("2021-12-31"):
        return "COVID"
    else:
        return "Post-COVID"


def normalize_matrix(M):
    return (M - M.min()) / (M.max() - M.min())


def safe_log_returns(df):
    return np.log(df / df.shift(1)).replace([np.inf, -np.inf], np.nan).dropna()


def main():
    print("Utility functions loaded.")


if __name__ == "__main__":
    main()
