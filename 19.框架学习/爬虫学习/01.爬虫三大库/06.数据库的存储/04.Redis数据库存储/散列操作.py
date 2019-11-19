#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 17:26
# filename: 散列操作.py


from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')

# 向键为price的散列表中添加映射关系，cake的值为5
print(redis.hset('price', 'cake', 5))

# 向键为price的散列表中添加映射关系，book的值为6,如果不存在，则添加
print(redis.hsetnx('price', 'book', 6))

# 获取键为price的散列表中键名为cake的值
print(redis.hget('price', 'cake'))

# 获取键为price的散列表中cake和book的值
print(redis.hmget('price', ['cake', 'book']))

# 向键为price的散列表中批量添加映射
redis.hmset('price', {'banana': 2, 'pear': 6, 'apple': 11})

# key为price的散列表中apple的值增加3
redis.hincrby('price', 'apple', 3)

# 键为price的散列表中banana的值是否存在
print(redis.hexists('price', 'banana'))

# 从键为price的散列表中删除键名为banabna的映射
redis.hdel('price', 'banana')

# 从键为price的散列表中获取映射个数
print(redis.hlen('price'))

# 从键为price的散列表中获取所有映射键名
print(redis.hkeys('price'))

# 从键为price的散列表中获取所有映射键值
print(redis.hvals('price'))


# 从键为price的散列表中获取所有映射键值对
print(redis.hgetall('price'))