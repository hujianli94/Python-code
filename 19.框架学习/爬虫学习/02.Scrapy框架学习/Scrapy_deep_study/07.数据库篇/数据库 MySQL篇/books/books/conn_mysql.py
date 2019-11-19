#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/13 10:41
# filename: conn_Redis.py

# -*- coding: utf-8 -*-
import pymysql

#连接数据库，得到Connection对象
conn = pymysql.connect(host='localhost',user='root',db='scrapydb',port=3306,charset='utf8')

#创建Cursor对象，用于执行SQL语句
cursor = conn.cursor()

#创建数据表
cursor.execute("CREATE TABLE person(name VARCHAR(32),age INT,sex char(1)) ENGINE INNODB DEFAULT CHARSET=utf8")

#插入一条数据
cursor.execute('INSERT INTO person VALUES(%s,%s,%s)',('李小龙',23,'M'))

#保存变更，commit后数据才会实际写入数据库
conn.commit()

#关闭连接
conn.close()