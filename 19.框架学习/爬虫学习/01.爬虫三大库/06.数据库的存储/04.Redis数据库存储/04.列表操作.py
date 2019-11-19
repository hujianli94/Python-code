#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 16:27
# filename: 04.列表操作.py
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')

# 在键为list的列表末尾添加值为value的元素
redis.rpush('list', 1, 2, 3, 4, 5, 6, 7)

# 在键为list的列表头添加职位value的元素
redis.lpush('list', 0)

# 返回键为name的列表的长度
print(redis.llen('list'))

# 截取键为name的列表保留索引为start到end的内容
print(redis.lrange('list', 1, 3))

# 截取键为name的列表，保留索引为start到end的内容
print(redis.ltrim('list', 1, 3))

# 返回键为name的列表中index位置的元素
print(redis.lindex('list', '1'))

# 给键为name的列表中index位置的元素赋值
print(redis.lset('list', 1, 4))
#
# 删除count个键的列表,将键为list的列表删除两个3
redis.lrem('list', 2, 1)

# 返回并删除键为name的name：键名列表中的首元素
print(redis.lpop('list'))

# 返回并删除键为name的name：键名列表中的尾元素
print(redis.rpop('list'))

# 返回并删除名称在keys中的list中的首个元素，如果列表为空，则会一直阻塞等待
print(redis.blpop('list'))

# 返回并删除名称为src的列表，并将该元素添加到名称为dst列表头部
redis.rpoplpush('list', 'list2')
