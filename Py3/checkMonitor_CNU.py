import requests
import json
import time
from urllib import parse

# Author: Delppine Lorna
# Time: 2022.2.19
# Version: V1.5
# Channel: Official

username = ""  # CNU统一认证账号;
password = ""  # 登陆密码;
realname = ""

##################################################################################################

main_app = "https://app2018.cnu.edu.cn"

save_url = main_app + "/ncov/wap/default/save"

"""
login_url = main_app + "/uc/wap/login/check" 
info_url = main_app + "/ncov/wap/default/index"
"""

group_url = main_app + "/ncov/wap/datacube-base/ulists?date=" + time.strftime("%Y-%m-%d", time.localtime(
    time.time())) + "&type=count&page=1&page_size=20&group_id=10&group_type=1"

remind_url = main_app + "/ncov/wap/datacube-base/remind"

cookie = { # 需要使用fiddler进行抓包，在抓到的信息中获得该两个值
    "eai-sess": "", 
    "UUkey": "" 
}

headerC = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 "
                  "Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)"
}


def out(str):
    print(time.strftime("%Y.%m.%d %H:%M:%S: ", time.localtime(time.time())) + str)


def encode_formdata(obj):
    str = []
    for key in obj:
        str.append(parse.unquote(key) + "=" + parse.unquote(obj[key]))

    return_str = "&".join(str)
    return return_str


def auto_monitor():
    print("首师大疫情防控通签到督促")

    s = requests.session()

    remind_post = s.post(url=remind_url, headers=headerC, cookies=cookie)
    remind_data = json.loads(remind_post.content.decode("utf-8"))
    out("%s" % remind_data["m"])


if __name__ == "__main__":
    auto_monitor()
