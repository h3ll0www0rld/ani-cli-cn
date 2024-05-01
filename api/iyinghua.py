from requests_html import HTMLSession


class IYingHua:
    def __init__(self) -> None:
        self.session = HTMLSession()

    def search(self, keyword: str) -> str:
        page_number = 1
        titles = []
        links = []
        while True:
            search_url = f"http://www.iyinghua.io/search/{keyword}?page={page_number}"
            response = self.session.get(search_url)
            try:
                items = response.html.find("li > h2 > a")
            except:
                break
            if not items:
                break
            for item in items:
                titles.append(item.attrs["title"])
                links.append(item.attrs["href"])
            page_number += 1
        return titles, links

    def episode(self, page_url: str) -> list[str]:
        response = self.session.get(page_url)
        video_links = []
        ul_elements = response.html.find("div.movurl > ul")
        for ul in ul_elements:
            li_elements = ul.find("li")
            for li in li_elements:
                href = li.find("a", first=True).attrs.get("href")
                video_links.append(href)
        return sorted(video_links)

    def play(self, page_url: str) -> str:
        response = self.session.get(page_url)
        data_vid = None
        div_element = response.html.find("div.bofang > div[data-vid]", first=True)
        if div_element:
            data_vid = div_element.attrs.get("data-vid")
        return data_vid.replace("$mp4", "")
