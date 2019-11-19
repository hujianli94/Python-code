from scrapy import Spider
from scrapy_splash import SplashRequest
from dongman.items import DongmanItem
from scrapy.selector import Selector

class SplashSpider(Spider):
    name = 'finish_opera'
    start_urls = 'https://www.bilibili.com/v/anime/finish/#/all/default/0/%s/'

    # 将Scrapy的request改为SplashRequest
    def start_requests(self):
        for page in range(2):
            url = self.start_urls %(str(page+1))
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }
            # 设置请求信息
            args = {
                'wait': '3',
                "headers": headers,
                # 设置Cookies
                # "cookies": {'hello': 'Python'}
                # 设置代理IP
                # "proxy": "http://101.200.153.236:8123",
            }
            yield SplashRequest(url, self.parse, args=args)

    def parse(self, response):
        # 将响应内容生成Selector，用于数据清洗
        sel = Selector(response)
        # 定义DongmanItem对象
        item = DongmanItem()
        info_list = sel.xpath('//div[@class="vd-list-cnt"]/ul/li')
        for i in info_list:
            item['name'] = ''.join(i.xpath('.//div/div[2]/a/text()').extract()).strip()
            item['desc'] = ''.join(i.xpath('.//div/div[2]/div[1]/text()').extract()).strip()
            item['viewNumber'] = ''.join(i.xpath('.//div/div[2]/div[2]/span[1]/span/text()').extract()).strip()
            item['captionsNum'] = ''.join(i.xpath('.//div/div[2]/div[2]/span[2]/span/text()').extract()).strip()
            yield item