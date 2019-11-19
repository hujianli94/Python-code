#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 9:31
# filename: Beautifultest2.py
from bs4 import BeautifulSoup
from urllib import request

# html = BeautifulSoup('<h1>这是一个测试文档</h1>', "html.parser")
# print(html.h1)


# html = BeautifulSoup(request高级用法.urlopen("http://www.baidu.com"), 'html.parser')
# print(html.b)

html = BeautifulSoup(open(b"test.html", encoding='utf-8'), 'html.parser')
print(html.h1)
