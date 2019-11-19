#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/19 9:50
# filename: check001.py
import requests
from lxml import etree

url = "https://www.jianshu.com/p/befe5db4051e"

html = requests.get(url)
selector = etree.HTML(html.text)
infos = selector.xpath('//a[@class="item"]')
print(infos)