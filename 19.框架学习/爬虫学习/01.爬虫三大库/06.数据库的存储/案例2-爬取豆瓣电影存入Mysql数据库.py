#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/14 17:38
# filename: 案例2-爬取豆瓣电影存入Mysql数据库.py

import requests
import time
from bs4 import BeautifulSoup
from lxml import etree
import re
import pymysql

"""
手动浏览豆瓣电影的网页结构如下
https://movie.douban.com/review/best/?start=0
https://movie.douban.com/review/best/?start=20
https://movie.douban.com/review/best/?start=40
https://movie.douban.com/review/best/?start=60
"""

conn = pymysql.connect(host="localhost", user="root", passwd="admin#123", db="sqlyog",
                       port=3306, charset="utf8")
cursor = conn.cursor()  # 连接数据库及光标

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def get_movie_url(url):
    """
    定义获取URL详细页的函数
    :param url:
    :return:
    """
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="main review-item"]/a/@href')
    for movie_href in movie_hrefs:
        # print(movie_href)
        get_movie_info(movie_href)  # 调用获取详细页的函数


def get_movie_info(url):
    """
    获取详细页信息的函数
    :param url:
    :return:
    """
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)

    # 这里通过try来处理，防止报错就停止爬取
    try:

        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        daoyan = selector.xpath('//*[@id="info"]/span[1]/span[2]//a/text()')
        daoyan = "/".join(daoyan)
        zhuyans = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        zhuyan = zhuyans.xpath('string(.)')
        style = re.findall(r'<span property="v:genre">(.*?)</span>', html.text, re.S)
        style = "/".join(style)
        country = re.findall(r'<span class="pl">制片国家/地区:</span> (.*?)<br/>', html.text, re.S)[0]
        release_time = re.findall(r'<span property="v:initialReleaseDate" content="(.*?)">(.*?)</span>', html.text,
                                  re.S)[0][0]
        time = re.findall(r'片长:</span>(.*?)>(.*?)</span>', html.text, re.S)[0][1]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]

        # print(str(name), str(daoyan), str(zhuyan), str(style)), \
        # str(country), str(release_time), str(time), str(score)

        # 获取信息插入数据库
        cursor.execute("insert into doubanmovie (name, director, actor, style, country, release_time, time, score) "
                       "values (%s,%s,%s,%s,%s,%s,%s,%s)",
                       (str(name), str(daoyan), str(zhuyan), str(style),
                        str(country), str(release_time), str(time), str(score)))

    except:
        pass


if __name__ == '__main__':
    # url = "https://movie.douban.com/review/best/?start=0"
    # get_movie_url(url)

    # url = "https://movie.douban.com/subject/4739952/"
    # get_movie_info(url)
    urls = ["https://movie.douban.com/review/best/?start={}".format(str(i)) for i in range(0, 200, 20)]
    for url in urls:
        get_movie_url(url)
        time.sleep(1)
    conn.commit()
    cursor.close()
    conn.close()
