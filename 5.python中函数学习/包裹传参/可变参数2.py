#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/21 16:49
# filename: 可变参数2.py

def show_info(seq=":", **info):
    print("---------------------info---------------")
    print("info".center(40, "-"))

    for key, value in info.items():
        print("{0}{2}{1}".format(key, value, seq))


show_info("-->", name="hujianli", age=18, sex="Man")
show_info(name="hujianli2", age=19, sex="Man", seq="-")

stu_dict = {"name": "xiaojian", "age": "18"}  # 创建字典对象
show_info(**stu_dict)
