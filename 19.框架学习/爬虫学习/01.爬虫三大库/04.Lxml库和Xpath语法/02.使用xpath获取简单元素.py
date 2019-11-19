#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 21:35
# filename: 02.使用xpath获取简单元素.py
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = "https://www.qiushibaike.com/text/"
res = requests.get(url, headers=headers)
parser = etree.HTMLParser(encoding="utf-8")
selector = etree.HTML(res.text, parser=parser)
id = selector.xpath("//*[@id=\"qiushi_tag_121978518\"]/div[1]/a[2]/h2/text()")[0]  # 通过/text()可以获取标签中的文字信息
print(id)
