from tui.Selector import Selector
from tui.TextInputer import TextInputer
from api.iyinghua import IYingHua
from api.girigirilove import GiriGiriLove
from mpv import MPV
import os


def main() -> None:
    keyword = TextInputer("搜索关键词:").show()
    source_list = ["iyinghua", "girigirilove"]
    player_function_list = ["上一集", "下一集", "选择集数", "退出"]

    # 选择源
    selected_source_index = Selector("选择一个源:", source_list).show()
    if selected_source_index == 0:
        session = IYingHua()
    if selected_source_index == 1:
        session = GiriGiriLove()

    # 选择番
    titles, links = session.search(keyword)
    if titles == []:
        print("错误，搜索无结果")
        exit()
    os.system("cls" if os.name == "nt" else "clear")
    selected_ani_index = Selector("选择一部番:", titles).show()

    # 选择集数
    video_page_hrefs = session.episodes(links[selected_ani_index])
    os.system("cls" if os.name == "nt" else "clear")
    selected_episode_index = Selector(
        "选择集数:", [f"第{i+1}集" for i in range(len(video_page_hrefs))]
    ).show()
    video_link = session.play(video_page_hrefs[selected_episode_index])
    player = MPV(video_link)

    # 播放器菜单
    while True:
        if selected_episode_index == 0:
            tmp_player_function_list = player_function_list[1:]
        else:
            tmp_player_function_list = player_function_list
        os.system("cls" if os.name == "nt" else "clear")
        selected_player_function_index = Selector(
            f"播放器菜单(当前集数: 第{selected_episode_index+1}集):",
            tmp_player_function_list,
        ).show()
        if tmp_player_function_list[selected_player_function_index] == "上一集":
            selected_episode_index -= 1
            video_link = session.play(video_page_hrefs[selected_episode_index])
            player.close()
            player = MPV(video_link)
        elif tmp_player_function_list[selected_player_function_index] == "下一集":
            selected_episode_index += 1
            video_link = session.play(video_page_hrefs[selected_episode_index])
            player.close()
            player = MPV(video_link)
        elif tmp_player_function_list[selected_player_function_index] == "选择集数":
            os.system("cls" if os.name == "nt" else "clear")
            selected_episode_index = Selector(
                "选择一集:", [f"第{i+1}集" for i in range(len(video_page_hrefs))]
            ).show()
            video_link = session.play(video_page_hrefs[selected_episode_index])
            player.close()
            player = MPV(video_link)
        elif tmp_player_function_list[selected_player_function_index] == "退出":
            player.close()
            break
