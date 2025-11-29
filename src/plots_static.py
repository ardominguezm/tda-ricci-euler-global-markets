"""
plots_static.py
----------------
Generate figures 1–4:
    - Annual correlation matrices
    - Annual network structures
    - Annual summary metrics
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path


def plot_corr_matrix(C, year):
    plt.figure(figsize=(8, 6))
    sns.heatmap(C, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(f"Correlation Matrix {year}")
    plt.tight_layout()
    plt.savefig(f"results/figures/corr_{year}.png")
    plt.close()


def main():
    print("Static plots generated from notebooks.")


if __name__ == "__main__":
    main()
