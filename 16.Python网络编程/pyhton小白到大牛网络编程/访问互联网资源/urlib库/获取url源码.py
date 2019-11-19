#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/24 10:58
# filename: 获取url源码.py
import urllib.request

with urllib.request.urlopen("http://www.sina.com.cn/") as response:
    data = response.read()
    html = data.decode()
    print(html)