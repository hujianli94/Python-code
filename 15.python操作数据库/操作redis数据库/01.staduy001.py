#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/29 17:06
# filename: 01.staduy001.py
import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

p1 = {
    "name": "胡建力",
    "age": 18,
    "sex": "Man",
}

p2 = {
    "name": "科比",
    "age": 30,
    "sex": "Man",
}

# 将数据保存到Redis中
r.hmset("person:1", p1)
r.hmset("person:2", p2)

# 关闭链接
r.connection_pool.disconnect()
