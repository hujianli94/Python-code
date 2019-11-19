#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/19 15:12
# filename: urllib-request高级用法.py

from urllib import request, parse

url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Host": "httpbin.org"
}

dict = {
    "name": "hujianli"
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
