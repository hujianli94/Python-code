#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
python操作SQLite数据库
'''

#导入模块
import sqlite3

#创建连接对象
conn = sqlite3.connect('mrsoft.db')
#创建游标对象
cursor = conn.cursor()

#执行sql语句
cursor.execute('create table user(id INT (10) PRIMARY KEY ,name VARCHAR (20))')

#关闭游标
cursor.close()

#关闭连接
conn.close()


