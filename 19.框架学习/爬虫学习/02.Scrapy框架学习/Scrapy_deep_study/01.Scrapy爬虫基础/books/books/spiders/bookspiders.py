#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/1 9:27//article/h3/a/text()
# filename: bookspiders.py
import scrapy
from books.items import BooksItem
from scrapy.http import Request


class Books(scrapy.Spider):
    name = 'books'  # 建立唯一爬虫名，调用CMD命令时会用到
    start_urls = ['http://books.toscrape.com/']  # 爬取开始地址

    def parse(self, response):  # 默认解析函数
        infos = response.xpath('//article')  # 直接使用response.xpath来解析信息
        for info in infos:
            title = info.xpath("h3/a/@title").extract()  # 最终提取信息时，加上.extract()
            price = info.xpath('div/p[@class="price_color"]/text()').extract()

            yield {'title': title, 'price': price}  # 生成器返回数据信息

        next_url = response.xpath('//li[@class="next"]/a/@href').extract()[0]
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)


