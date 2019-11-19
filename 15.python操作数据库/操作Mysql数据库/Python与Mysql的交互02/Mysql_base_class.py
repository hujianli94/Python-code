#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaojian'
import pymysql
from mysql_env import mysql_info


class Mysql_SQL():
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def connet(self):
        self.db = pymysql.connect(self.host, self.user,
                                  self.passwd, self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        rest = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res1 = self.cursor.fetchone()
            title = self.cursor.description
            # print(res)
            # print(title)
            rest = dict(zip([k[0] for k in title], res1))
            self.close()
        except:
            print("查询数据失败")
        return rest

    def get_all(self, sql):
        res1 = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            title = self.cursor.description
            rest1 = [dict(zip([k[0] for k in title], row)) for row in res]
            self.close()
        except:
            print("查询数据失败")
        return rest1

    def insert(self, sql):
        return self.__edit_one(sql)

    def update(self, sql):
        return self.__edit_one(sql)

    def delete(self, sql):
        return self.__edit_one(sql)

    def __edit_one(self, sql):
        """
        #准备SQL
        #获取链接和cursor
        #提交数据到数据库
        #提交事务
        #关闭cursor和链接
        :param sql:
        :return:
        """
        count = 0
        try:
            # 连接数据库
            self.connet()
            count = self.cursor.execute(sql)
            # 提交事务
            self.db.commit()
            # 关闭数据库
            self.close()
            print("数据库语句执行完毕！")
        except:
            print("事务提交失败！")
            self.db.rollback()
        return count


if __name__ == '__main__':
    hu_mysql = Mysql_SQL(**mysql_info)
    hu_mysql.connet()
    # get_one = hu_mysql.get_one("select * from students1;")
    # print(get_one)

    # find_all = hu_mysql.get_all("select * from students1;")
    # for i in find_all:
    #     print(i)
    # sql = 'INSERT INTO students1 (`name`,`nickname`,`sex`) VALUES ("hu2","xiaojian2","男");'
    # hu_mysql.insert(sql)

    sql = 'INSERT INTO students1 (`name`,`nickname`,`sex`) VALUES ({},{},{});'
    sql = sql.format('"hu3"','"xiaojian3"','"男"')
    hu_mysql.insert(sql)

