# CNU_CheckerPro

## Description

CNU (首都师范大学) 自动签到与自动督促，有 iOS/iPadOS 12.0 以上系统 与 Python3 环境的脚本，此外还有自动发送 ios 系统通知，查看未打卡学生名单等功能。



## Usage

首先，需要使用 fiddler 在电脑端的微信或企业微信中打开健康打卡界面进行抓包，在抓到的信息中获得该两个值 `eai-sess`、`UUkey` 。获得后在所需要的脚本中填写相关的程序值（在每个程序中，这两个值出现在 Cookies 中，且已经标记了位置），在信息填报脚本中，需要填写打卡地址（代码中已标出）。



**Python Version**

在 `Py3` 文件夹中包含 3 个 Python3 脚本。`checkDaily_CNU.py` 是信息填报脚本，`checkInfo_CNU.py` 是未打卡学生信息查看脚本，`checkMonitor_CNU.py` 是监管角色发送督促打卡信息的脚本（任何具有监管权限的账号都可以使用）。



**iOS/iPadOS Scriptable Version**

在 `Scriptable` 文件夹中包含 2 个 Javascript 脚本。首先在 AppStore 中下载 `Scriptable`，之后新建一个脚本，并在其中粘贴从 `Scriptable` 文件夹中选取的脚本文件，并将其中的 headerC 中的 Cookie 填好。运行一下看看是否会报错，没有错误的话就可以用了，这个时候可以打开 Shortcuts(捷径)新建一个自动流程，在联网的情况下可完成 `自动` 的目的。

`checkInfo.js` 是信息填报和未打卡学生信息查看脚本（如果只想进行自动信息填报可注释掉 126~160 行），`monitor.js` 是班长等角色发送督促打卡信息的脚本。



## Attention

如果有任何疑问，可发起 Issue。如果您有新的代码想要发布，请使用 Pull Request 提交，我会思考后决定是否合并。



另外，此仓库以及转移至以下链接，请大家反馈时注意地址，以防找不到项目：

[SnapdragonLee/CNU_CheckerPro: CNU auto sign-in and supervise tools (github.com)](https://github.com/SnapdragonLee/CNU_CheckerPro) 
