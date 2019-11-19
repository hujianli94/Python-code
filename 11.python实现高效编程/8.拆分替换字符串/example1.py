#!/usr/bin/env python
#-*- coding:utf8 -*-

a='Hello!World!'
t = a.maketrans('l','a')
t1 = a.maketrans("!"," ")
print(a.translate(t))
print(a.translate(t1))


# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))