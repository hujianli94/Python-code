#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql


def update_table():
    db = pymysql.connect("127.0.0.1", "root", "123456", "ttmgrportal")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL更新语句
    sql = "UPDATE student4 set money=15000 WHERE id=1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("UPDATE SUCCESS...")
    except Exception as ex:
        print("UPDATE MYSQL table faild.Case:{}".format(ex))
        # 发生错误时回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()
    db.close()


def main():
    update_table()


if __name__ == '__main__':
    main()
