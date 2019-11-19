#!/usr/bin/env python
# -*- coding:utf8 -*-


class Animal(object):
    def run(self):
        print("动物跑......")


class Dog(Animal):
    def run(self):
        print("狗狗跑.....")


class Car(Animal):
    def run(self):
        print("汽车跑.....")


if __name__ == '__main__':
    f1 = Animal()           # 没有发生多态
    f1.run()

    f2 = Dog()              # 发生多态
    f2.run()

    f3 = Car()              # 发生多态
    f3.run()
