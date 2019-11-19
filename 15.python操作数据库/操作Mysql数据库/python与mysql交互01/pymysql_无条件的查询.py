#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 11:00
# filename: pymysql_无条件的查询.py
import pymysql

# 1.建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin#123',
                             database='hujianli2',
                             charset='utf8')

# 2.创建游标对象
try:
    with connection.cursor() as cursor:
        # 3.执行SQL操作
        sql = 'select max(userid) from user '
        cursor.execute(sql)
        # 4.提取结果集
        row = cursor.fetchone()  # 提取1条数据

        if row is not None:  # 判断非空时，提取字段内容
            print("最大用户Id:{0}".format(row[0]))
        # 5.with代码块结束，关闭游标
finally:
    # 6.关闭数据连接
    connection.close()
