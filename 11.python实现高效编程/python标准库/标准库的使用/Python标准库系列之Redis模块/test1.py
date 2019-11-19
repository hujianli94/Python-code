#!/usr/bin/env python
#-*- coding:utf8 -*-
import redis
#入门及使用
'''
import redis
conn = redis.Redis(host="127.0.0.1", port=6379)
#写入两条数据
conn.set('name', 'hujianli')
conn.set('url', 'www.baidu.com')

#获取一条数据
print(conn.get('name'))
print(conn.get('url'))
'''


'''
##使用连接池连接到Redis
pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
conn = redis.Redis(connection_pool=pool)
print(conn.set('hello', 'world'))
print(conn.get('hello'))

'''

##API
'''
redis-py提供的API用来操作redis

String API
set(name, value, ex=None, px=None, nx=False, xx=False)

参数	描述
ex	过期时间（秒）
px	过期时间（毫秒）
nx	如果设置为True，则只有name不存在时，当前set操作才执行
xx	如果设置为True，则只有name存在时，岗前set操作才执行
'''




