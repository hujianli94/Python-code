#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/23 21:52
# filename: 装饰器函数001.py

import datetime


def time(func):
    def wrapper():
        start_time = datetime.datetime.now()
        print(start_time)
        func()
        end_time = datetime.datetime.now()
        print(end_time)
        print("time use :{}".format(end_time - start_time))

    return wrapper


@time
def loop():
    print("start.....")
    for i in range(100000000):
        pass
    print("finish......")


if __name__ == '__main__':
    loop()

"""
2019-09-23 21:55:12.081090
start.....
finish......
2019-09-23 21:55:14.501618
time use :0:00:02.420528
"""