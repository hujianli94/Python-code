#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 9:32
# filename: request003.py
import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile(r'<a class="ExploreSpecialCard-contentTitle" (.*?)>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
for info in title:
    print(info[1])
