#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 13:50
# filename: 04.属性多值匹配.py
from lxml import etree

#
# text = '''
# <li class="li li-first" name="item"><a href="link.html"> first item</a><li>
# '''
#
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

html = etree.parse('test-hu01.html', etree.HTMLParser())
result = html.xpath('//li/text()')
print(result)


"""
html = etree.parse('test-hu01.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
"""

