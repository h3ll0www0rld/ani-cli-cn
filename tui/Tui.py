from tui.Selector import Selector
from api.iyinghua import IYingHua
from mpv import MPV
import curses


def main() -> None:
    keyword = input("KeyWord => ")
    source_list = ["iyinghua"]

    # curses selector
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.noecho()
    stdscr.keypad(True)

    # 选择源
    selected_source_index = Selector(stdscr, source_list).selected_item_index
    if selected_source_index == 0:
        session = IYingHua()
    # 选择番
    titles, links = session.search(keyword)
    selected_ani_index = Selector(stdscr, titles).selected_item_index
    # 选择集数
    video_links = session.episode(f"http://www.iyinghua.io" + links[selected_ani_index])
    selected_episode_index = Selector(
        stdscr, [f"第{i+1}集" for i in range(len(video_links))]
    ).selected_item_index

    curses.echo()
    curses.endwin()
    print("正在获取视频地址...")
    m3u8_link = session.play(
        f"http://www.iyinghua.io" + video_links[selected_episode_index]
    )
    print(f"获取成功，地址: {m3u8_link}")
    print("正在调用mpv进行播放...")
    player = MPV()
    player.play(m3u8_link)
