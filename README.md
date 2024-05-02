# ani-cli-cn
一个更适合中国宝宝体制的`ani-cli`

# 支持源列表
- iyinghua
- girigirilove

# 下载
请到`Github Actions`中的工件下载<br>
[h3ll0www0rld/ani-cli-cn/actions](https://github.com/h3ll0www0rld/ani-cli-cn/actions)

# 安装
本项目使用`mpv`作为播放器，请确保`mpv`在你的环境变量中(在终端输入`mpv --version`有输出)
## Windows
```shell
scoop install mpv
```

# 使用
## Windows
```shell
./ani-cli.exe
```
## Linux & Mac
```shell
./ani-cli
```

# 开发&构建
在项目根目录下先运行
```shell
pip install -r requirements.txt
```
安装依赖<br>
运行前，请运行`./setup.ps1`设置`PYPPETEER_CHROMIUM_REVISION`，不然可能会报错

对于`windows`用户，本项目提供了一键构建脚本<br>
在根目录下输入`./scripts/build.ps1`来进行构建
