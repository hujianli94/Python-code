#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 14:08
# filename: urlib模块2.py
import urllib.parse
import urllib.request

url = "http://www.cncrk.com/up/1801/201801051228459384.jpg"

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = "download.png"

    with open(f_name, "wb") as f:
        f.write(data)
        print("下载文件成功....")
