# data/raw/

This folder contains the **raw financial time series** downloaded directly from
**Yahoo Finance** using the script:

    src/download_data.py

Each file corresponds to one global stock market index and is stored in CSV
format, named as:

    CountryName.csv

Example:

    United States.csv
    Germany.csv
    Japan.csv

## Contents

- Daily historical prices (Open, High, Low, Close, Adj Close, Volume)
- Downloaded for the period **2017-01-01 to 2022-12-31**
- No preprocessing, no cleaning, no alignment
- Missing values are preserved exactly as downloaded

## Purpose

The files in this folder are intended to be:

1. **Unmodified archival data**
2. **Input for the preprocessing pipeline**
3. **Reproducible evidence** of the original source (Yahoo Finance)

## Next step in the pipeline

Run:

    python src/preprocess_data.py

to generate:

- aligned_prices.csv  
- log_returns.csv

which will be stored in `data/processed/`.

---
```

