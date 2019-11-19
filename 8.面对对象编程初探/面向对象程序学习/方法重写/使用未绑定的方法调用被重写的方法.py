#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 23:09
# filename: 使用未绑定的方法调用被重写的方法.py
class BaseClass:
    def foo(self):
        print("父类中定义的foo方法")

class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo(self):
        print("子类中重写父类的foo方法")

    def bar(self):
        print("执行bar方法")

        #直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()

        #使用类名调用实例方法(未绑定方法)调用父类被重写的方法
        BaseClass.foo(self)

if __name__ == '__main__':
    sc = SubClass()
    sc.bar()