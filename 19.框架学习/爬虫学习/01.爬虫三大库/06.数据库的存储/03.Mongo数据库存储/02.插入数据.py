#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 22:32
# filename: 02.插入数据.py
from pymongo import MongoClient

# 连接方式1
client = MongoClient(host='localhost', port=27107)

# 1条命令连接MongoDB数据库和集合
stus = MongoClient().test1.stu2  # 一条语句实现连接到集合

student = {
    'id': 20190820,
    'name': 'hujianli',
    'age': 20,
    'gender': 'male'
}

# 插入一条数据
result = stus.insert_one(student)
print(result)
print(result.inserted_id)





student1 = {
    'id': 20190822,
    'name': 'hujianli722',
    'age': 21,
    'gender': 'male'
}

student2 = {
    'id': 20190823,
    'name': 'hujianli723',
    'age': 22,
    'gender': 'male'
}
# 插入多条数据
result = stus.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
