# 导入items.py的BaiduItem，存放爬取数据
from baidu.items import BaiduItem
# Scrapy自带数据清洗模块
from scrapy.selector import Selector
# 导入CrawlSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
# 爬虫规则，一个爬虫以类为单位
class Baispider(CrawlSpider):
	# 属性name必须设置，而且是唯一命名，用于运行爬虫
    name = "Baidu"
	# 设置允许访问域名
    allowed_domains = ["baidu.com"]
	# 设置URL
    start_urls = [
        "https://zhidao.baidu.com/list?cid=110"
        ]
	# 编写爬取规则
    rules = (
        Rule(LinkExtractor(allow=('zhidao.baidu.com/question/', ), deny=(),), callback='parse_item'),
    )
	# 编写处理函数
    def parse_item(self, response):
        sel = Selector(response)
        items = []
        item = BaiduItem()
        title = sel.xpath('//span[@class="ask-title "]/text()').extract()
        for i in title:
            items.append(i)
        item['TitleName'] = items
        return item
