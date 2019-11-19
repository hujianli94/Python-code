#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/27 12:16
# filename: request002.py
import requests

r = requests.get("https://accounts.douban.com/passport/login_popup?login_source=anony")
print("content---->", r.content)        #返回字节形式
print("text---->", r.text)              #返回文本形式
print("encoding---->", r.encoding)
r.encoding = "utf-8"
print("new text---->", r.text)
print(r.status_code)
print(r.cookies)
