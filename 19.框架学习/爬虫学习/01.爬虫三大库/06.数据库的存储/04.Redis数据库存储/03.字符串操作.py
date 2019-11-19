#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 13:22
# filename: 03.字符串操作.py

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')

# 给数据库中的键赋予值value
redis.set('name20', 'huxioajian01')
redis.set('name21', 'huxioajian02')
redis.set('age', 18)

# 返回数据库中键对应的值
print(redis.get('name20'))

# 返回多个键对应的值 value
print(redis.mget(['name20', 'name21']))

# 如果不存在这个键值对，则更新，否则不变
redis.setnx('name22', 'huxiaojian22')
redis.setnx('name22', 'huxiaojian23')

# 设置键对应值的有效期。
redis.setex('name23', 5, 'passable')

# 设置指定键的value值的子字符串
redis.set('name24', 'hello')
redis.setrange('name24', 6, 'World')
print(redis.get('name24'))

# 批量赋值
redis.mset({'name25': 'hu001', 'name26': 'hu002'})

# 键均不存在时才批量赋值
redis.msetnx({'name27': 'hu001', 'name28': 'hu002'})

# 键为name的value增值操作。默认为1，若不存在则创建
redis.incr('age', 1)

# 键为name的value减值操作。默认为1，若不存在则创建
redis.decr('age', 1)

# 键为name的string的值附加value
redis.append('name24', 'OK')
print(redis.get('name24'))

# 范围键的string的子串,截取索引1~5
print(redis.substr('name24', 1, 5))

# 获取键的value值从start到end的子字符串，截取索引1~6
print(redis.getrange('name24', 1, 6))


