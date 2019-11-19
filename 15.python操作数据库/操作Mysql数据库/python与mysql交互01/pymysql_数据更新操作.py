#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 11:19
# filename: pymysql_数据更新操作.py
import pymysql

# 1.建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin#123',
                             database='hujianli2',
                             charset='utf8')

try:
    # 2.创建游标对象
    with connection.cursor() as cursor:

        # 3.执行SQL操作
        sql = "update user set name = %s where userid > %s"
        affectedcount = cursor.execute(sql, ("hujianli", 2))
        print("影响的数据行数:{0}".format(affectedcount))
        # 4. 提交数据库事务
        connection.commit()
        # 5.with代码块结束，关闭游标
except pymysql.DatabaseError as e:
    # 6.回滚数据库事务
    connection.rollback()
    print(e)

finally:
    # 7.关闭数据库连接
    connection.close()
