#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/18 12:08
# filename: 多进程抓取瓜子二手车.py
"""

手动浏览瓜子二手车的信息如下：
https://www.guazi.com/bj/audi/o1/#bread
https://www.guazi.com/bj/audi/o2/#bread
https://www.guazi.com/bj/audi/o3/#bread

# 翻页：
urls = ["https://www.guazi.com/bj/audi/o{}/#bread".format(str(i)) for i in range(1, 50)]
"""
import re
import requests
import time
from multiprocessing import Pool
from lxml import etree
import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']
guazi_2car = mydb['guazi']  ## 连接数据库及创建数据库、数据集合

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "uuid=90ed9f44-b20d-4ed8-a8e5-2fe9a107c527; antipas=69151747kC695T498278y598l82; user_city_id=12; ganji_uuid=1086212832684246083191; sessionid=cddd6039-f178-417d-ef82-3fc603fe1904; lg=1; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2290ed9f44-b20d-4ed8-a8e5-2fe9a107c527%22%2C%22sessionid%22%3A%22cddd6039-f178-417d-ef82-3fc603fe1904%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A43620202225%7D; cityDomain=bj; preTime=%7B%22last%22%3A1563424468%2C%22this%22%3A1563422804%2C%22pre%22%3A1563422804%7D",
    "Host": "www.guazi.com",
    "Referer": "https://www.guazi.com/bj/buy/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

guazi_url = "https://www.guazi.com"


def get_link_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="carlist clearfix js-top"]/li')
    for info in infos:
        href = info.xpath('a/@href')[0]
        href = guazi_url + str(href)
        # print(href)
        get_info_car(href)


def get_info_car(url):
    """
    抓取标题、
    上牌时间、 里程表信息、排量、变速箱、价格、原价
    :param url:
    :return:
    """
    html = requests.get(url, headers=headers)
    selettor = etree.HTML(html.text)
    try:
        tettile = re.findall(r'<h2 class="titlebox">(.*?)<span class="labels baomai">(.*?)</span>', html.text, re.S)[0][
            0].strip()
        pailiang = re.findall(r'<li class="three"><span>(.*?)</span>排量</li>', html.text, re.S)[0]
        btjs = re.findall(
            r'<span class="pricestype"><span class="f14">(.*?)</span>(.*?)<span class="f14">(.*?)</span></span>',
            html.text,
            re.S)
        if len(btjs) == 0:
            btj = "没有补贴"
        else:
            a, b, c = btjs[0]
            btj = a + str(b).strip() + c
        yuanjia = re.findall(r'<span class="newcarprice">(.*?)</span>', html.text, re.S)[0].strip()

        data = {
            "标题": tettile,
            "排量": pailiang,
            "补贴价格": btj,
            "原价": yuanjia
        }
        print(data)
        # guazi_2car.insert_one(data)

    except:
        pass


if __name__ == '__main__':
    urls = ["https://www.guazi.com/bj/audi/o{}/#bread".format(str(i)) for i in range(1, 50)]
    pool = Pool(4)  # 创建4个进程池，多线程
    for url in urls:
        pool.apply_async(get_link_url, args=(url,))
    pool.close()
    pool.join()


# pool.map(get_link_url, urls)

# urls = "https://www.guazi.com/bj/audi/o3/#bread"
# get_link_url(urls)

# url = "https://www.guazi.com/bj/37f5a6414ab7d2dex.htm#fr_page=list&fr_pos=city&fr_no=1"
# get_info_car(url)
