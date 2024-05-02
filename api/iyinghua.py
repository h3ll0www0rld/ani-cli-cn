from requests_html import HTMLSession


class IYingHua:
    def __init__(self) -> None:
        self.SESSION = HTMLSession()
        self.BASE_URL = "http://www.iyinghua.io"

    def search(self, keyword: str) -> str:
        page_number = 1
        titles = []
        hrefs = []
        while True:
            search_url = f"{self.BASE_URL}/search/{keyword}?page={page_number}"
            response = self.SESSION.get(search_url)
            try:
                items = response.html.find("li > h2 > a")
            except:
                break
            if not items:
                break
            for item in items:
                titles.append(item.attrs["title"])
                hrefs.append(item.attrs["href"])
            page_number += 1
        return titles, hrefs

    def episodes(self, page_href: str) -> list[str]:
        response = self.SESSION.get(self.BASE_URL + page_href)
        video_page_hrefs = []
        ul_elements = response.html.find("div.movurl > ul")
        for ul in ul_elements:
            li_elements = ul.find("li")
            for li in li_elements:
                href = li.find("a", first=True).attrs.get("href")
                video_page_hrefs.append(href)
        return sorted(video_page_hrefs)

    def play(self, page_href: str) -> str:
        response = self.SESSION.get(self.BASE_URL + page_href)
        data_vid = None
        div_element = response.html.find("div.bofang > div[data-vid]", first=True)
        if div_element:
            data_vid = div_element.attrs.get("data-vid")
        return data_vid.replace("$mp4", "")
