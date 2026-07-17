"""
Project Configuration
AI-Powered Quant Trading System
"""

# ======================================
# Exchange Configuration
# ======================================

EXCHANGE = "binance"

# ======================================
# Trading Instrument
# ======================================

SYMBOL = "BTCUSDT"

# ======================================
# Required Timeframes
# (As specified by mentor)
# ======================================

TIMEFRAMES = [
    "1m",
    "3m",
    "5m",
    "15m",
    "1h"
]

# ======================================
# Historical Dataset
# ======================================

START_YEAR = 2018
END_YEAR = 2025

TRAINING_YEARS = 4
TESTING_YEARS = 3

# ======================================
# Project Directories
# ======================================

RAW_DATA_DIR = "data/raw"

PROCESSED_DATA_DIR = "data/processed"

PARQUET_DIR = "data/parquet"

DOWNLOADS_DIR = "data/downloads"

# ======================================
# Download Configuration
# ======================================

DOWNLOADS_DIR = "data/downloads"

BASE_DOWNLOAD_URL = (
    "https://data.binance.vision/data/spot/monthly/klines"
)

# ======================================
# Binance Vision
# ======================================

BASE_DOWNLOAD_URL = (
    "https://data.binance.vision/data/spot/monthly/klines"
)