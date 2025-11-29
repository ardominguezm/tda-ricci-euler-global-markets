"""
euler_rmt_analysis.py
----------------------
Compute:
    - Euler characteristic (χ)
    - Maximum eigenvalue (λ_max) for RMT analysis
"""

import numpy as np
import pandas as pd


def euler_characteristic(adj):
    triangles = np.trace(adj @ adj @ adj) / 6
    edges = np.sum(adj) / 2
    nodes = adj.shape[0]
    return nodes - edges + triangles


def lambda_max(C):
    vals = np.linalg.eigvals(C)
    return np.max(vals.real)


def main():
    print("Use inside annual or sliding-window analyses.")


if __name__ == "__main__":
    main()
