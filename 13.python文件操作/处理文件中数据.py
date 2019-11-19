#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/28 12:51
# filename: 处理文件中数据.py
def file_hdl(name="test_num.txt"):
    res = 0  # 累加计数器
    i = 0  # 行数计数器
    with open(name,encoding="utf8") as f:
        for line in f:
            i += 1
            print("第{}行的数据为:{}".format(i, line.strip()))
            res += int(line)
        print("{}文件中数的和为{}".format(name, res))

file_hdl()
