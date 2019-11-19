#!/usr/bin/env python
#-*- coding:utf8 -*-
#封装类

# 导入mysql模块
from pymysql import *


class MysqlPython:
    def __init__(self, database,  # 库
                 host="127.0.0.1",  # ip地址
                 user="root",  # 用户名
                 password="123456",  # 密码
                 port=3306,  # 端口
                 charset="utf8"):  # 字符集
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset

    def open(self):  # 创建数据库链接函数
        self.db = connect(host=self.host,
                          database=self.database,
                          user=self.user,
                          password=self.password,
                          port=self.port,
                          charset=self.charset)
        self.cur = self.db.cursor()  # 创建游标对象

    def close(self):  # 创建断开数据库链接　关闭游标函数
        self.cur.close()
        self.db.close()

    def zhixing(self, sql, L=[]):  # 创建pymysql.execute() 方法函数
        try:
            self.open()  # 链接数据库
            self.cur.execute(sql, L)  # 参数化执行ＳＱＬ命令
            self.db.commit()  # 提交数据
            print("ok")
        except Exception as e:
            self.db.rollback()  # 出错取消提交
            print("Failed", e)
        self.close()  # 断开数据库链接　关闭游标

    def all(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute(sql, L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed", e)
        self.close()