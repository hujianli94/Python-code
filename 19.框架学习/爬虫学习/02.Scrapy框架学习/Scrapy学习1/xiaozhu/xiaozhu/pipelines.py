# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class XiaozhuPipeline(object):
    def __init__(self):
        self.file = codecs.open('mydata1.json', 'wb', encoding='utf-8')

    # def process_item(self, item, spider):
    #     f = open("xiaozhu.txt", "a+",encoding="utf-8")
    #     f.write(item['title'] + "\n")
    #     f.write(item['address'] + "\n")
    #     f.write(item['price'] + "\n")
    #     f.write(item['lease_type'] + "\n")
    #     f.write(item['suggestion'] + "\n")
    #     f.write(item['bed'] + "\n")
    #     return item

    def process_item(self, item, spider):
        # 通过json模块下的dumps()处理
        i = json.dumps(dict(item), ensure_ascii=False, indent=4)
        line = i + '\n'
        print(line)
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
