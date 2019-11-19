#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/21 13:05
# filename: 01.连接redis数据库.py

import redis

# 连接Redis，得到一个客户端对象
r = redis.StrictRedis(host='localhost', port=6379, db=0)

p1 = {
    'name': '李小龙',
    'age': 23,
    'sex': 'M',
}

p2 = {
    'name': '乔丹',
    'age': 23,
    'sex': 'M',
}

# 将数据保存到Redis中
r.hmset('person:1', p1)
r.hmset('person:2', p2)

# 关闭链接
r.connection_pool.disconnect()
