#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 11:42
# filename: 图片的爬取方法01.py

"""
urlretrieve(url,path)
url为图片链接,path为下载到本地的地址。
爬取妹子图代码如下
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import time
import urllib

urls = ["https://www.mzitu.com/188142/{}".format(str(i)) for i in range(1, 44)]

list_photos = []


# url = "https://www.mzitu.com/188142/4"

def get_html(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print("request高级用法 error")


path = "D:\GitHub\21_staduy_python\19.框架学习\爬虫学习\01.爬虫三大库\使用API\meizi_photo"


def get_down_photo(url):
    res = get_html(url)
    soup = BeautifulSoup(res, 'lxml')
    titeles = soup.select("body > div.main > div.content > h2")
    photos = soup.select("body > div.main > div.content > div.main-image > p > a > img")
    for img in photos:
        list_photos.append(img.get("src"))


if __name__ == '__main__':

    for url in urls:
        get_down_photo(url)

    for item in list_photos:
        urlretrieve(item, path + item[-10:])
    # # get_photo(url)
