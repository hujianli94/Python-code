#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/18 17:35
# filename: main_many_Process.py
# 多进程
from multiprocessing import Pool
from class_urls import class_urls1
from page_spider import get_page, get_info
from page_spider import zhuanzhuan_url, zhuanzhuan_info


def get_links_from(url):
    for page in range(1, 20):
        get_page(url, page)


zz_urls = [item['详细页面链接'] for item in zhuanzhuan_url.find()]  # 获取数据库中的详细页面链接
zz_urls_2 = [item['链接'] for item in zhuanzhuan_info.find()]  # 数据表zhuanzhuan_info不存在时返回0
rest_urls = set(zz_urls) - set(zz_urls_2)  # 使用集合来过滤重复链接，支持断点续传

if __name__ == '__main__':
    url_list = class_urls1.split()  #将字符串转变成列表
    # pool = Pool(processes=4)      #创建进程池
    # pool.map(get_links_from, url_list)  #调用进程池

    # pool = Pool(processes=4)  # 创建进程池
    # pool.map(get_info, rest_urls)  # 调用进程池
