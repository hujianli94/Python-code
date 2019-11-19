#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 9:16
# filename: BeautifulSouptest.py
from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen("http://www.baidu.com")
bs = BeautifulSoup(response.read(), 'html.parser')
print(bs.title)     #<title>百度一下，你就知道</title>
# print(bs)
