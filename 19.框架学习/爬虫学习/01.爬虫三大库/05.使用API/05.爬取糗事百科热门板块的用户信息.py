#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/13 23:44
# filename: 05.爬取糗事百科热门板块的用户信息.py
import requests
from lxml import etree
import csv
import json

"""
1.抓取糗事百科网的URL构造。
2.先爬取详细页的网站链接，进而爬取数据。
3.通过百度地图API进行用户位置的经纬度转换。
4.运用csv库，把爬取的信息存储在本地的CSV文件中。
"""

fp = open("D:/GitHub/21_staduy_python/19.框架学习/爬虫学习（旧版）/01.爬虫三大库/05.使用API/map.csv", "wt", newline="\n", encoding='utf-8-sig')
writer = csv.writer(fp)
writer.writerow(("address", "longitude", "latitude"))  # 写入header数据

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def get_user_url(url):
    """
    获取进入用户详细页URL的函数
    :param url:
    :return:
    """
    url_part = "https://www.qiushibaike.com"
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//li[starts-with(@id,"qiushi_tag")]')
    for url_info in url_infos:
        user_part_urls = url_info.xpath('div/div/a/@href')
        if len(user_part_urls) == 1:  # 判断用户是否有详细信息
            user_part_url = user_part_urls[0]
            user_part_url = url_part + user_part_url
            get_user_address(user_part_url)
            # print(user_part_url)
        else:
            pass  # 如无，则pass掉


def get_user_address(url):
    """
    获取用户地址信息
    :param url:
    :return:
    """
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    if selector.xpath('//div[@class="user-main clearfix"]/div[3]/div[2]/ul/li[5]/text()'):
        address_info = selector.xpath('//div[@class="user-main clearfix"]/div[3]/div[2]/ul/li[5]/text()')
        address_info = address_info[0].split('·')[0]
        get_geo(address_info)
        # print(address_info)
    else:
        pass


def get_geo(address):
    """
    定义获取用户地址的经纬度
    :param address:
    :return:
    """
    key = "svZI4iaMvmTqTaKEljF9oPyAkNShZzLV"
    api_url = "http://api.map.baidu.com/geocoding/v3/?address={0}&output=json&ak={1}&callback=showLocation".format(
        address, key)
    res = requests.get(api_url)
    res = res.text.strip("showLocation&&showLocation(").strip(")")
    json_date = json.loads(res)
    try:
        lng = json_date["result"]['location']['lng']
        lat = json_date["result"]['location']['lat']
        address = address
        writer.writerow((address, lng, lat))
        # print((address, lng, lat))

    except Exception as e:
        pass


if __name__ == '__main__':
    urls = ["https://www.qiushibaike.com/8hr/page/{}".format(str(i)) for i in range(1, 36)]
    for url in urls:
        get_user_url(url)

    # url = "https://www.qiushibaike.com/8hr/page/1"
    # get_user_url(url)

    # url = "https://www.qiushibaike.com/users/38730746"
    # get_user_address(url)

    # url = "https://www.qiushibaike.com/8hr/page/1"
    # get_user_url(url)
    # url = "https://www.qiushibaike.com/users/31617169/"
    # get_user_address(url)
    # get_geo("上海")
    # get_geo("武汉")
    # get_geo("北京")
    # get_geo("宜昌")
