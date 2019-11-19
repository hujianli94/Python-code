#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 14:03
# filename: urllib模块.py
import urllib.request

with urllib.request.urlopen("http://www.sina.com.cn/") as response:
    data = response.read()
    html = data.decode()
    print(html)