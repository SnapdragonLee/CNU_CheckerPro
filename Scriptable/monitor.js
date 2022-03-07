// Variables used by Scriptable.
// These must be at the very top of the file. Do not edit.
// icon-color: deep-purple; icon-glyph: magic;

/* Author: Delppine Lorna
 * Time: 2022.2.15
 * Version: V1.35
 * Channel: Official
 */

username = ""; // CNU学生姓名;

/**********************************************************************************/

main_app = "https://app2018.cnu.edu.cn";

remind_url = main_app + "/ncov/wap/datacube-base/remind";

headerC = { /* 需要使用fiddler进行抓包，在抓到的信息中获得 Cookie 的两个值 */
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)",
    "Cookie": "eai-sess=; UUkey="
};


notify = new Notification();
notify.title = "首师大疫情防控通签到督促";

async function check() {

    var req_remind = new Request(remind_url);
    req_remind.headers = headerC;
    req_remind.method = "POST";
    var remind_rsp_json = await req_remind.loadJSON();

    console.log(remind_rsp_json);
    notify.body = "提醒请求上传成功！\n" + remind_rsp_json["m"];

    return true;
}

await check();

notify.schedule();
Script.complete();