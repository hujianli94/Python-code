#!/usr/bin/env python
#-*- coding:utf8 -*-


#导入PyMySQL模块
import pymysql

#调用connect()函数生成connection连接对象
db = pymysql.connect(host="39.96.10.11", user="hujianli",
                     password="admin#123", database="test_hu",
                     charset="utf8")

#调用cursor()方法，创建Cursor对象
cursor = db.cursor()

#执行SQL语句
cursor.execute('select version()')
data = cursor.fetchone()
print(data)

#关闭连接
cursor.close()
db.close()


