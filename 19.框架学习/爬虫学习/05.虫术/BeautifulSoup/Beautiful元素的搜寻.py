#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 9:43
# filename: Beautiful元素的搜寻.py
from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen("http://www.xz577.com/e/cxsj/").read()
soups = BeautifulSoup(html, 'lxml')

for i in soups.find_all('strong'):
    _name = i.text
    print(_name)
print()

# name = soups.select('body > div.g-box-1200.clearfix > div.g-listbox.f-fl.g-main-bg > ul > li > div > div.f-fl.m-leftbox > p > strong > a')
# for na in name:
#     print(na.get_text())
