import scrapy
from scrapy.spider import Request
class HeaderSpider(scrapy.Spider):
    name = "headers"
    allowed_domains = ["httpbin.ort/get"]
    start_urls = ['http://httpbin.org/get']
    def start_requests(self):
        headers = {'Referer': 'https://www.baidu.com/',
                   'Upgrade-Insecure-Requests': '1',
                   'Accept-Language': 'zh-CN,zh;q=0.9'}
        yield Request(url=self.start_urls[0], meta={'requsetHeader': headers}, callback=self.parse)
    def parse(self, response):
        print(response.text)