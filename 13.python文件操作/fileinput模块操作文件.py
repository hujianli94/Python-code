#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/28 13:00
# filename: fileinput模块操作文件.py
'''
fileinput.input(): 返回一个可以用于迭代的一个或多个文件所有行的对象
fileinput.lineno():返回当前读取的行的数量
fileinput.filename():  返回当前的文件名称
fileinput.filelineno()：返回当前读取行在文件中的行数
fileinput.isfirstline()：返回当前行是否是文件的第一行
'''
import fileinput


def demo_fileinput():
    with fileinput.input(["test_num.txt", "test2_num.txt"]) as lines:  # 使用with语句
        for line in lines:
            print("总第{0}行,文件{1}中第{2}行".format(fileinput.lineno(),
                                              fileinput.filename(),
                                              fileinput.filelineno()))
            print(line.strip())

if __name__ == '__main__':
    demo_fileinput()