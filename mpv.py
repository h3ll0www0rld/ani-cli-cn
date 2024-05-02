import subprocess
import psutil
import sys


class MPV:
    def __init__(self, url: str) -> None:
        if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
            self.process_name = "mpv"
        elif sys.platform.startswith("win32"):
            self.process_name = "mpv.exe"
        else:
            raise NotImplementedError("Unsupported platform")
        process = subprocess.Popen(
            ["mpv", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def close(self) -> None:
        for process in psutil.process_iter():
            process_info = process.as_dict(attrs=["pid", "name"])
            if process_info["name"] == self.process_name:
                process.terminate()
