#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/26 9:53
# filename: Jianshu2spider.py

#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/25 21:08
# filename: Jianshuspider.py
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu2.items import Jianshu2Item


class Jianshu(CrawlSpider):
    name = "Jianshu2"         # 定义Spider的名字，在Scrapy爬虫运行时会用到：scrapy crawl xiaozhu
    start_urls = ["https://www.jianshu.com/recommendations/collections?page=1&order_by=hot"]

    def parse(self, response):
        item = Jianshu2Item()
        selector = Selector(response)
        infos = selector.xpath('//div[@class="collection-wrap"]')
        for info in infos:
            try:
                name = info.xpath('a/h4/text()').extract()[0]
                content = info.xpath('a/p/text()').extract()[0].replace('\n', '')
                article = info.xpath('div[@class="count"]/a/text()').extract()[0]
                fans = info.xpath('div[@class="count"]/text()').extract()[0].strip('· ')

                item["name"] = name
                item["content"] = content
                item["article"] = article
                item["fans"] = fans
                yield item

            except IndexError:
                pass

        # 构造第2页到第37页的‘热门专题’URL，通过Request请求URL，并回调parse()函数
        urls = ['https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.format(str(i)) for i in
                range(2, 37)]
        for url in urls:
            yield Request(url, callback=self.parse)
