#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 11:07
# filename: pymysql_插入操作.py
import pymysql


# 查询最大用户Id
def read_max_userid():
    with connection.cursor() as cursor:
        # 3.执行SQL操作
        sql = 'select max(userid) from user '
        cursor.execute(sql)

        # 4.提取结果集
        row = cursor.fetchone()  # 提取1条数据

    return row[0]


# 1.建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin#123',
                             database='hujianli2',
                             charset='utf8')
# 查询最大值
maxid = read_max_userid()

try:
    # 2.创建游标对象
    with connection.cursor() as cursor:
        # 3.执行SQL操作
        sql = 'insert into user (userid,name) values (%s,%s)'
        nextid = maxid + 1
        name = "Tony" + str(nextid)
        affectedcount = cursor.execute(sql, (nextid, name))
        print("影响的数据行数:{0}".format(affectedcount))
        # 4.提交数据库事务
        connection.commit()
except pymysql.DatabaseError:
    # 5.回滚数据库事务
    connection.rollback()
finally:
    # 6.关闭数据连接
    connection.close()
