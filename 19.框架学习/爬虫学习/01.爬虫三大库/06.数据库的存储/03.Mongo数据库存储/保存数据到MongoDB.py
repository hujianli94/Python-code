#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/9 16:56
# filename: 保存数据到MongoDB.py
import pymongo

Mongo_Url = "localhost"
Mongo_DB = 'taobao'
Mongo_Collection = 'products'
client = pymongo.MongoClient(Mongo_Url)
db = client[Mongo_DB]


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    :return:
    """
    try:
        if db[Mongo_Collection].insert(result):
            print("存储到MongoDB成功")
    except Exception:
        print("存储到MongoDB失败")
