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
        info = response.xpath('//div[contains(@class,"product_main")]')
        item['name'] = info.xpath('h1/text()').extract()[0]
        item['price'] = info.xpath('p/text()').extract()[0]
        item['review_rating'] = info.xpath('p[3]/@class').re('star-rating (\w+)')[0]

        info2 = response.xpath('//table[contains(@class,"table")]')
        item['upc'] = info2.xpath('//tr[1]/td/text()').extract_first()
        item['stock'] = info2.xpath('//tr[6]/td/text()').re_first('\d+')
        item['review_num'] = info2.xpath('//tr[7]/td/text()').extract_first()
        yield item
