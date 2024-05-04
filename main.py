import tui.Tui as Tui
import os
import chromium_downloader

if __name__ == "__main__":
    username = os.environ.get("USERNAME")
    if os.path.exists(chromium_downloader.DOWNLOADS_FOLDER) != True:
        print("检测到未下载chromium，开始下载...")
        chromium_downloader.download_chromium()
        os.rename(
            os.path.join(chromium_downloader.DOWNLOADS_FOLDER,"1294824"),
            os.path.join(chromium_downloader.DOWNLOADS_FOLDER,"1181205"),
        )
        print("下载完成")
    Tui.main()
