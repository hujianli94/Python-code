#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/9 17:00
# filename: test02.py
import requests
from bs4 import BeautifulSoup

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
res = requests.get("https://www.zhipin.com/c101200100-p100109/?page=2&ka=page-2", headers=headers)
soup = BeautifulSoup(res.text, "html.parser")             #对返回的结果进行解析
prices = soup.select("#main > div > div.job-list > ul > li > div > div.info-primary > h3 > a > span")
for price in prices:
    print(price.get_text())