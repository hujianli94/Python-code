#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/22 10:49
# filename: pymysql_有条件的查询.py
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
        sql = 'select name,userid from user where userid > %(id)s'
        cursor.execute(sql, {'id': 0})

        # 4.提取结果集
        result_set = cursor.fetchall()

        for row in result_set:
            print("id:{0} - name:{1}".format(row[1], row[0]))

        # 5.with代码块结束，关闭游标
finally:
    # 6.关闭数据连接
    connection.close()
