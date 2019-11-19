# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class ChinanewsCrawlerPipeline(object):
    # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        # 创建了一个文件
        self.filename = open("chinanewsCrawler.json", "w", encoding="utf-8")

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False, indent=4) + "\n"
        self.filename.write(jsontext)
        return item

    # close_spider方法是可选的，结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()
