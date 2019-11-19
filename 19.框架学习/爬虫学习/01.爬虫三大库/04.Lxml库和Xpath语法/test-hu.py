#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 22:06
# filename: test-hu.py
import requests
from lxml import etree
html1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<li class="tag-1">需要的内容1</li>
<li class="tag-2">需要的内容2</li>
<li class="tag-3">需要的内容3</li>

</body>
</html>
"""
selector = etree.HTML(html1)                                                    # 直接读取html文件内容
# selecctor = etree.HTML(open("test-hu01.html", encoding="utf-8").read())       #打开html文件进行爬取过滤
contenrs = selector.xpath('//li[starts-with(@class,"tag")]/text()')             # starts-with()可以获取类似标签的信息
for content in contenrs:
    print(content)  # starts-with()可以获取类似标签的信息

# /html/body/li[1]
