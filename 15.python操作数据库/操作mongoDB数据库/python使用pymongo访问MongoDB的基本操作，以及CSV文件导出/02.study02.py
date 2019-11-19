#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 16:23
# filename: 02.study02.py
from pymongo import MongoClient

stus = MongoClient().mydb.taobao_renaiping  # 一条语句实现连接到集合

# for stu in stus.find():
#     print(stu)

queryArgs = {}
projectionFields = {'_id': False, '城市': False}  # 用字典指定
searchRes = stus.find(queryArgs, projection=projectionFields)
for info in searchRes:
    print(info)
