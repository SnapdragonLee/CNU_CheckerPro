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

main_app = "https://app2018.cnu.edu.cn"
save_url = main_app + "/ncov/wap/default/save"

/*login_url = main_app + "/uc/wap/login/check"
info_url = main_app + "/ncov/wap/default/index"*/

data = new Date();
dateformatter = new DateFormatter();
dateformatter.dateFormat = 'yyyy-MM-dd';

checkprocess_url = main_app + "/ncov/wap/datacube-base/fenji?date=" + dateformatter.string(data) +
    "&group_id=10";

group_url = main_app + "/ncov/wap/datacube-base/ulists?date=" + dateformatter.string(data) +
    "&type=count&page=1&page_size=20&group_id=10&group_type=1";

remind_url = main_app + "/ncov/wap/datacube-base/remind";

headerC = { /* 需要使用fiddler进行抓包，在抓到的信息中获得 Cookie 的两个值 */
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6305002e)",
    "Cookie": "eai-sess=; UUkey=",
};


notify = new Notification();
notify.title = "首师大疫情防控通信息查看";

function encode_formdata(obj) {
    var str = [];
    for (var key in obj) {
        if (obj.hasOwnProperty(key)) {
            str.push(encodeURIComponent(key) + "=" + encodeURIComponent(obj[key]));
            // console.log(key + " -> " + obj[key]);
        }
    }
    return str.join("&");
}

async function check() {

    console.log(save_url);
    console.log(checkprocess_url);
    console.log(group_url);
    console.log(remind_url);

    var save_data = { /* address 需要自己填写 */
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
    };

    // self checkin
    var req_save = new Request(save_url);

    req_save.headers = headerC;
    req_save.method = "POST";
    req_save.body = encode_formdata(save_data);

    var save_rsp_json = await req_save.loadJSON();

    console.log(save_rsp_json);
    notify.body = "上传成功！[" + username + "]" + save_rsp_json["m"] + "\n";

    // check "check-in" number
    var req_checkpro = new Request(checkprocess_url);

    req_checkpro.headers = headerC;
    req_checkpro.method = "POST";

    var checkpro_rsp_json = await req_checkpro.loadJSON();

    /* console.log(checkpro_rsp_json); */
    console.log("未申报人数：" + checkpro_rsp_json["d"]["datacube"]["weishangbao"]);
    notify.body += "未申报：" + checkpro_rsp_json["d"]["datacube"]["weishangbao"] + "人";

    // check "unchecked" name in group
    if (checkpro_rsp_json["d"]["datacube"]["weishangbao"] !== 0) {
        var req_group = new Request(group_url);

        req_group.headers = headerC;
        req_group.method = "POST";

        var group_rsp_json = await req_group.loadJSON();

        console.log(group_rsp_json);

        var unchecked_list = "";
        group_rsp_json["d"]["lists"].forEach(element => {
                if (element["status"] === "-") {
                    unchecked_list += element["realname"] + " ";
                }
            }
        );
        console.log(unchecked_list);
        notify.body += "，分别为：" + unchecked_list;

        return true;
    }
}

await check();

notify.schedule();
Script.complete();