#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/9 16:53
# filename: test01.py
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

res = requests.get("https://cq.xiaozhu.com/", headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
# 定位元素位置并通过selector方法提取
prices = soup.select("#page_list > ul > li > div > div > span.result_price > i")


for price in prices:
    print(price.get_text())
