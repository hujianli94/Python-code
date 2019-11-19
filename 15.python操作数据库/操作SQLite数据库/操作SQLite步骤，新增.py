#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
操作数据库：增、删、改、查
查询不需要commit方法来提交事务
'''

#导入模块
import sqlite3

#创建连接对象
conn = sqlite3.connect('mrsoft.db')

#创建游标对象
cursor = conn.cursor()


#执行sql语句
# sql = 'insert INTO  USER (id,NAME ) VALUES (1, "mrsoft")'
# cursor.execute(sql)
#防止SQL注入，使用占位符，元祖替换
sql = 'insert into user (id,NAME ) VALUES (?,?)'
# cursor.execute(sql,(2,'hujianli'))

#同时插入多条记录
data = [(1,'hu'),(2,'xiaojian'),(3,'hujianli'),(4,'kebe'),(5,'xiaojian')]
cursor.executemany(sql, data)

#关闭游标
cursor.close()

#提交事务
conn.commit()

#关闭连接
conn.close()


