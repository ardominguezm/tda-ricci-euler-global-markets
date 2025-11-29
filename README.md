# Topological and Geometric Analysis of Global Stock Markets


---

## Overview

This repository contains the reproducible code used in the study:

> Domínguez-Monterroza A., Jiménez-Martínez A., and  Mateos-Caballero A., *Network Geometry, Topology, and Spectral Analysis in Global Stock Markets: Insights from Ricci Curvature, Euler Characteristic, and Random Matrix Theory*, Plos One, 2025, In review.

The project analyzes 45 global stock indices from 2017 to 2022 using a combined framework of:

- **Topological Data Analysis (TDA)**
- **Network Geometry (Ollivier–Ricci curvature)**
- **Euler Characteristic**
- **Random Matrix Theory (RMT)**
- **Sliding-window dynamical analysis**

---
## Acknowledgements
This paper was supported by the grants PID2021-122209OB-C31, RED2022-134540-T and PID2024-155179NB-C22 funded
by MICIU/AEI/10.13039/501100011033.

## Repository Structure

```
tda-ricci-euler-global-stock-markets/
│
├── data/
│   ├── raw/              # Raw downloaded index prices (Yahoo Finance)
│   ├── interim/          # Temporally aligned, NA-filled data
│   └── processed/        # Log-returns, correlation matrices, etc.
│
├── src/
│   ├── download_data.py        # Download global stock index data
│   ├── preprocess_data.py      # Align, clean, and compute log-returns
│   ├── compute_correlations.py # Annual and sliding-window correlations
│   ├── tda_analysis.py         # Persistence diagrams, Betti numbers, entropy
│   ├── ricci_analysis.py       # Ricci curvature (static and dynamic)
│   ├── euler_rmt_analysis.py   # Euler characteristic + λ_max computation
│   ├── plots_static.py         # Figures 1–4 (annual analysis)
│   ├── plots_dynamic.py        # Figures 5–6 (sliding window)
│   └── utils.py                # Helper functions
│
├── notebooks/
│   ├── 01_download.ipynb
│   ├── 02_preprocess.ipynb
│   ├── 03_annual_analysis.ipynb
│   └── 04_sliding_window.ipynb
│
├── results/
│   ├── figures/    # Output figures used in the paper
│   └── tables/     # CSV/TEX for tables
│
├── environment.yml
├── requirements.txt
├── CITATION.cff
└── LICENSE
```
