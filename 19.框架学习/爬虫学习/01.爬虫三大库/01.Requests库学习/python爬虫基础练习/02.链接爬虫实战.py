#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/12 12:57
# filename: 02.链接爬虫实战.py
import requests
import re
import urllib
import string
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def get_html(url):
    try:
        html = requests.get(url, headers=headers)
        return html.text
    except:
        print("request高级用法 error")


def get_link(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    infos = soup.select('#feedlist_id  li  div  div.title  h2  a')
    for link in infos:
        # print(link.get_text().strip())
        title = link.get_text().strip()
        links = link.get("href").strip()
        data = {
            "标题": title,
            "链接": links
        }
        print(data)


if __name__ == '__main__':
    url = 'https://blog.csdn.net/nav/python'
    get_link(url)
