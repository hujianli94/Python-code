#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 22:27
# filename: 01.连接MongoDB.py
from pymongo import MongoClient

# 连接方式1
client = MongoClient(host='localhost', port=27107)

# # 连接方式2
# client = MongoClient('mongodb://localhost:27107/')


# ##指定数据库
# db = client.test1
#
# ##或者
# db = client['test1']

# ## 指定集合
# collection = db.stu2
# ## 或者
# collection = db['stu2']



# 1条命令连接MongoDB数据库和集合
stus = MongoClient().test1.stu2  # 一条语句实现连接到集合