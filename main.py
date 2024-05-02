import tui.Tui as Tui
import os
import chromium_downloader

if __name__ == "__main__":
    username = os.environ.get("USERNAME")
    path = (
        f"C:\\Users\\{username}\\AppData\\Local\\pyppeteer\\pyppeteer\\local-chromium"
    )
    if os.path.exists(path) != True:
        print("检测到未下载chromium，开始下载...")
        chromium_downloader.download_chromium()
        os.rename(
            f"C:\\Users\\{username}\\AppData\\Local\\pyppeteer\\pyppeteer\\local-chromium\\1294824",
            f"C:\\Users\\{username}\\AppData\\Local\\pyppeteer\\pyppeteer\\local-chromium\\1181205",
        )
        print("下载完成")
    Tui.main()
