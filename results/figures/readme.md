# results/figures/

This folder stores all **figures generated during the analysis** and used in the
manuscript:

"Network Geometry, Topology, and Spectral Analysis in Global Stock Markets (2017–2022)."

Figures are automatically produced by:
- `src/plots_static.py` (Figures 1–4)
- `src/plots_dynamic.py` (Figures 5–6)
- and by the notebooks inside `notebooks/`

---

# Figure Index

The figures follow the numbering used in the submitted manuscript.

---

## Figure 1 — Annual Correlation Matrices (2017–2022)
**Source:** `03_annual_analysis.ipynb` / `plots_static.py`

Contains:
- Heatmaps of correlation matrices for each year.
- Colormap: coolwarm, range [-1, 1].
- Used to illustrate structural changes in global stock market dependency.

Files:
- `corr_2017.png`
- `corr_2018.png`
- `corr_2019.png`
- `corr_2020.png`
- `corr_2021.png`
- `corr_2022.png`

---

## Figure 2 — Thresholded Market Networks (Annual)
**Source:** `03_annual_analysis.ipynb` / `plots_static.py`

Contains:
- Graphs constructed from annual correlations.
- Thresholding performed using ρ > 0.5.
- Node colors represent geographical regions.

Files:
- `network_2017.png`
- `network_2018.png`
- `network_2019.png`
- `network_2020.png`
- `network_2021.png`
- `network_2022.png`

---

## Figure 3 — Annual Summary Metrics
**Source:** `03_annual_analysis.ipynb`

Includes:
- Ricci curvature (κ)
- Euler characteristic (χ)
- Maximum eigenvalue λ_max
- Mean correlation

Visualizations:
- Barplots or line panels.

Saved as:
- `annual_metrics.png`

---

## Figure 4 — Metric Interactions (Scatter Plots)
**Source:** `03_annual_analysis.ipynb`

Plots showing pairwise interactions:
- κ vs λ_max  
- χ vs λ_max  
- κ vs χ  
- ρ̄ vs λ_max  

Used to show structural-spectral relationships.

File:
- `metric_interactions.png`

---

## Figure 5 — Dynamic Sliding-Window Analysis
**Source:** `04_sliding_window.ipynb` / `plots_dynamic.py`

Contains time series of:
- Ricci curvature (κ)
- Euler characteristic (χ)
- Maximum eigenvalue λ_max

Segmentation:
- Pre-COVID (Before Jan 2020)
- COVID (2020–2021)
- Post-COVID (2022)

File:
- `sliding_window_metrics.png`

---

## Figure 6 — 3D Structural Manifold (Optional)
**Source:** `04_sliding_window.ipynb`

Shows:
- Parametric embedding of (λ_max, χ, κ)
- Trajectory reveals the topological/geometric deformation during COVID.

File:
- `3d_metric_manifold.png`

---

# Notes

- All figures are reproducible with the provided scripts.
- Figures may also be exported in `.svg` or `.pdf` for publication.
- Intermediate visual outputs (debug plots) may also be stored here.

---
```
