#!/usr/bin/env python
#-*- coding:utf8 -*-
from foo import foo_fun    #导入foo模块中的函数foo_fun

name = "Current module"     #定义全局变量name

def bar():
    print("当前模块中函数bar:")
    print("变量name:",name) #输出全局变量name

def call_foo_fun(fun):      #定义调用传入函数作为参数的函数
    fun()                   #调用传入的函数

if __name__ == '__main__':
    bar()
    print()
    foo_fun()
    print()
    call_foo_fun(foo_fun)
