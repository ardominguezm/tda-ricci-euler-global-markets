"""
tda_analysis.py
----------------
Compute:
    - Persistence diagrams
    - Betti curves
    - Persistence entropy

Requires:
    pip install gudhi
"""

import numpy as np
import pandas as pd
import gudhi as gd
from pathlib import Path


def correlation_to_distance(C):
    return np.sqrt(2 * (1 - C))


def compute_persistence_diagram(dist_matrix):
    rips = gd.RipsComplex(distance_matrix=dist_matrix)
    st = rips.create_simplex_tree(max_dimension=2)
    return st.persistence()


def persistence_entropy(diagram):
    lifetimes = [b - d for d, b in diagram if b > d]
    p = np.array(lifetimes) / np.sum(lifetimes)
    return -np.sum(p * np.log(p))


def main():
    print("Import this script into notebooks for TDA computations.")


if __name__ == "__main__":
    main()

