pip install -r requirements.txt
pyinstaller -F main.py
Rename-Item -Path "./dist/main.exe" -NewName "ani-cli-cn.exe"
Copy-Item "./scripts/install.ps1" -Destination "./dist"