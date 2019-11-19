#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/8 16:36
# filename: 01.浏览器模拟-headers属性01.py
import requests

def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    #使用请求头部之后，对请求进行了包装
    res = requests.get(url, headers=headers)

    try:
        print(res.text)
    except ConnectionError:
        print("拒绝连接")
