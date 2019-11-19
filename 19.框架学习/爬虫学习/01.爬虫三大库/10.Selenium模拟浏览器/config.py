#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/2 10:20
# filename: config.py

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'

# 使用Phantomjs API
SERVICE_ARGS = []

MAX_PAGE = 100

# 移植性
SERVICE_ARGS.append('--load-images=no')  #关闭图片加载
SERVICE_ARGS.append('--disk-cache=yes')  #开启缓存
SERVICE_ARGS.append('--ignore-ssl-errors=true') #忽略https错误

# 可替换成其他关键词
KEYWORD = '手表'