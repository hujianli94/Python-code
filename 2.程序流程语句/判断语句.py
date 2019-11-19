#!/usr/bin/env python
#-*- coding:utf8 -*-
def count_login():
    passwd = input("请输入密码: ")
    if passwd == "123.com":
        print("输入成功!")
    else:
        print("输入错误！重新输入")
        count_login()

count_login()