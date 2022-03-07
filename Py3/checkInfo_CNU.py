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

checkprocess_url = main_app + "/ncov/wap/datacube-base/fenji?date=" + time.strftime("%Y-%m-%d", time.localtime(
    time.time())) + "&group_id=10"

group_url = main_app + "/ncov/wap/datacube-base/ulists?date=" + time.strftime("%Y-%m-%d", time.localtime(
    time.time())) + "&type=count&page=1&page_size=20&group_id=10&group_type=1"

cookie = { # 需要使用fiddler进行抓包，在抓到的信息中获得该两个值
    "eai-sess": "",
    "UUkey": ""
}

headerC = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 "
                  "Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)"
}


def out(string):
    print(time.strftime("%Y.%m.%d %H:%M:%S: ", time.localtime(time.time())) + string)


def encode_formdata(obj):
    str = []
    for key in obj:
        str.append(parse.unquote(key) + "=" + parse.unquote(obj[key]))

    return_str = "&".join(str)
    return return_str


def checkInfo():
    print("首师大疫情防控通信息查看")

    s = requests.session()

    stuchk_post = s.post(url=checkprocess_url, headers=headers, cookies=cookies)
    stuchk_data = json.loads(stuchk_post.content.decode("utf-8"))

    out("未上报人数：%d" % stuchk_data["d"]["datacube"]["weishangbao"])

    if stuchk_data["d"]["datacube"]["weishangbao"] != 0:
        out_string = ""
        group_post = s.post(url=group_url, headers=headerC, cookies=cookie)
        group_data = json.loads(group_post.content.decode("utf-8"), parse_int=str)

        for element in group_data["d"]["lists"]:
            if element["status"] == "-":
                out_string += element["realname"] + " "

        out("分别为：%s" % out_string)


if __name__ == "__main__":
    checkInfo()
