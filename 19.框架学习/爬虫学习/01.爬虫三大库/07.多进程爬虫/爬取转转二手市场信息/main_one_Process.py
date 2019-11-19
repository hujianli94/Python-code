#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/18 17:34
# filename: main_one_Process.py

from class_urls import class_urls1
from page_spider import get_page, get_info

url_list = class_urls1.split()


for url in url_list:
    print(url)
    for page in range(1, 101):
        detail_url_list = get_page(url, page)
        for detail_url in detail_url_list:
            get_info(detail_url)
