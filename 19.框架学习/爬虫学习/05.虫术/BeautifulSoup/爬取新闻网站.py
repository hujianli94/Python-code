#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/8 12:45
# filename: 爬取新闻网站.py
from urllib import request
import json
from bs4 import BeautifulSoup

res = request.urlopen("http://www.chinanews.com/rss/rss_2.html")
rss_page = BeautifulSoup(res.read(), 'html.parser')
rss_links = set([item['href'] for item in rss_page.find_all('a')])


def crawl_feed(url):
    response = request.urlopen(url)
    rss = BeautifulSoup(response.read(), 'lxml')
    items = []
    print("Crawling {}".format(url))

    for item in rss.find_all('item'):
        try:
            info = {
                "title": item.title.text.strip(),
                "link": item.link.text,
                "description": item.description.text.strip(),
                'pub_data': u'' if item.pubDate is None else item.pubDate.text
            }
            items.append(info)
        except Exception as e:
            print("Crawling {} error.".format(url))
            print(e.mesage)

    return items


if __name__ == '__main__':
    feed_items = []
    for link in rss_links:
        feed_items += crawl_feed(link)

        # for i in feed_items:
        #     print(type(i))

    with open('result.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(feed_items, indent=4, ensure_ascii=False))

    print("Total crawl {} items".format(len(feed_items)))
