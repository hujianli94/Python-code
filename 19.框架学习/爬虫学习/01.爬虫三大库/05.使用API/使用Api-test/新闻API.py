#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/8 16:46
# filename: 新闻API.py

import requests

url = "http://v.juhe.cn/toutiao/index"

querystring = {"type": "guonei", "key": "3371cc8759e01a06be2891604f428277"}

headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ebd54850-b9c8-4cf6-9d02-57ff884790b0,33d92f9c-13e5-49b8-b564-5dae408e03ce",
    'Host': "v.juhe.cn",
    'cookie': "aliyungf_tc=AQAAAIxyLAxHaQEAmvFBfH548XCOpmpA",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
