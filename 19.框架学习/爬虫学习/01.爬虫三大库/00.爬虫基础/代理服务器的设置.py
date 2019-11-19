#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/11 21:30
# filename: 代理服务器的设置.py
import urllib.request


def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


proxy_addr = "120.83.107.113:9999"
data = use_proxy(proxy_addr, "http://www.baidu.com")
# print(len(data))
print(data)

