# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
import scrapy
# 导入setting.py配置信息
from scrapy.conf import settings

class ScrapyDownloadPipeline(object):
    def process_item(self, item, spider):
        # 入库处理等操作
        return item

# 下载功能
class DownloadFlie(FilesPipeline):
    # 重写get_media_requests
    def get_media_requests(self, item, info):
        for index, url in enumerate(item['FileUrl']):
            yield scrapy.Request(url, meta={'name': item['FileName'][index]})

    # 重写file_path，命名文件名
    def file_path(self, request, response=None, info=None):
        file_name = settings['FILES_STORE'] + (request.meta['name'])
        return file_name