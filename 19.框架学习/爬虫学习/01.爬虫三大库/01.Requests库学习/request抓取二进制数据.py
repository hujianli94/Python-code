#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 9:42
# filename: request抓取二进制数据.py
import requests

r = requests.get("http://www.xz577.com/uploads/1908/1-1ZQ1112AM21.jpg")
# print(r.text)  # 文本形式打印
# print(r.content)  # 二进制形式打印

# 保存图片到本地,'wb'表示以二进制方式打开，可以写入二进制文件
with open("book01.jpg", "wb") as f:
    f.write(r.content)
