# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.selector import Selector
from scrapy.spider import Spider
import scrapy


class Baispider(Spider):
    name = "Get_Post_spider"
    allowed_domains = []
    start_urls = [
        "http://127.0.0.1:5000/",
    ]
    # 定义请求头和cookies，两者皆以字典形式表示
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               }
    cookies = {}

    # 第一次请求GET，return是第二次POST请求
    def parse(self, response):
        data = Selector(response).xpath('//p/text()').extract()[0]
        print(data)
        return [scrapy.FormRequest(
            self.start_urls[0],
            cookies=self.cookies,
            headers=self.headers,
            formdata={"Python": "爬虫开发"},
            callback=self.mypsot)]

    # 第二次POST请求，return是第三次GET请求
    def mypsot(self, response):
        data = Selector(response).xpath('//p/text()').extract()[0]
        print(data)
        return scrapy.Request(self.start_urls[0], cookies=self.cookies,
                              headers=self.headers, callback=self.myget)

    # 第三次GET请求
    def myget(self, response):
        data = Selector(response).xpath('//p/text()').extract()[0]
        print(data)
