#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 13:50
# filename: 04.属性多值匹配.py
from lxml import etree

text = '''
<li class="li li-first"><a href="link.html"> first item</a><li>
'''

html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)