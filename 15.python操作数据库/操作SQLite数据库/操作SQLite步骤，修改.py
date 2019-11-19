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
sql = 'update user set NAME = ? WHERE id = ?'           #修改id为1的记录
cursor.execute(sql, ('MR', 1))

#关闭游标
cursor.close()

#提交事务
conn.commit()

#关闭连接
conn.close()


