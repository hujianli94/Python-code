#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/1 10:05
# filename: spider开发流程.py
"""
最简单的Spider只需4个步骤：
1).继承scrapy.Spider；
2).为Spider取名；
3).设置爬取的起始点；
4).实现页面解析函数。

其中，Spider是一个基类，后面我们使用到的所有其他爬虫都需要继承这个Spider基类，
例如：CrawlSpider，XMLFeedSpider，CSVFeedSpider，SitemapSpider等，这些类全部位于scrapy\spiders目录之下。




实际上设置完爬取起始点后，默认由start_reqeusts()方法构建Request对象，
然后默认指定由parse方法作为页面解析函数。如果我们希望为Request添加特定的请求头部或想为Request指定特定的页面解析函数，
可以考虑在构建的Spider类中实现start_requests方法，即可覆盖基类Spider的start_requests方法。例如，在第一章的基础上进行修改：


"""

""" 
import scrapy

class Books(scrapy.Spider):
    name = 'books'
    #start_urls = ['http://books.toscrape.com/']

    #实现start_requests方法，替代start_urls这个类属性
    def start_requests(self):
        yield scrapy.Request(url="http://books.toscrape.com/",
                             callback=self.parse_book,    #此时改用parse_book作为回调函数
                             headers={'User-Agent':'Mozilla/5.0'},
                             dont_filter=True)

    def parse_book(self,response):
        infos = response.xpath('//article')
        for info in infos:
            title = info.xpath("h3/a/@title").extract()[0]
            price = info.xpath('div/p[@class="price_color"]/text()').extract()[0]

            yield {'title': title, 'price': price}   
"""

"""
所以，设置爬取的起爬点有两种方法：

定义start_urls属性
改写start_requests方法

而第四个步骤，页面解析函数需要完成以下两个工作：
1).提取数据，将数据封装后（Item或字典）提交给Scrapy引擎；
2).提取链接，并用链接构造新的Request对象提交给Scrapy引擎；其中，提取链接的方法包括使用选择器或使用LinkExtractor。

"""