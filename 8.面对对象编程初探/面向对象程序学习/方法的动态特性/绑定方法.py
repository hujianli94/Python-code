#!/usr/bin/env python
#-*- coding:utf8 -*-

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self,val):
        self.val = val

    def __call__(self, arg):
        return self.val + arg


class Product:
    def __init__(self, val):
        self.val = val

    def method(self, arg):
        return self.val * arg


if __name__ == '__main__':
    sobject = Sum(2)
    poject = Product(3)

actions = [square, sobject, poject.method]

for act in actions:
    print(act(5))

print(actions[-1](5))
print([act(5) for act in actions])
print(list(map(lambda act:act(5),actions)))

table = {act(5): act for act in actions}
print(table.keys())
print(table.values())
print(table.items())