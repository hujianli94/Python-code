#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/17 23:08
# filename: 不可变集合.py
student_set = frozenset({"张三", "李四", "王五"})
print(student_set)
print(type(student_set))

#报错，不能被修改
# print(student_set.add("胡六"))

