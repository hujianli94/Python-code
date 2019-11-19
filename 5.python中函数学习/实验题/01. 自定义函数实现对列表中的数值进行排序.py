#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/31 16:43
# filename: 01. 自定义函数实现对列表中的数值进行排序.py

def list_sort(list_args):
    """
    列表排序
    :return:
    """
    try:
        isinstance(list_args, list) or isinstance(list_args, tuple)
        list_args = sorted(list(list_args))
        return list_args

    except Exception as e:
        print(e)


list_args = [3, 4, 2, 7, 8, 9, 11, 24, 46, 22, 13, 56]
# tuple_args = (3, 4, 2, 7, 8, 9, 11, 24, 46, 22, 13, 56)
print(list_sort(list_args))
# print(list_sort(tuple_args))
