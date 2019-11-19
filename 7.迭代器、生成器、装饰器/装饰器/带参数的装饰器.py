#!/usr/bin/env python
# -*- coding:utf8 -*-
import time


def abc(action):
    def mabc(func):
        def wrapper(*args, **kwargs):
            print("开始运行....", action)
            func(*args, **kwargs)
            print("运行结束！....", action)

        return wrapper
    return mabc


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return deco


@timer
@abc("print_name")  # 带参数的装饰器
def deam_print_name(name):
    time.sleep(2)
    print("Hello {}!".format(name))


@timer
@abc("list_info")  # 带参数的装饰器
def deam_list_print(x):
    a = []
    time.sleep(2)
    for i in range(x):
        a.append(i)
    print(a)


if __name__ == '__main__':
    deam_list_print(8)
    print()
    print(''.center(100, "#"))
    print("".center(100, "#"))
    print()
    deam_print_name("hujianli")
