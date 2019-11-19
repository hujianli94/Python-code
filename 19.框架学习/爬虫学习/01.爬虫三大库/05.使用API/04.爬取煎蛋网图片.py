#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 13:34
# filename: 04.爬取煎蛋网图片.py
import requests
from lxml import etree

urls = ["http://jandan.net/zoo/page-{}".format(str(i)) for i in range(1, 20)]
# url = "http://jandan.net/zoo/page-1"

path = "D://GitHub/21_staduy_python/19.框架学习/爬虫学习（旧版）/01.爬虫三大库/05.使用API/煎蛋网/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def get_photo(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    photo_urls = selector.xpath('//*[@id]/div/div/div[2]/p/a/@href')
    for photo_url in photo_urls:
        # print(photo_url)
        data = requests.get("http:" + photo_url, headers=header)
        with open(path + photo_url[-10:], "wb") as f:
            f.write(data.content)  # 把图片内容写入文件


if __name__ == '__main__':
    for url in urls:
        get_photo(url)