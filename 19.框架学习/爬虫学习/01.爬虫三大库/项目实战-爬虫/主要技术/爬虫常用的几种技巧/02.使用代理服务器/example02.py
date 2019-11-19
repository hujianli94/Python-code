#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/12 23:02
# filename: example02.py
import urllib.request


def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


proxy_addr = "222.249.238.138:8080"
data = use_proxy(proxy_addr, "https://movie.douban.com/")
# print(len(data))
print(data)