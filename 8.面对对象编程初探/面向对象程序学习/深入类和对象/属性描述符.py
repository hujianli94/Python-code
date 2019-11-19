#!/usr/bin/env python
#-*- coding:utf8 -*-
#属性描述符

import numbers

#只要一个类实现了下面三种魔法函数中的一种，这个类就是属性描述符
class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("必须为int")
        self.value = value
    def __delete__(self, instance):
        pass

class User:
    age = IntField()

if __name__ == '__main__':
    user = User()
    user.age = "test"
    # user.age = 24
    print(user.age)
