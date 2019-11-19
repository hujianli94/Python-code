#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/26 11:01
# filename: Jianshumongospider.py
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshumongodb.items import JianshumongodbItem

"""
翻页Ajax异步加载的页面信息：
https://www.jianshu.com/recommendations/users?page=1
https://www.jianshu.com/recommendations/users?page=2
https://www.jianshu.com/recommendations/users?page=3
"""


class Jianshumongodb(CrawlSpider):
    # 定义Spider的名字，在Scrapy爬虫运行时会用到：scrapy crawl jianshumongodb
    name = "jianshumongodb"

    start_urls = ["https://www.jianshu.com/recommendations/users?page=1"]

    def parse(self, response):
        base_url = "https://www.jianshu.com/u/"
        selector = Selector(response)
        infos = selector.xpath('//div[@class="col-xs-8"]')
        for info in infos:
            author_url = base_url + info.xpath('div/a/@href').extract()[0].strip('/users/')
            new_article = info.xpath('div/div[@class="recent-update"]')[0]
            new_article = new_article.xpath('string(.)').extract()[0].strip().replace(' ', '').replace('\n', '')

            yield Request(author_url, meta={'author_url': author_url, 'new_article': new_article},
                          callback=self.parse_item)
            # 通过meta进行爬虫信息参数的传递，并通过Request请求author_url,回调parse_item()函数。

        # 制作翻页功能
        urls = ['https://www.jianshu.com/recommendations/users?page={}'.format(i) for i in range(2, 30)]
        for url in urls:
            yield Request(url, callback=self.parse)  # 回调parse()函数

    def parse_item(self, response):  # 定义parse_item()爬取详细页面的信息
        item = JianshumongodbItem()
        item['author_url'] = response.meta['author_url']  # 取出传递的参数meta
        item['new_article'] = response.meta['new_article']

        try:
            selector = Selector(response)
            focus = selector.xpath('//div[@class="info"]/ul/li[1]/div/a/p/text()').extract()[0]
            fans = selector.xpath('//div[@class="info"]/ul/li[2]/div/a/p/text()').extract()[0]
            article_num = selector.xpath('//div[@class="info"]/ul/li[3]/div/a/p/text()').extract()[0]
            write_num = selector.xpath('//div[@class="info"]/ul/li[4]/div/p/text()').extract()[0]
            like_num = selector.xpath('//div[@class="info"]/ul/li[5]/div/p/text()').extract()[0]

            item['focus'] = focus
            item['fans'] = fans
            item['article_num'] = article_num
            item['write_num'] = write_num
            item['like_num'] = like_num
            yield item

        except IndexError:
            pass




# /html/body/div[1]/div/div[1]/div[1]/div[2]/
# /html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[2]/div/a/p
# /html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[3]/div/a/p
# 字数： /html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[4]/div/p
# like数：/html/body/div[1]/div/div[1]/div[1]/div[2]/ul/li[5]/div/p
