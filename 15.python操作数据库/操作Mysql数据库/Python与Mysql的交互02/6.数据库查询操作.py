#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
"""
fetchone()
功能:获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数
"""
import pymysql


def query_data():
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123456", "ttmgrportal")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL查询语句
    sql = "select * from student4 where money>100"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        reslist = cursor.fetchall()
        for row in reslist:
            # 输出结果
            print("%d -- %d" % (row[0], row[1]))
    except Exception as ex:
        print("Error:unable to fecth data.Error info:{}".format(ex))
        # 如果提交失败，回滚到上一次数据
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


def main():
    query_data()


if __name__ == '__main__':
    main()
