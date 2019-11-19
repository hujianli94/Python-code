#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 15:01
# filename: 简单的try+except使用.py
import datetime as dt


def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print("处理ValueError异常")
        print(e)


str_date = "201B-06-06"
print("日期 = {0}".format(read_date(str_date)))