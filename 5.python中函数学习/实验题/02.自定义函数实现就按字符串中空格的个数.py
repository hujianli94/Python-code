#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/31 16:59
# filename: 02.自定义函数实现就按字符串中空格的个数.py

def calc_kongge(string):
    str_list = string.split(" ")
    count = 0
    for i in str_list:
        if i == "":
            count += 1
    return count


str = ''' 你好哈   哈哈哈哈哈     my name is hujianli
yep you studying python   '''

print(calc_kongge(str))
