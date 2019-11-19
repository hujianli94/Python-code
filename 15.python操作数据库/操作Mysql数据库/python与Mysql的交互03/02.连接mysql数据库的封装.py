#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/19 9:39
# filename: 02.连接mysql数据库的封装.py

"""
安装pymysql数据库驱动程序:
pip install pymysql
运行完毕 查看是否成功 pip -m  list

"""

import time
import pymysql


# import decimal
class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def GetConnect(self):
        if not self.db:
            raise (NameError, '没有目标数据库')
        self.connect = pymysql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,
                                       charset='utf8')
        cur = self.connect.cursor()
        if not cur:
            raise (NameError, '数据库访问失败')
        else:
            return cur

    def ExecSql(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.connect.commit()
        self.connect.close()

    def ExecQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.connect.close()
        return resList


def main():
    ms = MSSQL(host="192.168.0.108", user="sa", pwd="sa", db="ComPrject")
    resList = ms.ExecQuery("select *from TestModel")
    print(resList)


if __name__ == '__main__':
    main()
    input("执行完成:")
