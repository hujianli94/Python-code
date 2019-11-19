#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql


def insert_record():
    db = pymysql.connect('192.168.2.122', 'root', '123456', 'ttmgrportal')
    cursor = db.cursor()

    # 插入数据，捕获异常
    sql = "insert into student4 VALUES(3,110),(4,220)"
    try:
        cursor.execute(sql)
        # 提交事务
        db.commit()
    except Exception as ex:
        print("INSSET INTO MYSQL table faild.Case:{}".format(ex))
        # 如果提交失败，回滚到上一次的数据
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


def main():
    insert_record()


if __name__ == '__main__':
    main()
