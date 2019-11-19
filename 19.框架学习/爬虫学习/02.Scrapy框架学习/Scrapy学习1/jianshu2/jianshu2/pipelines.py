# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class Jianshu2Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        mydb = client['mydb']
        zhuanti = mydb['jianshu']
        self.post = zhuanti  ##连接数据库


    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)  ##插入数据库
        return item
