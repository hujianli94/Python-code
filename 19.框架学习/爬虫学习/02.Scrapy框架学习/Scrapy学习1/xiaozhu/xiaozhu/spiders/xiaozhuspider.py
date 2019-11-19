#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/25 20:40
# filename: xiaozhuspider.py
from scrapy.spiders import CrawlSpider  # CrawlSpider作为xiaozhu的父类
from scrapy.selector import Selector  # Selector用于解析请求网页后返回的数据，与Lxml库的用法一样
from xiaozhu.items import XiaozhuItem  # XiaozhuItem是items.py中定义爬虫字段的类


class xiaozhu(CrawlSpider):
    name = "xiaozhu"  # 定义Spider的名字，在Scrapy爬虫运行时会用到：scrapy crawl xiaozhu
    start_urls = ['http://gz.xiaozhu.com/fangzi/112646821103.html']  # 默认情况下，spider会以start_urls中的链接为入口开始爬取

    def parse(self, response):  # response是请求网页返回的数据
        item = XiaozhuItem()  # 初始化item
        html = Selector(response)  # 导入Selector用于解析数据
        title = html.xpath('//div[@class="pho_info"]/h4/em/text()').extract()[0]  # 唯一不同，需要加上.extract()来提取信息
        address = html.xpath('//div[@class="pho_info"]/p/span/text()').extract()[0].strip()
        price = html.xpath('//div[@class="day_l"]/span/text()').extract()[0]
        lease_type = html.xpath('//li[@class="border_none"]/h6/text()').extract()[0]
        suggestion = html.xpath('//h6[@class="h_ico2"]/text()').extract()[0]
        bed = html.xpath('//h6[@class="h_ico3"]/text()').extract()[0]

        item['title'] = title
        item['address'] = address
        item['price'] = price
        item['lease_type'] = lease_type
        item['suggestion'] = suggestion
        item['bed'] = bed

        yield item
