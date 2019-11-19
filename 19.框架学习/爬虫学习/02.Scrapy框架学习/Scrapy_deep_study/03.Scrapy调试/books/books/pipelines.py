# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline(object):
    review_rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def process_item(self, item, spider):
        # rating = item.get('review_rating')  #获取review_rating的数据
        rating = item['review_rating']  # 与上面的语句等价
        item['review_rating'] = self.review_rating_map[rating]

        return item
