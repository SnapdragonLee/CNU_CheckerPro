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

checkprocess_url = main_app + "/ncov/wap/datacube-base/fenji?date=" + time.strftime("%Y-%m-%d", time.localtime(
    time.time())) + "&group_id=10"

group_url = main_app + "/ncov/wap/datacube-base/ulists?date=" + time.strftime("%Y-%m-%d", time.localtime(
    time.time())) + "&type=count&page=1&page_size=20&group_id=10&group_type=1"

remind_url = main_app + "/ncov/wap/datacube-base/remind"

users = [
    {
        "name": "",
        "cookie": { # 需要使用fiddler进行抓包，在抓到的信息中获得该两个值
            "eai-sess": "",
            "UUkey": ""
        }
    }
]

headerC = {    "Content-Type": "application/x-www-form-urlencoded",
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


def autoCheck(userCookie):
    print("首师大疫情防控通签到打卡")

    s = requests.session()

    data = { # address 需要自己填写
        "ismoved": "0",
        "jhfjrq": "",
        "jhfjjtgj": "",
        "jhfjhbcc": "",
        "szgj": "",
        "szcs": "",
        "zgfxdq": "0",
        "mjry": "0",
        "csmjry": "0",
        "tw": "2",
        "sfcxtz": "0",
        "sfyyjc": "0",
        "jcjgqr": "0",
        "jcjg": "",
        "sfjcbh": "0",
        "sfcxzysx": "0",
        "qksm": "",
        "remark": "",
        "address": "",
        "area": "北京市",
        "province": "北京市",
        "city": "北京市",
        "geo_api_info": "",
        "sfzx": "0",
        "sfjcwhry": "0",
        "sfcyglq": "0",
        "gllx": "",
        "glksrq": "",
        "jcbhlx": "",
        "jcbhrq": "",
        "sftjwh": "0",
        "sftjhb": "0",
        "fxyy": "",
        "bztcyy": "",
        "fjsj": "0",
        "sfjchbry": "0",
        "sfjcqz": "",
        "jcqzrq": "",
        "jcwhryfs": "",
        "jchbryfs": "",
        "xjzd": "",
        "sfsfbh": "false",
        "jhfjsftjwh": "0",
        "jhfjsftjhb": "0",
        "szsqsfybl": "0",
        "sfygtjzzfj": "0",
        "gtjzzfjsj": "",
        "sfsqhzjkk": "0",
        "sqhzjkkys": ""
    }

    save_data = encode_formdata(data).encode("utf-8")

    '''
        info = s.post(url=info_url, headerC=headerC, cookie=user["cookie"])

        def1 = re.findall("var def = (.*?);\n", info.content.decode("utf-8"))
        oldInfo = re.findall("oldInfo: (.*?),\n", info.content.decode("utf-8"))
    '''

    result = s.post(url=save_url, data=save_data, headers=headerC, cookies=userCookie["cookie"])

    out(userCookie["name"] + ":" + json.loads(result.text)["m"])


if __name__ == "__main__":
    for item in users:
        autoCheck(item)
