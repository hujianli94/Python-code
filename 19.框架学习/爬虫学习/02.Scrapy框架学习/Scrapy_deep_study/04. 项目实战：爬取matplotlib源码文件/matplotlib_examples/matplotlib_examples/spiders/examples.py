# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from matplotlib_examples.items import MatplotlibDownloadItem


class MatplotSpider(scrapy.Spider):
    name = 'matplot'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//li[@class="toctree-l2"]/a')
        detail_links = le.extract_links(response)
        for detail_link in detail_links:
            yield scrapy.Request(detail_link.url, callback=self.parse_url)

    def parse_url(self, response):
        item = MatplotlibDownloadItem()
        le2 = LinkExtractor(restrict_xpaths='//div[@class="section"]/p[1]/a')
        download_link = le2.extract_links(response)[0].url
        item['file_urls'] = [download_link]
        yield item


# # 导入CrawlerProcess类
# from scrapy.crawler import CrawlerProcess
#
# # 获取项目的设置信息
# from scrapy.utils.project import get_project_settings
#
# if __name__ == '__main__':
#     # 创建CrawlerProcess类对象，并将获取的设置信息传入
#     process = CrawlerProcess(get_project_settings())
#     # 设置需要启动的爬虫名称
#     process.crawl('matplot')
#     # 启动爬虫
#     process.start()