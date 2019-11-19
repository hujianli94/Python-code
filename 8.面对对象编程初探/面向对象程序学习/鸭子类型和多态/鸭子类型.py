#!/usr/bin/env python
#-*- coding:utf8 -*-
class Dog(object):
    def say(self):
        print("a dog")

class Cat(object):
    def say(self):
        print("a cat")

class Duck(object):
    def say(self):
        print("a duck")


# animal_list = [Dog, Cat, Duck]
#
# for animal in animal_list:
#     animal().say()

def yazi(func):
    func.say()

a = Dog()
b = Cat()
yazi(a)
yazi(b)