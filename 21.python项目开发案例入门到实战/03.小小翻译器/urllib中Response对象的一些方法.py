#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/24 14:23
# filename: urllib中Response对象的一些方法.py
from urllib import request

req = request.Request("https://fanyi.baidu.com/")
response = request.urlopen(req)

#获取url地址
print("geturl打印信息:{}".format(response.geturl()))
print("*" * 100)
#获取响应信息
print("info打印信息;{}".format(response.info()))
print("*" * 100)

#获取响应HTTP状态码
print("getcode打印信息:{}".format(response.getcode()))
