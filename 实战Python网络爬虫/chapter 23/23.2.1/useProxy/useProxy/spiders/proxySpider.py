import scrapy
class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["httpbin.ort/get"]
    start_urls = ['http://httpbin.org/get']
    def parse(self, response):
        print(response.text)
