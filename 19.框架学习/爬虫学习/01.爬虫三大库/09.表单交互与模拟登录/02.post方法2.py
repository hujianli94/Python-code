#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/21 13:47
# filename: 02.post方法2.py
import requests

url = "https://accounts.douban.com/passport/login"
params = {
    "username": "13262662216",
    "password": "cu0gu0ai@94"
}

html = requests.post(url, params)
print(html.text)