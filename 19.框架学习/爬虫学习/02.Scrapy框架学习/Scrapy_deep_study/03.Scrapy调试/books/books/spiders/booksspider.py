# -*- coding: utf-8 -*-
import scrapy
from books.items import BooksItem
from scrapy.linkextractors import LinkExtractor


class BooksspiderSpider(scrapy.Spider):
    name = 'booksspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        ##提取每本书的链接
        le = LinkExtractor(restrict_xpaths='//article[@class="product_pod"]')  ##具体位置在//article/div/a的标签中
        detail_urls = le.extract_links(response)
        for detail_url in detail_urls:
            yield scrapy.Request(detail_url.url, callback=self.parse_book)  ##记得使用.url提取出extract_links里面的链接。

        ##提取下一页的链接
        le2 = LinkExtractor(restrict_xpaths='//li[@class="next"]')
        next_url = le2.extract_links(response)[0].url
        yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):
        ##提取每本书的具体信息
        item = BooksItem()
        info = response.xpath('//article[@class="product_page"]')
        item['name'] = info.xpath('div[1]/div[2]/h1/text()').extract()[0]
        item['price'] = info.xpath('div[1]/div[2]/p[1]/text()').extract()[0]
        item['review_rating'] = info.xpath('div[1]/div[2]/p[3]/@class').re('star-rating (\w+)')[0]

        info2 = response.xpath('//table[@class="table table-striped"]')
        item['upc'] = info2.re('<td>.*?</td>')[0].strip('<td>').strip('</td>')
        item['stock'] = info2.re_first('((\d+) available)').split()[0]
        # item['stock'] = info2.xpath('//tr[last()-1]/td/text()').re_first('\d+')  #使用last()获取标签的最后一个数字
        item['review_num'] = info2.re('<td>.*?</td>')[-1].strip('<td>').strip('</td>')
        # item['review_num'] = info2.xpath('//tr[last()]/td/text()').extract_first()
        yield item
