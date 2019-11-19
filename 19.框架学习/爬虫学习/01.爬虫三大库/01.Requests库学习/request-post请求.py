#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 9:50
# filename: request高级用法-post请求.py

import requests

data = {"name": "germey", 'age': '22'}

r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
