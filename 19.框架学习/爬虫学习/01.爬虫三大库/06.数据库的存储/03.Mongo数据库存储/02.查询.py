#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 22:44
# filename: 02.查询.py
from pymongo import MongoClient

# 连接方式1
client = MongoClient(host='localhost', port=27107)

# 1条命令连接MongoDB数据库和集合
stus = MongoClient().test1.stu2  # 一条语句实现连接到集合

# 查询一条数据
result = stus.find_one({'name': 'hujianli722'})
print(type(result))
print(result)
# 如果查询结果不存在，则会返回None


# 查询多条数据
result1 = stus.find({'age': 20})
print(result1)

for res in result1:
    print(res)

# 条件查询
result2 = stus.find({'age': {'$gt': 20}})
for res in result2:
    print(res)

"""
                    比较符号        
符号            含义                示例
$lt             小于              {'age':{'$lt:20'}}
$gt             大于              {'age':{'$gt':20}}
$lte            小于等于          {'age':{'$let':20}}
$gte            大于等于          {'age':{'$get':20}}
$ne             不等于            {'age':{'$ne':20}}
$in             在范围内          {'age':{'$in':[20,23]}}
$nin            不在范围内        {'age':{'$nin':[20,23]}}

                    正则匹配
符号            含义                        示例                       示例含义                                                    
$regex          匹配正则表达式    {'name':{'$regex':'^M.*'}}           name以M开头
$exists         属性是否存在      {'name':{'$exists':True}}            name属性存在
$type           类型判断          {'age':{'$type':'int'}}              age的类型为int
$mod            数字模操作        {'age':{'$mod':[5,0]}}               年龄模5余0
$text           文本查询          {'text':{'$search':'Mike'}}          text类型的属性中包含Mike字符串

$where          高级条件查询      {'$where':'obj.fans_count == obj.follows_count'}    自身粉丝数等于关注数
"""

