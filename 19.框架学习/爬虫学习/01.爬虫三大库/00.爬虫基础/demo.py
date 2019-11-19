#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/27 12:55
# filename: demo.py
"""
import urllib.request高级用法
import urllib.parse  # 导入解析模块

# 创建参数
data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf-8")

# 发送post网络请求
response = urllib.request高级用法.urlopen("http://httpbin.org/post", data=data)
html = response.read()
print(html)
"""

"""
import urllib3  # 导入标准库升级版模块

# 创建PoolManager对象，用于处理与线程的连接以及线程安全
http = urllib3.PoolManager()
# 发送网络请求
# response = http.request高级用法("GET", "http://www.baidu.com")
response = http.request高级用法("POST", "http://httpbin.org/post",fields={"word": "hello"})

print(response.data.decode())
"""

import requests  # 导入网络请求模块

#表单参数
data = {"word":"hello"}
# 发送网络请求
# response = requests.get("http://www.baidu.com/")
response = requests.post("http://httpbin.org/post",data)

print(response.status_code)
print(response.content.decode())

# # 打印状态码
# print("状态码：", response.status_code)
#
# # 打印请求地址
# print("请求地址", response.url)
#
# # 打印头部信息
# print("打印头部信息", response.headers)
# # 打印cookies信息
# print("cookie信息", response.cookies)
# # 打印文本源码
# print("打印文本源码", response.text)
#
# # 打印字节流源码
# print("打印字节码源码", response.content)
