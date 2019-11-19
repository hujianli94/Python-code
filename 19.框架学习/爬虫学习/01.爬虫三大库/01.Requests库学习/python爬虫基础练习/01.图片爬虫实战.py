#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/11 21:40
# filename: 01.图片爬虫实战.py
import re
import requests
import os
import urllib.request

"""
https://www.qiushibaike.com/pic/page/1/?s=5218576
https://www.qiushibaike.com/pic/page/2/?s=5218576
https://www.qiushibaike.com/pic/page/3/?s=5218576
https://www.qiushibaike.com/pic/page/4/?s=5218576
"""

urls = ["https://www.qiushibaike.com/pic/page/{}/?s=5218576".format(str(i)) for i in range(1, 31)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

URL_flag = "https:"


def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print("request高级用法 error")


def craw(url):
    html = get_html(url)
    Photo_info = re.findall('<img src=(.*?) alt=(.*?)>', html, re.S)
    for png in Photo_info:
        if str(png[1]).endswith('/'):
            photo_name = str(png[1]).strip('/').strip('"').strip().strip('"')
            photo_file_name = file_name + "/" + photo_name + ".jpg"
            photo_url = URL_flag + str(png[0]).strip('"')
            data = requests.get(photo_url)
            with open(photo_file_name, 'wb') as f:
                f.write(data.content)
                print("下载 {} 完成......".format(photo_file_name))

            # 或者使用如下方式进行下载
            # urllib.request高级用法.urlretrieve(photo_url, filename=photo_file_name)


if __name__ == '__main__':

    file_name = "download"
    if not os.path.exists(file_name):
        os.mkdir(file_name)

    for url in urls:
        craw(url)
