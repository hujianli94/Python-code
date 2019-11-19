#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 17:13
# filename: 05.集合操作.py

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')

# 向键为tags的集合中添加3个内容
redis.sadd('tags', 'Book', 'Tea', 'Coffee', 'hujianli', 'hujianli2', 'hujianli3', 'hujianli4')

# 从键为tag的集合中删除Book
redis.srem('tags', 'Book')

# 随机返回并删除一个元素
redis.spop('tags')

# 从键为tags的集合中删除元素Coffee并将其添加到键为tags的集合
redis.smove('tags', 'tags2', 'Coffee')

# 范围键为name的name:键名集合的元素个数
print(redis.scard('tags'))

# 测试hujianli2是否是键为tags的集合元素
print(redis.sismember('tags', 'hujianli2'))
