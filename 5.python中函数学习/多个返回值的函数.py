#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 16:05
# filename: 多个返回值的函数.py

def sum_and_avg(list):
    sum = 0
    count = 0
    for i in list:
        if isinstance(i, int) or isinstance(i, float):
            count += 1
            sum += i
    return sum, sum / count


mylist = [11, 22, 33, 44, 55, 66, 77]
sum_test = sum_and_avg(mylist)
sum_num, average_num = sum_and_avg(mylist)
print(sum_num)
print(average_num)
print("sum_test函数中的sum为【{}】".format(sum_test[0]))
print("sum_test函数中的avg为【{}】".format(sum_test[1]))
