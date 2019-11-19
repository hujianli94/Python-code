from maoyan.items import MaoyanItem
from scrapy.selector import Selector
from scrapy.spider import Spider, Request
class MovieSpider(Spider):
    # 属性name必须设置，而且是唯一命名，用于运行爬虫
    name = "Movie"
    # 设置允许访问域名
    allowed_domains = ["maoyan.com"]
    # 设置URL
    start_urls = 'http://maoyan.com/board/4?offset=%s'
    # 重写start_requests
    def start_requests(self):
        # TOP100的电影共10页，则循环10次
        for page in range(10):
            url = self.start_urls %(str(page * 10))
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        # 将响应内容生成Selector，用于数据清洗
        sel = Selector(response)
        # 定义DoubanItem对象
        item = MaoyanItem()
        infoList = sel.xpath('//dl[@class="board-wrapper"]//dd')
        for c in infoList:
            item['movieName'] = ''.join(c.xpath('.//p[@class="name"]//text()').extract()).strip()
            item['performer'] = ''.join(c.xpath('.//p[@class="star"]//text()').extract()).strip()
            item['releasetime'] = ''.join(c.xpath('.//p[@class="releasetime"]//text()').extract()).strip()
            item['score'] = ''.join(c.xpath('.//p[@class="score"]//text()').extract()).strip()
            yield item