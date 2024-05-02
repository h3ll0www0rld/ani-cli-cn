$env:PYPPETEER_CHROMIUM_REVISION='1263111'
pip install -r requirements.txt
# 修改chromium镜像位置
$filePath = "c:\hostedtoolcache\windows\python\3.11.9\x64\lib\site-packages\pyppeteer\chromium_downloader.py"
$content = Get-Content $filePath
$content | ForEach-Object {
    if ($_ -match "REVISION") {
        $_ = 'REVISION = "1294824"'
    }
    $_
} | Set-Content $file -Force

$content = Get-Content $filePath
$content | ForEach-Object {
    if ($_ -match "DOWNLOAD_HOST") {
        $_ = 'DOWNLOAD_HOST = "https://registry.npmmirror.com/-/binary"'
    }
    $_
} | Set-Content $file -Force

pyinstaller -F main.py
Rename-Item -Path "./dist/main.exe" -NewName "ani-cli-cn.exe"