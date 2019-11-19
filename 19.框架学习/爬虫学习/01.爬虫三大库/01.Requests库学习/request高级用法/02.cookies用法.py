#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:01
# filename: 02.cookies用法.py
import requests

r = requests.get("https://www.baidu.com")
print(r.cookies)

for key,value in r.cookies.items():
    print(key + "=" + value)
