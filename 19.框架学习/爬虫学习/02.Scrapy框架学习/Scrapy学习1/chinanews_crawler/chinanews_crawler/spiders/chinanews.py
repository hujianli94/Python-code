# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from scrapy.http import Request
from chinanews_crawler.items import ChinanewsCrawlerItem


class ChinanewsSpider(Spider):
    name = 'chinanews'  # 项目名称
    allowed_domains = ['chanews.com']  # 只爬取该域内的内容，自动过滤链接到其他域的内容
    start_urls = ('http://www.chinanews.com/rss/rss_2.html',)  # 蜘蛛被启动并产生第一批请求时的URL数组

    def parse(self, response):
        rss_page = BeautifulSoup(response.body, 'html.parser')
        rss_links = set([item['href'] for item in rss_page.find_all('a')])

        for link in rss_links:
            yield Request(url=link, callback=self.parse_feed, dont_filter=True)

    def parse_feed(self, response):
        rss = BeautifulSoup(response.body, 'lxml')

        for item in rss.find_all('item'):
            feed_item = ChinanewsCrawlerItem()
            feed_item['title'] = item.title.text,
            feed_item['link'] = item.link.text,
            feed_item['desc'] = item.description.text,
            feed_item['pub_date'] = item.pubdate.text

            yield feed_item


# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess

# 获取项目的设置信息
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    # 创建CrawlerProcess类对象，并将获取的设置信息传入
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('chinanews')
    # 启动爬虫
    process.start()
