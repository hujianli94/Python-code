#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/15 13:52
# filename: 1.网络请求.py
import urllib.request
import urllib.parse  # 导入解析模块

# 创建参数
data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf-8")

# 发送post网络请求
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
html = response.read()
print(html)
