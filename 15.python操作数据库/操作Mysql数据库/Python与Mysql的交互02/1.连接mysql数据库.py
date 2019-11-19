#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql

# 连接数据库
'''
参数1：mysql服务所在主机的IP
参数2：用户名
参数3：密码
参数4：要连接的数据库名
'''


def db_connect():
    # 打开数据库连接
    db = pymysql.connect('localhost', 'root', 'admin#123', 'test')
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute("SELECT VERSION()")

    # 使用fetchone()方法获取单条数据
    data = cursor.fetchone()

    print("Database version:{}".format(data[0]))
    # 关闭数据库连接
    db.close()


def main():
    db_connect()


if __name__ == '__main__':
    main()
