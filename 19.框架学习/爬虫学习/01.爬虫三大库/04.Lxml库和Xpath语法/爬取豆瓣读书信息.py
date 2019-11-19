#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/12 16:06
# filename: 爬取豆瓣读书信息.py

import requests
from lxml import etree  # 导入3个库:lxml、csv、requests
import csv

# <p class="pl">[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元</p>
# //*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[2]

fp = open("douban.csv", "wt", newline='', encoding="utf-8")
writer = csv.writer(fp)
writer.writerow(("书名", "链接", "作者", "出版社", "出版时间", "价格", "评分", "导语"))
urls = ["https://book.douban.com/top250?start={}".format(str(i)) for i in range(0, 25, 250)]
# 加入请求头部
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}
for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath("td[2]/div[1]/a/@title")[0]
        url = info.xpath("td[2]/div[1]/a/@href")[0]
        book_infos = info.xpath("td[2]/p/text()")[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath("td[2]/div[2]/span[2]/text()")[0]
        comments = info.xpath("td[2]/p[2]/span/text()")
        comment = comments[0] if len(comments) != 0 else "空"

        writer.writerow((name, url, author, publisher, date, price, rate, comment))
fp.close()
