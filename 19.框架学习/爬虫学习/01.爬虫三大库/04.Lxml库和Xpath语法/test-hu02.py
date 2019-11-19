#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 22:21
# filename: test-hu02.py
import requests
from lxml import etree

selector = etree.HTML(open("test-hu02.html", encoding="utf-8").read())
content1 = selector.xpath('//div[@class="red"]')[0]
content2 = content1.xpath('string(.)')
print(content2)
