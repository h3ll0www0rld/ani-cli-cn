# 需要cookie
from requests_html import HTMLSession


class GiriGiriLove:
    def __init__(self) -> None:
        self.SESSION = HTMLSession()
        self.BASE_URL = "https://anime.girigirilove.com"

    def search(self, keyword: str) -> str:
        page_number = 1
        titles = []
        hrefs = []
        while True:
            search_url = f"{self.BASE_URL}/search/{keyword}----------{page_number}---/"
            response = self.SESSION.get(search_url)
            thumb_txts = response.html.find(".thumb-txt.cor4.hide")
            if not thumb_txts:
                break
            divs = response.html.find("div.left.public-list-bj")
            for i in range(min(len(thumb_txts), len(divs))):
                thumb_txt_text = thumb_txts[i].text
                div_href = divs[i].find("a")[0].attrs["href"]
                titles.append(thumb_txt_text)
                hrefs.append(div_href)
            page_number += 1
        return titles, hrefs

    def episodes(self, page_href: str) -> list[str]:
        response = self.SESSION.get(self.BASE_URL + page_href)
        ul = response.html.find("ul.anthology-list-play.size", first=True)
        hrefs = ul.find("li a")
        video_page_hrefs = [href.attrs["href"] for href in hrefs]
        return self.changeToSC(sorted(video_page_hrefs))

    def play(self, page_href: str) -> str:
        response = self.SESSION.get(self.BASE_URL + page_href)
        response.html.render()
        src = response.html.find("td#playleft iframe", first=True).attrs["src"]
        return src.split("=")[-1]

    def changeToSC(self, video_page_hrefs: list[str]):
        test_video_page_href = video_page_hrefs[0].replace("-1-", "-2-")
        response = self.SESSION.get(self.BASE_URL + test_video_page_href)
        if "m3u8" in response.html.html or "mp4" in response.html.html:
            return video_page_hrefs
        return [
            video_page_href.replace("-1-", "-2-")
            for video_page_href in video_page_hrefs
        ]
