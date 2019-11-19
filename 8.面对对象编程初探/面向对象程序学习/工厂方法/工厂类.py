#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 15:52
# filename: 工厂方法.py
class Factory:
    def createFruit(self,fruit):
        if fruit == "apple":
            return Apple()
        elif fruit == "banana":
            return Banana()
        else:
            raise Exception("类不存在")



class Fruit:
    def __str__(self):
        return "fruit"

class Apple(Fruit):
    def __str__(self):
        return "apple"


class Banana(Fruit):
    def __str__(self):
        return "banana"


if __name__ == '__main__':
    factory = Factory()
    print(factory.createFruit("apple"))
    print(factory.createFruit("banana"))
    # print(factory.createFruit("banana22"))
