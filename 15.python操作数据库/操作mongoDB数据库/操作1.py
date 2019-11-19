#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/25 14:48
# filename: 操作1.py
from pymongo import MongoClient
import random

src = "abcdefghijklmnopqrstuvwxyz"


def get_str(x, y):
    """ 生成随机数，x~y之间的随机字母字符串"""
    str_sum = random.randint(x, y)  # 产生x,y之间一个随机整数
    astr = ""
    for i in range(str_sum):
        astr += random.choice(src)
    return astr


def get_data_list(n):
    res = []
    for i in range(n):
        res.append({"name": get_str(2, 4), "passwd": get_str(8, 12)})
    return res


if __name__ == '__main__':
    print("建立连接...................")
    '''
    db = MongoClient()
    db_test = db.test
    stus = db_test.stu
    '''
    stus = MongoClient().test.stu  # 一条语句实现连接到集合
    print("插入一条记录.................")
    stus.insert({"name:": get_str(2, 4), "passwd": get_str(8, 12)})
    print("显示所有记录...................")
    stu = stus.find()  # 显示刚才插入的一个文档
    print(stu)

    # 批量插入多条记录
    stus.insert(get_data_list(3))
    # 显示所有记录
    print("显示所有记录................")
    for stu in stus.find():
        print(stu)

    print("更新一条记录..........")
    name = input("请输入记录的name: ")
    stus.update({"name": name}, {"$set": {"name": "aaaa"}})  # 更新
    print("显示所有记录")
    for stu in stus.find():
        print(stu)

    print("删除一条记录.........")
    name = input("请输入记录的name:")
    stus.remove({"name": name})
    print("显示所有记录................")
    for stu in stus.find():
        print(stu)
