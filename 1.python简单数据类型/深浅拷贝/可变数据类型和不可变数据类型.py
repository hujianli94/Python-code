#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/21 9:33
# filename: 可变数据类型和不可变数据类型.py

'''
不可变类型:
    int、float、str、tuple、bool
'''

# int类型为不可变，重新定义之后，内存地址改变
Int_var = 10
print(Int_var, "-------->", id(Int_var))  # 10 --------> 1762591504

Int_var = 20
print(Int_var, "-------->", id(Int_var))  # 20 --------> 1762591824

print()

# float类型为不可变，重新定义之后，内存地址改变
float_var = 10.111
print(float_var, "-------->", id(float_var))  # 10.111 --------> 1701696015480

float_var = 20.111
print(float_var, "-------->", id(float_var))  # 20.111 --------> 1701696015408

print()

# str类型为不可变，重新定义之后，内存地址改变
Str_var = "hello hujianli"
print(Str_var, "-------->", id(Str_var))  # hello hujianli --------> 1701662799344

Str_var = "hello huxiaojian"
print(Str_var, "-------->", id(Str_var))  # hello huxiaojian --------> 1701712521376

print()
# tuple类型为不可变，重新定义之后，内存地址改变
tuple_var = (1, 2, 3)
print(tuple_var, "------>", id(tuple_var))  # (1, 2, 3) ------> 1701712521040
tuple_var = (1, 2, 3, 4, 5, 6)
print(tuple_var, "------>", id(tuple_var))  # (1, 2, 3, 4, 5, 6) ------> 1701712508296
print()

# bool类型为不可变，重新定义之后，内存地址改变
bool_var = True
print(bool_var, "------>", id(bool_var))  # True ------> 1762336944

bool_var = False
print(bool_var, "------>", id(bool_var))  # False ------> 1762336976
print()

'''
可变数据类型：
    list、set、dict
'''

# 可变数据类型
list1 = [1, 2, 3, 4, 5, 6]
print(list1, "------------->", id(list1))  # [1, 2, 3, 4, 5, 6] -------------> 2048223991688
list1.append(7)
print(list1, "------------->", id(list1))  # [1, 2, 3, 4, 5, 6, 7] -------------> 2048223991688
