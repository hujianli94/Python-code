#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql


def create_table():
    db = pymysql.connect('localhost', 'root', 'admin#123', 'test')
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在就删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE (
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT,
      CREATE_TIME DATETIME)"""
    try:
        cursor.execute(sql)
        print("CREATE TABLE SUCCESS.")
    except Exception as ex:
        print("CREATE TABLE FAILED,CASE:{}".format(ex))
    finally:
        # 关闭数据库连接
        db.close()


def main():
    create_table()


if __name__ == '__main__':
    main()
