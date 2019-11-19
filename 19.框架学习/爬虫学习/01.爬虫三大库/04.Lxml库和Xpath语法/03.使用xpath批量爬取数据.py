#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/10 21:54
# filename: 03.使用xpath批量爬取数据.py

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

url = "https://www.qiushibaike.com/text/"
res = requests.get(url, headers=headers)
selector = etree.HTML(res.text)
url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
for url_info in url_infos:
    id = url_info.xpath("div[1]/a[2]/h2/text()")[0]
    print(id)

# //*[@id="qiushi_tag_121978518"]/div[1]/a[2]/h2
# //*[@id="qiushi_tag_121978518"]
