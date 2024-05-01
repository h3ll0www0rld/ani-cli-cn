import subprocess


class MPV:
    def __init__(self) -> None:
        pass

    def play(self, url: str) -> None:
        subprocess.run(
            ["mpv", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
        )
