#!/usr/bin/env python
# -*- coding:utf8 -*-
import datetime as dt

class MyException(Exception):
    """
    自定义异常类 MyError
    """
    def __init__(self, message):
        super(MyException, self).__init__(message)



def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, "%Y-%m-%d")
        return date
    except ValueError as e:
        raise MyException("不是有效的日期")

    except FileNotFoundError as e :
        raise MyException("文件找不到.....")

    except OSError as e:
        raise MyException("文件无法打开或无法读取.....")


date = read_date_from_file("readme2.txt")
print("日期 = {0}".format(date))
