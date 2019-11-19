# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#导入pymongo
from pymongo import MongoClient
# 导入setting配置信息
from scrapy.conf import settings

class BaiduPipeline(object):
    def __init__(self):
		# 连接数据库
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
		# 入库处理
        self.collection.insert(dict(item))
        return item
