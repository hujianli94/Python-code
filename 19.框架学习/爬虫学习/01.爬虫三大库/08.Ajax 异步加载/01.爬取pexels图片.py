#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/19 16:09
# filename: 01.爬取pexels图片.py
import requests
from bs4 import BeautifulSoup
import time
import os
from multiprocessing import Pool

Dir_name = "Poxels/"


def chek_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def get_images(url):
    headers = {
        "apiKey": "883991539",
        "ui": "121105726",
        "anonymousId": "w4ur7qzdnxb",
        "type": "page",
        "userAgent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.142Safari/537.36"
    }

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "lxml")
    images = soup.select(
        'article > a.js-photo-link.photo-item__link > img')
    # print(images)
    download_list = []
    for image in images:
        ims = image.get('data-big-src')
        download_list.append(ims)

    for item in download_list:
        res = requests.get(item, headers=headers)
        file_name = item.split("?")[0].split('/')[-1]
        # print(file_name)
        if Dir_name.endswith("/"):
            image_name = Dir_name + file_name
        else:
            image_name = Dir_name + "/" + file_name

        with open(image_name, "wb") as f:
            f.write(res.content)
            print("下载{}图片完成。".format(file_name))


if __name__ == '__main__':
    chek_dir(Dir_name)
    # url = 'https://www.pexels.com/search/book'
    urls = ['https://www.pexels.com/search/girl/?page={}'.format(str(i)) for i in range(2, 11)]
    # for url in urls:
    #     get_images(url)       #单进程爬取

    pool = Pool(processes=4)
    pool.map(get_images, urls)      #多进程爬取
