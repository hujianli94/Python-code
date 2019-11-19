#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 20:54
# filename: te.py
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"
}

url = "https://www.qiushibaike.com/text/page/3/"
res = requests.get(url, headers=headers)
print(res.status_code)
print(res.content.decode('utf-8'))