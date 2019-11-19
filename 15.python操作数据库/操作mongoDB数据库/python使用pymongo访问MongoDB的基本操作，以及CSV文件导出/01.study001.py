#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 16:08
# filename: 01.01.导入excel文件.py
import pymongo

# mongodb服务器地址和端口
mongo_url = "127.0.0.1:27017"

client = pymongo.MongoClient(mongo_url)

# 连接到数据库
DATABASE = "mydb"
db = client[DATABASE]

# 连接到集合
Coll = "taobao_renaiping"
db_coll = db[Coll]

# 根据城市是广东、广州的记录，然后进行价格排序，从高到低
city = {"城市": "广东 广州"}
search_res = db_coll.find(city).sort("价格", -1)
for record in search_res:
    # print(record)
    print(record['_id'], record['商店名称'], record['商品'], record['购买人数'], record['价格'])
