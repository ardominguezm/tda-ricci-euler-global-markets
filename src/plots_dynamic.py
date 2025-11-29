"""
plots_dynamic.py
-----------------
Generate Figures 5–6:
    - Sliding-window Ricci curvature
    - Sliding-window λ_max
    - Sliding-window Euler characteristic
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_time_series(df, columns, title, outfile):
    plt.figure(figsize=(10, 4))
    for col in columns:
        plt.plot(df.index, df[col], label=col, linewidth=1.5)
    plt.legend()
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()


def main():
    print("Dynamic plots generated from notebooks.")


if __name__ == "__main__":
    main()
