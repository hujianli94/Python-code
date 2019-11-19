# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline(object):
    review_rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def process_item(self, item, spider):
        # rating = item.get('review_rating')  #获取review_rating的数据
        rating = item['review_rating']  # 与上面的语句等价
        item['review_rating'] = self.review_rating_map[rating]

        return item


##简单设置方式,在setting.py中开通pipeline即可。
import pymongo


class PymongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['scrapydb']
        books = db['books']
        self.post = books  ##连接数据库

    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)  ##插入数据库
        return item

    def close_spider(self, spider):
        self.client.close()
