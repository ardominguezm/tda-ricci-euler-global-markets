"""
download_data.py
-----------------
Download daily prices for global stock indices using Yahoo Finance.

Outputs:
    data/raw/<Country>.csv
"""

import yfinance as yf
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw/")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# List of indices (example – replace with your list)
INDICES = {
    "United_States": "^GSPC",
    "Germany": "^GDAXI",
    "Japan": "^N225",
    # add all your indices…
}

START = "2017-01-01"
END = "2022-12-31"


def download_index(name, ticker):
    print(f"Downloading {name} ({ticker})...")
    df = yf.download(ticker, start=START, end=END)
    df.to_csv(RAW_DIR / f"{name}.csv")
    return df


def main():
    for country, ticker in INDICES.items():
        download_index(country, ticker)

    print("\nDownload completed. Files saved in data/raw/")


if __name__ == "__main__":
    main()
