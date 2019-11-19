#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
1.内置作用域：python事先定义的
2.全局作用域：整个程序都可以使用的
3.局部作用局：某个函数内部范围
"""
def func_test():
    a = 0
    a +=3
    print("局部作用域为 %s " % a)

a = "hujianli"
print("全局作用域为{}".format(a))
func_test()
print("全局作用域为{}".format(a))


print("".center(100,"*"))
#使用global可以让局部作用域修改到全局
def function_test():
    global name
    name = "hujianli_neibu "
    name += "global test"

name = "external"
print("全局作用域为{}".format(name))
function_test()
print("全局作用域为{}".format(name))

#局部作用域可以引用全局作用域，但是不能修改
a = "hujianli"
def test():
    print(a)

test()

a = "test"
def test2():
    print(a)
    a = "hu"   #当在这里修改的时候会报错
test2()