```
# data/processed/

This folder contains **cleaned, aligned, and transformed datasets** generated
during the preprocessing and analysis pipeline.

These files are produced using:

    src/preprocess_data.py
    src/compute_correlations.py

## Files stored here

### 1. cleaned_global_stock_indices.csv
- All indices merged into a single time-aligned dataframe
- Missing values filled using:
  - Forward fill
  - Backward fill
- Indexed by date

### 2. log_returns.csv
- Log-returns computed as:
  
      log(P_t / P_{t-1})

- NA-free and aligned
- Used as input for all correlation, TDA, Ricci, Euler, and λ_max analyses

### 3. correlation_matrices_2017_2022.xlsx
- Annual correlation matrices (2017, 2018, 2019, 2020, 2021, 2022)
- Full-period correlation matrix (2017–2022)
- One sheet per year

### 4. Sliding-window correlation matrices (optional)
If enabled, the script stores:

    corr_window_YYYY-MM-DD.pkl

corresponding to each window end date.

## Purpose

The datasets in this folder are used as **primary input** for:

- Topological Data Analysis (tda_analysis.py)
- Ricci curvature analysis (ricci_analysis.py)
- Euler characteristic and RMT (euler_rmt_analysis.py)
- Paper figures (plots_static.py, plots_dynamic.py)

## Notes

No manual modifications should be made here.  
If any adjustment is required, modify the corresponding script in `src/`
and regenerate the processed data.

---
```

