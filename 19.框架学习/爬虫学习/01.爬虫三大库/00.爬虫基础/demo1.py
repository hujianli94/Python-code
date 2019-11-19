#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/27 13:25
# filename: demo1.py
'''
import requests

# 网络请求地址
url = "http://www.whatismyip.com/"

# 发送网络请求
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36}"}
response = requests.get(url, headers=headers)
print(response.content.decode("utf-8"))

'''

import requests
#导入网络请求模块中的三种异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException

# 循环发送50次网络请求
for i in range(0, 50):
    try:
        response = requests.get("http://www.whatismyip.com/", timeout=0.5)
        print(response.status_code)    #打印请求码

    except ReadTimeout:
        # print("异常"+str(e))          #打印异常
        print("timeout ")


    except HTTPError:
        print("Http error")

    except RequestException:
        print("requerror")
