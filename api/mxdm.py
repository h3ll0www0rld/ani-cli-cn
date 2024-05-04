# 弃用，过不了cloudflare检测

from requests_html import HTMLSession
import cloudscraper


class MXDM:
    def __init__(self) -> None:
        self.session = HTMLSession()
        self.scraper = cloudscraper.create_scraper(
            browser={"browser": "firefox", "platform": "windows", "mobile": False}
        )

    def search(self, url: str):
        # response = self.session.get(url)
        # response.html.render(timeout=8000)
        response = self.scraper.get(url)
        return response.text
