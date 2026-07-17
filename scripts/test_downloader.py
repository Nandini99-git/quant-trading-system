from src.data.downloader import BinanceDownloader


def main():
    downloader = BinanceDownloader()

    downloader.create_directory_structure()

    downloader.download_zip(
        timeframe="1h",
        year=2018,
        month=1,
    )


if __name__ == "__main__":
    main()