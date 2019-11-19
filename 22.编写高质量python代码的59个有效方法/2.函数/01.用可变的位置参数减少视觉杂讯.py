#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 18:29
# filename: 01.用可变的位置参数减少视觉杂讯.py

"""
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print("%s :%s" % (message, values_str))


log("My numbers are", 1, 2)
log('Hi there')

favorites = [7, 33, 99]
log('Favorite colors', *favorites)

"""


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)


"""
1.在def语句中使用*args，即可令函数接受数量可变的位置参数
2.调用函数时，可以采用*操作符，把序列中的元素当成位置参数，传给该函数
3.对生成器使用*操作符，可以能导致程序耗尽内存并崩溃
4.在已经接受*args参数的函数上面继续添加位置参数，可能会产生难以排查的bug。
"""