# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json


class ImagesSpider(scrapy.Spider):
    name = 'images'
    # allowed_domains = ['image.so.com']        ###必须注释掉，否则只能下载第一页图片
    urls = 'http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
    start_urls = [urls.format(0)]

    image_index = 0
    MAX_DOWNLOAD_NUM = 1000

    def parse(self, response):
        r = json.loads(response.body.decode("utf-8"))
        infos = r['list']
        yield {'image_urls': [info['qhimg_url'] for info in infos]}  # 给image_urls传递链接列表

        self.image_index += r['count']
        # 如count字段大于0，并且下载数量不足MAX_DOWNLOAD_NUM的图片信息
        if r['count'] > 0 and self.image_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.urls.format(self.image_index))  # callback默认传递给parse(self,response)。
