#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 15:19
# filename: 异常else语句.py
import datetime as dt


def read_date_file(filename):
    try:
        with open(filename) as file:
            in_date = file.read()
            in_date = in_date.strip()
            date = dt.datetime.strptime(in_date, "%Y-%m-%d")
            print("现在的时间是：{}".format(date))
    except ValueError as e:
        print("处理ValueError异常", e)
    except OSError as e:
        print("处理OSError异常", e)

    else:
        print("语句正常执行...无异常")


read_date_file("readme.txt")

