#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/13 9:43
# filename: createDB.py

# -*- coding: utf-8 -*-
import sqlite3

#连接数据库，得到Connection对象
conn = sqlite3.connect('scrapy.db')
#print(type(conn))

#创建Cursor对象，用于执行SQL语句
cur = conn.cursor()
#print(type(cur))

#创建数据表
cur.execute(''' CREATE TABLE books(
 upc CHAR(16) NOT NULL PRIMARY KEY,
 name VARCHAR(256) NOT NULL,
 price VARCHAR(16) NOT NULL,
 review_rating INT,
 review_num INT,
 stock INT
 );''')

#插入一条数据
# cur.execute('INSERT INTO person VALUES(?,?,?)',('李小龙',23,'M'))

#保存变更，commit后数据才会实际写入数据库
conn.commit()

#关闭连接
conn.close()