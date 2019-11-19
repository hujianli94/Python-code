from baidu.items import BaiduItem
from scrapy.selector import Selector
from scrapy.spider import Spider


class Baispider(Spider):
    name = "Baidu_know"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://zhidao.baidu.com/list?cid=110",
        "https://zhidao.baidu.com/list?cid=110102"
    ]

    def parse(self, response):
        sel = Selector(response)
        items = []
        item = BaiduItem()
        title = sel.xpath('//div[@class="question-title"]/a/text()').extract()
        for i in title:
            items.append(i)
        item['TitleName'] = items
        # print(item['TitleName'])
        return item
