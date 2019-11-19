#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/24 17:52
# filename: 操作MariaDB数据库.py
from mysql import connector
import random

src = "abcdefghijklmnopqrstuvwxyz"


def get_str(x, y):
    """ 生成随机数，x~y之间的随机字母字符串"""
    str_sum = random.randint(x, y)  # 产生x,y之间一个随机整数
    astr = ""
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


def output():
    """
    定义输出数据库表中所有记录函数
    :return:
    """
    # 执行查询
    cur.execute("select * from mytab")

    # 遍历记录
    for sid, name, ps in cur:
        print(sid, " ", name, " ", ps)  # 输出记录


def out_put_all():
    """
    定义输出数据库表中所有记录函数
    :return:
    """
    cur.execute("select * from mytab")
    for item in cur.fetchall():
        print(item)  # 使用fetchall()函数


def get_data_list(n):
    """
    定义生成记录列表数据的函数
    :param n:
    :return:
    """
    res = []
    for i in range(n):
        res.append((get_str(2, 4), get_str(8, 12)))
    return res


if __name__ == '__main__':
    print("建立连接.......................")
    con = connector.connect(host="localhost", user="hujianli", password="admin#123",
                            database="hujianliDB")  # 建立连接使用内存中的数据库
    # con = sqlite3.connect("test.db")  # 建立连接使用内存中的数据库
    print("建立游标.......................")
    cur = con.cursor()  # 获取游标
    print("创建一张表mytab.......................")
    sql = """ 
    CREATE TABLE `mytab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `passwd` text,
  PRIMARY KEY (`id`)
) Full_backuk-2019-08-13_09_28_42.sql DEFAULT CHARSET=utf8; """
    cur.execute(sql)
    print("插入一条记录.......................")
    cur.execute("insert into mytab(name,passwd)values (%s,%s)", (get_str(2, 4), get_str(8, 12),))  # 插入1条记录
    output()  # 显示所有记录
    print("批量插入多条记录.......................")
    cur.executemany("insert into mytab(name,passwd)values (%s,%s)", get_data_list(3))  # 插入多条记录
    print("显示所有记录........................")
    out_put_all()  # 显示所有记录
    print("更新一条记录..............")
    cur.execute("update mytab set name=%s where id =%s", ("aaa", 1))  # 更新记录
    print("显示所有记录.........................")
    output()  # 显示所有记录
    print("删除一条记录.......................")
    cur.execute("delete from mytab where id=%s", (3,))  # 删除一条记录
    print("显示所有记录：")
    output()  # 显示所有记录
    con.commit()        #提交数据
    cur.close()  # 关闭游标
    con.close()  # 关闭连接
