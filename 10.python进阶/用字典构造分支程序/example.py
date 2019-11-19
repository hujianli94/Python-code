#!/usr/bin/env python
#-*- coding:utf8 -*-
import random

#定义3个分支函数
def print_a():
    print("路径分支A")

def print_b():
    print("路径分支B")

def print_c():
    print("路径分支C")

if __name__ == '__main__':
    path_dict = {}
    path_dict['a'] = print_a
    path_dict['b'] = print_b
    path_dict['c'] = print_c
    paths = 'abc'
    for i in range(4):
        path = random.choice(paths)
        print("选择了路径:",path)
        path_dict[path]()
