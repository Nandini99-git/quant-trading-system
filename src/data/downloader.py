"""
Downloader Module

Responsible for preparing the directory structure
for historical market data.
"""

from pathlib import Path

from config.settings import (
    RAW_DATA_DIR,
    DOWNLOADS_DIR,
    SYMBOL,
    TIMEFRAMES,
    BASE_DOWNLOAD_URL,
)


class BinanceDownloader:
    """
    Handles Binance historical data preparation.
    """

    def __init__(self):
        self.base_path = Path(RAW_DATA_DIR)
        self.download_path = Path(DOWNLOADS_DIR)

        self.symbol = SYMBOL
        self.timeframes = TIMEFRAMES

    def create_directory_structure(self):
        """
        Create required directory structure.
        """

        # Temporary download folder
        self.download_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Raw data folder
        symbol_path = self.base_path / self.symbol

        symbol_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        for timeframe in self.timeframes:
            (symbol_path / timeframe).mkdir(
                parents=True,
                exist_ok=True,
            )

        print("Directory structure created successfully.")

    def build_download_url(
        self,
        timeframe: str,
        year: int,
        month: int,
    ):
        """
        Generate Binance Vision download URL.
        """

        month = f"{month:02d}"

        filename = (
            f"{self.symbol}-{timeframe}-{year}-{month}.zip"
        )

        url = (
            f"{BASE_DOWNLOAD_URL}/"
            f"{self.symbol}/"
            f"{timeframe}/"
            f"{filename}"
        )

        return url
