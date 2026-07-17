from src.data.downloader import BinanceDownloader

downloader = BinanceDownloader()

downloader.create_directory_structure()

url = downloader.build_download_url(
    timeframe="1h",
    year=2018,
    month=1,
)

print(url)