# src/

This directory contains all the **modular Python scripts** used to reproduce
the complete analysis for the study:

"Network Geometry, Topology, and Spectral Analysis in Global Stock Markets
(2017–2022)."

The codebase is organized following a fully reproducible research pipeline,
from data acquisition to topological, geometric, and spectral analysis, and
finally figure generation.

Each script is independent but coordinated within the workflow described in
the main README.md.

---

## Scripts Overview

### 1. download_data.py
Downloads raw global stock market index data from Yahoo Finance using the
`yfinance` API.

Output:
- `data/raw/*.csv`

---

### 2. preprocess_data.py
Processes all raw CSV files by:
- aligning dates across all indices,
- handling missing values (forward/backward fill),
- generating log-returns.

Output:
- `data/processed/aligned_prices.csv`
- `data/processed/log_returns.csv`

---

### 3. compute_correlations.py
Computes:
- Annual correlation matrices (2017–2022)
- Full-period correlation matrix (2017–2022)
- Sliding-window correlation matrices (optional)

Output:
- `data/processed/correlation_matrices_2017_2022.xlsx`
- optional: individual window correlations in `.pkl` format

---

### 4. tda_analysis.py
Performs Topological Data Analysis (TDA):
- Rips complexes
- Persistent homology (H0, H1)
- Persistence diagrams
- Persistence entropy
- Betti numbers

Requires:
- `gudhi`

---

### 5. ricci_analysis.py
Computes **Ollivier–Ricci curvature** for:
- Annual correlation networks
- Dynamic sliding-window networks

Steps:
1. Convert correlation matrices to graphs
2. Build thresholded networks
3. Compute Ricci curvature on edges
4. Average curvature per graph

Requires:
- `GraphRicciCurvature`

---

### 6. euler_rmt_analysis.py
Calculates:
- Euler characteristic (χ)
- Maximum eigenvalue (λ_max) from RMT
- Combined structural/spectral metrics

Used in:
- Figures 3, 4, 5, 6 of the paper

---

### 7. plots_static.py
Generates **Figures 1–4** of the manuscript:
1. Annual correlation matrices (Fig. 1)
2. Thresholded graphs by region (Fig. 2)
3. Annual metrics barplots (λ_max, χ, κ, ρ̄) (Fig. 3)
4. Pairwise metric scatter plots (Fig. 4)

Output:
- `results/figures/`

---

### 8. plots_dynamic.py
Generates **Figures 5–6**:
- Sliding-window trajectories of λ_max, χ, κ
- COVID vs Pre/Post period segmentation
- 3D manifold visualization of metrics

Output:
- `results/figures/`

---

### 9. utils.py
General helper functions:
- correlation → distance transformations
- graph construction utilities
- period tagging (Pre-COVID, COVID, Post-COVID)
- plotting helpers

Imported by several scripts.

---

## Usage

Scripts can be executed independently:

    python src/download_data.py
    python src/preprocess_data.py
    python src/compute_correlations.py
    python src/ricci_analysis.py

Or through the notebooks in `notebooks/` for interactive execution.

---

## Notes

- No script writes outside `data/`, `results/`, or its own directory.
- All results are fully reproducible.
- Modify parameters (window size, thresholds, date ranges) inside each script.

---
```
