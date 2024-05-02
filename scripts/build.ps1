$env:PYPPETEER_CHROMIUM_REVISION='1263111'
pip install -r requirements.txt
$filePath = "c:\hostedtoolcache\windows\python\3.11.9\x64\lib\site-packages\pyppeteerchromium_downloader.py"
# 修改chromium镜像位置
$lineNumber = 29
$newLineContent = 'DOWNLOAD_HOST = "https://registry.npmmirror.com/-/binary"'

(Get-Content $filePath) | ForEach-Object {
    if ($_.ReadCount -eq $lineNumber) {
        $_ -replace 'DOWNLOAD_HOST = ".+"', $newLineContent
    } else {
        $_
    }
} | Set-Content $filePath

$lineNumber = 32
$newLineContent = 'REVISION = "1294824"'

(Get-Content $filePath) | ForEach-Object {
    if ($_.ReadCount -eq $lineNumber) {
        $_ -replace 'DOWNLOAD_HOST = ".+"', $newLineContent
    } else {
        $_
    }
} | Set-Content $filePath
pyinstaller -F main.py
Rename-Item -Path "./dist/main.exe" -NewName "ani-cli-cn.exe"