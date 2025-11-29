"""
ricci_analysis.py
------------------
Compute Ollivier-Ricci curvature for:
    - Annual networks
    - Dynamic sliding-window networks

Requires:
    pip install GraphRicciCurvature
"""

import pandas as pd
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from pathlib import Path


def build_graph_from_corr(C, threshold=0.5):
    G = nx.Graph()
    for i in C.columns:
        for j in C.columns:
            if i < j and C.loc[i, j] > threshold:
                G.add_edge(i, j, weight=1 - C.loc[i, j])
    return G


def compute_ricci(G):
    orc = OllivierRicci(G, alpha=0.5)
    orc.compute_ricci_curvature()
    return orc.G


def main():
    print("Run this inside notebooks or analysis scripts.")


if __name__ == "__main__":
    main()
