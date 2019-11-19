#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/11 13:44
# filename: 快递数据爬取.py

import requests
import json

url = "http://www.kuaidi100.com/query"

querystring = {"type": "shunfeng", "postid": "121213123"}

headers = {
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "www.kuaidi100.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json_data = json.loads(response.text)


with open("kuaidi1.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

with open("kuaidi2.json", "w", encoding="utf-8") as f_json:
    f_json.write(json.dumps(json_data, ensure_ascii=False, indent=4))
