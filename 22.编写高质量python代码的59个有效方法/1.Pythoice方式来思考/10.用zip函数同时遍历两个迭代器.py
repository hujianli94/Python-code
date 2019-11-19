#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 13:37
# filename: 10.用zip函数同时遍历两个迭代器.py
names = ['hujianli1','hujianli2','hujianli3']
ids = [1,2,3]
letters = [len(n) for n in names]
print(letters)
for i,z in zip(names,ids):
    data = {i:z}
    print(data)


"""
1.内置的zip函数可以平行地遍历多个迭代器
2.python3中的zip相当于生成器、会在遍历过程中逐次产生元祖，python2中的zip则是直接把这些元祖完全生成好，并一次性地返回整份列表
3.如果提供的迭代器长度不等，那么zip就会自动提前终止
4.itertools内置模块中的zip_longest函数可以平行地遍历多个迭代器，而不用在乎它们的长度是否相等
"""
