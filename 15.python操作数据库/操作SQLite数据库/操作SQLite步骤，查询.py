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
sql = 'select * from USER '
cursor.execute(sql)
'''
cursor.fetchone()       #获取第一条
cursor.fetchone()       #获取第二条记录
result1 = cursor.fetchone()     #获取第三条记录
print(result1)
'''
'''
# result2 = cursor.fetchmany(3)
result3 = cursor.fetchmany(5)
# print(result2)
print(result3)
'''
result_all = cursor.fetchall()      #获取所有的记录
print(result_all)

#关闭游标
cursor.close()

#关闭连接
conn.close()


