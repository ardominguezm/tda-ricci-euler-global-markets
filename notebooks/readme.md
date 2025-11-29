# notebooks/

This directory contains the **interactive Jupyter notebooks** used to reproduce
the full analysis pipeline of the study:

"Network Geometry, Topology, and Spectral Analysis in Global Stock Markets(2017–2022)."

Each notebook corresponds to a sequential phase of the workflow, from
data ingestion to the static and dynamic analyses presented in the manuscript.

---

# Notebook Structure

## 01_download.ipynb
Downloads daily historical prices for all global stock indices from Yahoo
Finance.

Contains:
- Ticker list
- Automated fetch routine
- Raw file export to `data/raw/`

Output:
- CSV files of each index in `data/raw/`

---

## 02_preprocess.ipynb
Cleans and synchronizes raw price data.

Operations:
- Align index timelines
- Fill missing values
- Compute log-returns
- Basic quality checks

Output:
- `aligned_prices.csv`
- `log_returns.csv`
(stored in `data/processed/`)

---

## 03_annual_analysis.ipynb
Performs the **static yearly analysis** used in Figures 1–4.

Includes:
- Annual correlation matrices (2017–2022)
- Graph construction
- Euler characteristic (χ)
- Ricci curvature (κ)
- Maximum eigenvalue (λ_max)
- Persistence diagrams and entropy (TDA)

Outputs saved in:
- `results/figures/`
- `results/tables/`

---

## 04_sliding_window.ipynb
Implements the **dynamic analysis** (sliding window) used in Figures 5–6.

Pipeline:
- Rolling correlation matrices
- Time series of λ_max, χ, κ
- Pre-COVID / COVID / Post-COVID segmentation
- Visualization of local/global structural transitions

Outputs:
- Dynamic figures
- CSV with trajectories of all metrics

---

# How to Use the Notebooks

1. Create the environment:

       conda env create -f environment.yml
       conda activate tda-ricci-env

   or

       pip install -r requirements.txt

2. Run notebooks in the following order:

       01_download.ipynb
       02_preprocess.ipynb
       03_annual_analysis.ipynb
       04_sliding_window.ipynb

3. All generated outputs are stored automatically in:
   - `data/processed/`
   - `results/figures/`
   - `results/tables/`

---

# Notes

- Notebooks are designed for reproducibility.
- All heavy computations (TDA, Ricci curvature) are modularized inside `src/`.
- The notebooks should be used as high-level interfaces for exploration and
  visualization.

---
```
