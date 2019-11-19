# 导入items.py的BaiduItem，存放爬取数据
from baidu.items import BaiduItem
# Scrapy自带数据清洗模块
from scrapy.selector import Selector
# Scrapy搜索引擎
from scrapy.spider import Spider
# 爬虫规则，一个爬虫以类为实现对象

class Baispider(Spider):
    # 属性name必须设置，而且是唯一命名，用于运行爬虫
    name = "Baidu_know"
    # 设置允许访问域名
    allowed_domains = ["baidu.com"]
    # 设置URL
    start_urls = [
        "https://zhidao.baidu.com/list?cid=110",
        "https://zhidao.baidu.com/list?cid=110102"
    ]
    # 函数parse处理响应内容，函数名不能更改。
    def parse(self, response):
        # 将响应内容生成Selector，用于数据清洗
        sel = Selector(response)
        items = []
        # 定义BaiduItem对象
        item = BaiduItem()
        title = sel.xpath('//div[@class="question-title"]/a/text()').extract()
        for i in title:
            items.append(i)
        item['TitleName'] = items
        return item
