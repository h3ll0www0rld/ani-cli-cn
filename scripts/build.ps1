$env:PYPPETEER_CHROMIUM_REVISION='1263111'
pip install -r requirements.txt
pyinstaller -F main.py
Rename-Item -Path "./dist/main.exe" -NewName "ani-cli-cn.exe"