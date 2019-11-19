#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/12 16:01
# filename: 3种爬虫模式对比.py
# 爬取数据只做返回，不存储
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import time

# 加入请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

urls = ["https://www.qiushibaike.com/text/page/{}".format(str(i)) for i in range(1, 5)]  # 构造url


def re_scraper(url):
    '''
    :param url:
    :return:  正则爬取的时间
    '''
    res = requests.get(url,headers=headers)
    ids = re.findall("<h2>(.*?)</h2>", res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    for id, content, laugh, comment in zip(ids, contents, laughs, comments):
        info = {
            "id": id,
            "content": content,
            "laugh": laugh,
            "comment": comments[0]
        }
    return info


def bs_scraper(url):
    '''

    :param url: Beautifulsoup爬取时间
    :return:
    '''
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    ids = soup.select(" a > h2")
    contents = soup.select("div > span")
    laughs = soup.select("span.stats-vote > i")
    comments = soup.select("i.number")
    for id, content, laugh, comment in zip(ids, contents, laughs, comments):
        info = {
            'id': id.get_text(),
            'content': content.get_text(),
            'laugh': laugh.get_text(),
            'comment': comment.get_text()
        }
    return info


def lxml_scraper(url):
    '''
    :param url:
    :return:lxml爬虫爬取时间
    '''
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    try:
        for url_info in url_infos:
            id = url_info.xpath("div[1]/a[2]/h2/text()")[0]
            content = url_info.xpath("a[1]/div/span/text()")[0]
            laugh = url_info.xpath("div[2]/span[1]/i/text()")[0]
            comment = url_info.xpath("div[2]/span[2]/a/i/text()")[0]

        info = {
            "id": id,
            "content": content,
            "laugh": laugh,
            "comment": comment
        }
        return info
    except IndexError:
        pass  # 异常忽略掉


if __name__ == '__main__':
    for name, scraper in [("RE_exoressions", re_scraper), ("BeautifulSoup", bs_scraper), ("Lxml", lxml_scraper)]:
        start = time.time()
        for url in urls:
            scraper(url)
        end = time.time()
        print(name, end - start)
