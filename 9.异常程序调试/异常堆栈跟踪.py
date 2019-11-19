#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 8:40
# filename: 异常堆栈跟踪.py
# import datetime as dt
# import traceback as tb
#
#
# def read_date_from_file(filename):
#     try:
#         file = open(filename)
#         in_date = file.read()
#         in_date = in_date.strip()
#         date = dt.datetime.strftime(in_date, "%Y-%m-%d")
#         return date
#     except (ValueError,OSError) as e:
#         print("调用方法method1处理.....")
#         tb.print_exc()
#
# date = read_date_from_file("readme.txt")
# print("日期 = {0}".format(date))
import traceback


class SelfException(Exception):
    pass


def main():
    firstMethod()


def firstMethod():
    SecondMethod()


def SecondMethod():
    thirdMethod()


def thirdMethod():
    raise SecondMethod("自定义异常信息")


try:
    main()
except:
    # 捕获异常信息，并将异常信息输出到控制台
    traceback.print_exc()
    # 捕获异常信息，并将异常信息输出到指定文件中
    traceback.print_exc(file=open("log.txt", "a", encoding="utf-8"))
