#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/29 18:55
# filename: test4.py、
from functools import wraps

def decorator1(func):
    @wraps(func)                # 消除装饰器带来的副作用。
    def wrapper(*args, **kwargs):
        """
        :param args:可变位置参数
        :param kwargs: 关键字参数
        :return:
        """
        func(*args, **kwargs)  # func = house
        print("铺地板")
        print("刷漆")

    return wrapper


@decorator1
def house():
    """
    我是house函数，
    :return:
    """
    print("---------->毛坯房")


house()

# print(house.__name__)     # 此时出现的是装饰器的名称和文档注释
# print(house.__doc__)

print(house.__name__)
print(house.__doc__)


'''
---------->毛坯房
铺地板
刷漆
house

    我是house函数，
    :return:
    

'''