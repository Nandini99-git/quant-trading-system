"""
Downloader Module

Responsible for:
1. Creating the project directory structure
2. Generating Binance Vision download URLs
3. Downloading historical ZIP files
"""

from pathlib import Path
import requests

from config.settings import (
    RAW_DATA_DIR,
    DOWNLOADS_DIR,
    SYMBOL,
    TIMEFRAMES,
    BASE_DOWNLOAD_URL,
)


class BinanceDownloader:
    """
    Handles Binance historical market data.
    """

    def __init__(self):
        self.base_path = Path(RAW_DATA_DIR)
        self.download_path = Path(DOWNLOADS_DIR)

        self.symbol = SYMBOL
        self.timeframes = TIMEFRAMES

    def create_directory_structure(self):
        """
        Create all required project directories.
        """

        # Create download directory
        self.download_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Create raw data directory
        symbol_path = self.base_path / self.symbol

        symbol_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Create timeframe directories
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
        Build the Binance Vision download URL.
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

    def download_zip(
        self,
        timeframe: str,
        year: int,
        month: int,
    ):
        """
        Download one monthly Binance ZIP file.
        """

        url = self.build_download_url(
            timeframe,
            year,
            month,
        )

        month = f"{month:02d}"

        filename = (
            f"{self.symbol}-{timeframe}-{year}-{month}.zip"
        )

        save_path = self.download_path / filename

        print("=" * 60)
        print("Downloading Historical Data")
        print("=" * 60)
        print(f"Symbol     : {self.symbol}")
        print(f"Timeframe  : {timeframe}")
        print(f"Year       : {year}")
        print(f"Month      : {month}")
        print(f"URL        : {url}")
        print()

        response = requests.get(url, timeout=30)

        if response.status_code == 200:

            with open(save_path, "wb") as file:
                file.write(response.content)

            print("Download Successful!")
            print(f"Saved to: {save_path}")

        else:

            raise Exception(
                f"Download failed! HTTP Status Code: {response.status_code}"
            )