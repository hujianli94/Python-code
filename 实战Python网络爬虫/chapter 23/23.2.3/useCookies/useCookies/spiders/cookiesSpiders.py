import scrapy
from scrapy.spider import Request
class cookiesSpider(scrapy.Spider):
    name = "cookies"
    allowed_domains = ["httpbin.ort/get"]
    start_urls = ['http://httpbin.org/get']
    def start_requests(self):
        yield Request(url=self.start_urls[0], callback=self.parse)
    def parse(self, response):
        print(response.text)