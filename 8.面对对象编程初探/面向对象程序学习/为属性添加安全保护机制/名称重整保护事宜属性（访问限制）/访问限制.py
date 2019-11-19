#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
要让内部的属性不被外部直接访问
'''
class Person(object):
    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def __init__(self,name,age,height,weight,money,input_hu):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money  #此属性已经变为'_Person__money'
        self.__input__ = input_hu

    #通过内部的方法，去修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def set_Money(self,money):
        #数据的过滤
        if money < 0:
            money = 0
        else:
            self.__money = money

    def get_Money(self):
        return self.__money

    def __del__(self):
        print("这里是析构函数")


per = Person("hujianli", 24, 180, 65,1000,"python")
print(dir(per))
print(dir(Person))
per.age = 18

#一般帅的人不这么使用，很不方便
per._Person__money = 22
print(per._Person__money)  #__money此时已经变成_Person__money了

#如果让内部属性不被外部直接访问，在属性前加__下划线
#如果在属性前加__下划线，那么这个属性就变成了私有属性,不能再实例化之后直接访问
# per.__money = 10


print(per.age)

print(per.get_Money())
print("开始赋值set_money" + " ====ing")
per.set_Money(100)
print("赋值之后的money是: {}".format(per.get_Money()))

#在python中__xxx___ 属于特殊变量，特殊变量的值可以直接访问
print("这是一个__xx__的特殊变量: %s" % per.__input__)

#一个下划线_xxx的变量，看到这样的变量时，表示当成私有属性，虽然可以直接在外部访问
#这是一个约定束城
