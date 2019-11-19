#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql


def delete_record():
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123456", "ttmgrportal")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "delete from student4 WHERE money = 110"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        print("DELETE SUCCESS.")
    except Exception as ex:
        print("DELERE RECORD FAILED.Case:{}".format(ex))
        # 发送错误时回滚
        db.rollback()
    finally:
        # 关闭连接
        db.close()


def main():
    delete_record()


if __name__ == '__main__':
    main()
