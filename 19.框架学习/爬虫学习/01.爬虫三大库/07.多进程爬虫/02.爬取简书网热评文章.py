#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/16 9:45
# filename: 02.爬取简书网热评文章.py

"""
【爬虫】Xpath高级用法

手动浏览翻页界面如下
https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=1
https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=12
https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=13
https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=14
https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page=15

使用requests和lxml三方库和多进程爬虫方法，
"""

import requests
from lxml import etree
import re
import pymongo
import time
import random
from multiprocessing import Pool  # 导入库文件

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']
jianshu_shouye = mydb['jianshu_shouye']  ## 连接数据库及创建数据库、数据集合
# jianshu_shouye.insert_one({'收藏数': '1', '评论数': '1', '作者': '恋戰', '标题': '【python】进程与多进程', '热度': '0.2'})

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}


def get_jianshu_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')  # 获取大标签，以此进行循环

    for info in infos:
        try:
            author = info.xpath('div/div/a[1]/text()')[0]
            tittles = info.xpath('div/a/text()')[0]
            redus = info.xpath('div/div/span[1]/text()')
            if len(redus) == 1:
                redu = str(redus).strip().replace('[', '').replace(']', '').strip("'").strip() + "/未知"
            else:
                redu = str(redus[1]).strip()
            pinglun = info.xpath('div/div/a[2]/text()')[1].strip()
            shoucangs = info.xpath('div/div/span[2]/text()')
            if len(shoucangs) == 0:
                shoucang = str(0)
            else:
                shoucang = str(shoucangs).replace('[', '').replace(']', '').strip("'").strip()

            data = {
                "作者": author,
                "标题": tittles,
                "热度": redu,
                "评论数": pinglun,
                "收藏数": shoucang
            }
            # print(data)
            jianshu_shouye.insert_one(data)  # 依次写入mongodb数据库
            time.sleep(random.random())

        except:
            pass


def priint1(name):
    print("Child process {}......".format(name))


if __name__ == '__main__':
    # urls = "https://www.jianshu.com/c/22f2ca261b85"
    # get_jianshu_info(urls)
    urls = ["https://www.jianshu.com/c/22f2ca261b85?order_by=added_at&page={}".format(str(i)) for i in range(1, 2000)]
    # print(urls)
    # for url in urls:              #单线程
    #     get_jianshu_info(url)

    pool = Pool(4)  # 创建4个进程池，多线程
    for url in urls:
        pool.apply_async(get_jianshu_info, args=(url,))
    pool.close()
    pool.join()
    print("【数据爬取】完毕！！！(*^▽^*)(^_−)☆(σﾟ∀ﾟ)σ..:*☆哎哟不错哦")



    # for i in range(5):
    #     pool.apply_async(priint1, args=(i,))
    # pool.close()
    # pool.join()