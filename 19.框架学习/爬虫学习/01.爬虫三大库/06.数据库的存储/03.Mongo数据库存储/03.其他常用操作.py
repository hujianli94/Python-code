#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 23:03
# filename: 03.其他常用操作.py
import pymongo
from pymongo import MongoClient

# 连接方式1
client = MongoClient(host='localhost', port=27107)

# 1条命令连接MongoDB数据库和集合
stus = MongoClient().test1.stu2  # 一条语句实现连接到集合

# 统计所有数据
count_all = stus.find().count()
print(count_all)

# 统计符合条件的数据
count = stus.find({'age': 20}).count()
print(count)

# 排序
## 调用sort()方法，传入排序字段和升序标志
result1 = stus.find().sort('age', pymongo.ASCENDING)
print([result['age'] for result in result1])

result2 = stus.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in result2])

## 偏移,偏移2.就忽略前2个元素
result2 = stus.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in result2])

# 使用limit()方法指定要取的结果个数
result3 = stus.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in result3])

'''
## 更新
cond = {'name': 'hujianli723'}
student = stus.find_one(cond)
student['age'] = 25
result = stus.update(cond, student)
print(result)

# 使用 $set操作符对数据进行更新
cond = {'name': 'hujianli722'}
student = stus.find_one(cond)
student['age'] = 18
result = stus.update(cond, {'$set': student})
'''

cond = {'name': 'hujianli'}
student = stus.find_one(cond)
student['age'] = 17
result = stus.update_one(cond, {'$set': student})
print(result)
# 打印匹配条数和影响的条数
print(result.matched_count, result.modified_count)

## 调用update_many()方法，则会将所有符合条件的数据都更新
cond = {'age': {'$gt': 20}}
result = stus.update_many(cond, {'$inc': {'age': 1}})
print(result)
# 打印匹配条数和影响的条数
print(result.matched_count, result.modified_count)

'''
## 删除,直接调用remove()方法指定删除的条件即可
result = stus.remove({'name': 'hujianli722'})
print(result)
'''

## delete_one()和delete_mant()两个推荐的方法
# delete_one()删除第一台符合条件的数据
result = stus.delete_one({'name': 'hujianli'})
print(result)
print(result.deleted_count)

# delete_mant()删除所有符合条件的数据。deleted_count属性获取删除的数据条数
result1 = stus.delete_many({'age': {'$lt': 23}})
print(result.deleted_count)


## 其他方法
"""
# 查找后删除
find_one_and_delete()

# 查找后替换
find_one_and_replace()

# 查找后更新
find_one_and_update()


关于PyMongo 的详细用法， 可以参见官方文档： 
http://api.mongodb.com/python/current/api/pymongo/collection.html

另外， 还有对数据库和集合本身等的一些操作， 这里不再一一讲解， 可以参见官方文档：
http://api.mongodb.com/python/current/api/pymongo

"""