#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 13:22
# filename: 02.键值操作.py
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')



############################### 键操作 #######################################

# 设置键和值，获取键对应的值
redis.set('name1', 'hujianli0001')
redis.set('name2', 'hujianli0002')
redis.set('name3', 'hujianli0003')
print(redis.get('name'))


# 判断一个键是否存在
print(redis.exists('name1'))
print(redis.exists('name2'))

# 删除一个键
print(redis.delete('name'))

# 判断键类型
print(redis.type('name1'))

# 获取所有符合规则的键
print(redis.keys('n*'))

# 获取随机一个键
print(redis.randomkey())

# 重命名键
redis.rename('name1', 'name10')
print(redis.get('name10'))

# 获取当前数据库中键的数目
print(redis.dbsize())

# 设定键的过期时间，单位是秒。-1表示永不过期
print(redis.expire('name10', 4))

# 获取键的过期时间,单位是秒。-1表示永不过期
print(redis.ttl('name10'))

# 将键移动到其他数据库
print(redis.move('name3',2))

# # 删除当前选择数据库中的所有键
# redis.flushdb()
#
# # 删除首页数据库中的所有键
# redis.flushall()