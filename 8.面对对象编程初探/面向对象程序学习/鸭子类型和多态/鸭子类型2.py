#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/6 14:51
# filename: 鸭子类型2.py
class Animal(object):
    def run(self):
        print("动物跑......")


class Dog(Animal):
    def run(self):
        print("狗狗跑.....")

class Car:
    def run(self):
        print("汽车跑.....")


def go(animal):     #参数是Animal
    animal.run()



hu1 = Animal()
hu2 = Dog()
hu3 = Car()

go(hu1)
go(hu2)
go(hu3)