#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 15:10
# filename: 测试try嵌套.py
import datetime as dt


def read_date_from_file(filename):
    try:
        file = open(filename)
        try:
            in_date = file.read()
            in_date = in_date.strip()
            date = dt.datetime.strptime(in_date, "%Y-%m-%d")
            return date
        except ValueError as e:
            print("处理ValueError 异常")
            print(e)

    except FileNotFoundError as e:
        print("处理 FileNotFoundError异常")
        print(e)

    except OSError as e:
        print("处理 OSError 异常")
        print(e)

date = read_date_from_file("readme1.txt")
print("日期 ={0}".format(date))