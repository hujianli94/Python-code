# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy_download.items import ScrapyDownloadItem
from scrapy.spider import Spider
# 导入setting.py配置信息
from scrapy.conf import settings
class downspider(Spider):
    name = "downspider"
    allowed_domains = []
    start_urls = [
       'http://124.232.176.137/mp3.9ku.com/m4a/655825.m4a'
       ]

    def parse(self, response):
        # 下载方法一
        f = open(settings['FILES_STORE']+'MySong.m4a', 'wb')
        f.write(response.body)
        f.close()
        # 下载方法二
        item = ScrapyDownloadItem()
        item['FileName'] = ['PythonBook.zip', 'Python.jpg', 'MyMusic.m4a']
        item['FileUrl'] = ['http://d.1.didiwl.com/PYTHON_zryycl.zip',
                           'https://www.python.org/static/img/python-logo.png',
                           'http://124.232.176.137/mp3.9ku.com/m4a/655825.m4a']
        return item