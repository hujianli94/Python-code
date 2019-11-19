#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 21:07
# filename: 01.基础篇.py
from lxml import etree
import requests

'''
# 修正HTML代码
parser = etree.HTMLParser(encoding="utf-8")
html = etree.HTML("test001.html", parser=parser)
result = etree.tostring(html)
print(result)

# 读取HTML文件
parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("test001.html", parser=parser)
result = etree.tostring(html, pretty_print=True)
print(result)
'''

# 解析HTML文件

## 代理头文件
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = "http://www.doupoxs.com/"
res = requests.get(url, headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)
