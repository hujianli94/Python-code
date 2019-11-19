#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/19 20:23
# filename: 02.爬取简书网用户动态信息.py
"""
https://www.jianshu.com/u/fcd9c8c68d63
爬取网址：https://www.jianshu.com/u/fcd9c8c68d63
爬取信息：用户动态类型，时间信息
爬取方式：使用bs4解析。
存储方式：打印出来


查询规律：
https://www.jianshu.com/users/fcd9c8c68d63/timeline?max_id=267789044&page=2
https://www.jianshu.com/users/fcd9c8c68d63/timeline?max_id=267789044&page=3
https://www.jianshu.com/users/fcd9c8c68d63/timeline?max_id=267789044&page=4
https://www.jianshu.com/users/fcd9c8c68d63/timeline?max_id=267789044&page=5


"""
import requests
import re
from lxml import etree
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
timeline = mydb['timeline']

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}


def get_time_info(url, page):
    user_id = url.split('/')

    user_id = user_id[4]
    if url.find('page='):
        page = page + 1
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[class="note-list"]/li')
    for info in infos:
        dd = info.xpath('div/div/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        timeline.insert_one({'data': dd, 'type': type})
    id_infos = selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(infos) > 1:
        feed_id = id_infos[-1]
        max_id = feed_id.split('-')[1]
        next_url = 'https://www.jianshu.com/users/{}/timeline?max_id={}&page={}'.format(user_id, max_id, page)
        get_time_info(next_url, page)



if __name__ == '__main__':
    url = "https://www.jianshu.com/users/fcd9c8c68d63/timeline"
    get_time_info(url, 1)


"""
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3294.6 Safari/537.36'}


##获取data_type和datetime信息。
def get_info(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    infos = soup.select("ul.note-list li")
    for info in infos:
        data_type = info.select("div.author span")[0].get("data-type")
        datetime = info.select("div.author span")[0].get("data-datetime")
        print(data_type, datetime)

    ##获取max_id信息


def get_id(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    max_id = soup.select("ul.note-list li")[-1].get("id").split("-")[1]
    return int(max_id)


if __name__ == "__main__":
    start_url = "https://www.jianshu.com/users/9104ebf5e177/timeline"
    get_info(start_url)
    max_id = get_id(start_url) + 1

    # 利用循环代替递归函数。
    for page in range(2, 11):
        next_url = "https://www.jianshu.com/users/9104ebf5e177/timeline?max_id={}&page={}".format(max_id, page)
        get_info(next_url)
        max_id = get_id(next_url) + 1

"""