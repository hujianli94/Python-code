# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.selector import Selector
from scrapy.spider import Spider
import scrapy
class Baispider(Spider):
	name = "Post_spider"
	allowed_domains = []
	start_urls = [
		"http://127.0.0.1:5000/",
	]
	# 重写start_requests
	# scrapy.FormRequest是POST方式，formdata是POST参数，callback回调函数
	def start_requests(self):
		return [scrapy.FormRequest(
							self.start_urls[0],
							formdata={"Python": "爬虫开发"},
							callback=self.mypsot)]

	def mypsot(self, response):
		data = Selector(response).xpath('//p/text()').extract()[0]
		print(data)