#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/11/8 16:33
# filename: 天气test.py
import requests
import json

url = "http://v.juhe.cn/weather/index"

querystring = {"cityname":"北京","dtype\t":"","format\t":"","key":"91536efa9a578f9b33318278dc711eb5","format%09":"","dtype%09":""}

headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "8783f054-0c00-4067-b2fd-80791834f128,b5a087a4-44f9-42e4-8f53-54a211a5ca87",
    'Host': "v.juhe.cn",
    'cookie': "aliyungf_tc=AQAAAIxyLAxHaQEAmvFBfH548XCOpmpA",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
