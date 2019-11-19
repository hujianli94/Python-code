#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 12:47
# filename: 08.用生成器表达式来改写数据量较大的列表表达式.py
it = (print(x) for x in open("02.遵循PEP8风格指南.py",encoding="utf-8"))
print(it)
next(it)
next(it)
next(it)
next(it)
next(it)
"""
1.当输入的数据量较大时，列表推导可能会因为占用内存太多而出问题
2.由生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免了内存用量问题
3.把某个生成器表达式所返回的迭代器，放在另一个生成器表达式的for子表达式中，即可将二者组合起来
4.串在一起的生成器表达式执行速度很快
"""