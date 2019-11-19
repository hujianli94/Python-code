#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/18 17:33
# filename: page_spider.py
import requests
from bs4 import BeautifulSoup
import time
import pymongo
import re

# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
zhuanzhuan_url = mydb['zhuanzhuan_url']
zhuanzhuan_info = mydb['zhuanzhuan_info']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3294.6 Safari/537.36'}


def get_page(url, page):
    url1 = url
    try:
        detail_url = '{}0/pn{}/'.format(url, page)
        # print(detail_url)
        r = requests.get(detail_url, headers=headers)
        # print(r.text)
        soup = BeautifulSoup(r.text, "lxml")
        infos = soup.select("tr")
        url_list = []       #单进程时使用
        for info in infos:
            detail_url = info.select("a.t")[0].get("href")
            # print(detail_url)
            if str(detail_url).endswith("slot=-1"):
                url_list.append(detail_url)        #单进程时使用
                zhuanzhuan_url.insert_one({'详细页面链接': detail_url})
                # print({'详细页面链接': detail_url})
            else:
                page
        return url_list   #单进程时使用
    except requests.exceptions.ConnectionError:
        pass


def get_info(url):
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        title = soup.select("#basicinfo > div.detail-title > h1")[0].text.strip()
        price = soup.select(
            "#basicinfo > div.infocard__container.haveswitch > div:nth-of-type(1) > div.infocard__container__item__main > span")[
            0].text.strip()
        area = soup.select(
            "#basicinfo > div.infocard__container.haveswitch > div:nth-of-type(3) > div.infocard__container__item__main > a")[
            0].text.strip()
        info = {'标题': title,
                '价格': price,
                '区域': area,
                '链接': url
                }
        zhuanzhuan_info.insert_one(info)
        # print(info)
        time.sleep(2)
    except IndexError:
        pass


if __name__ == '__main__':
    pass
    # url = "http://cs.58.com/shouji/"
    # get_page(url, 1)

    # url = 'https://cs.58.com/shouji/38763000384403x.shtml?link_abtest=&psid=176927105204931508910465081&entinfo=38763000384403_j&slot=-1'
    # get_info(url)
