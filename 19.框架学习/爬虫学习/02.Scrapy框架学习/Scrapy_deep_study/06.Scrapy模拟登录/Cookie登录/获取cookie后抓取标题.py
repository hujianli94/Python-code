#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/9 13:16
# filename: 获取cookie后抓取标题.py
import re
import browser_cookie3
import requests


get_title = lambda html: re.findall('<title>(.*?)</title>', html, flags=re.DOTALL)[0].strip()

url = 'https://bitbucket.org/'
cj = browser_cookie3.chrome()
# cj = browser_cookie3.chrome('https://bitbucket.org/product/')
r = requests.get(url, cookies=cj)
print(get_title(r.text))
print()
print()
print()
print()
print()

# for cookie in cj:
#     print(cookie)
#     print()