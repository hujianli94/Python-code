# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class Jianshu3Pipeline(object):
    def __init__(self):
        conn = pymysql.connect(host='localhost', user='root', passwd="admin#123",
                               db='jianshu', port=3306, charset='utf8')
        cursor = conn.cursor()
        self.post = cursor  # 连接数据库

    def process_item(self, item, spider):
        cursor = self.post
        cursor.execute("use jianshu")  # 选择数据表
        sql = "INSERT INTO jianshu(name, content, article, fans) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (item["name"], item["content"], item["article"], item["fans"]))
        cursor.connection.commit()  # 提交事务，将数据插入数据库
        return item
