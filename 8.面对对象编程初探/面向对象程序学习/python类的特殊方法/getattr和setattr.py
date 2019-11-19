#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/15 2:54
# filename: getattr和setattr.py
class Rectangle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        # print("--------设置{}属性-----".format(key))
        if key == "name":
            if 2 < len(value) <= 8 or len(value) > 8:
                self.__dict__["name"] = value
            else:
                raise ValueError("name 的长度必须在2~8之间")
        elif key == "age":
            if 10 < value < 60:
                self.__dict__["age"] = value
            else:
                raise ValueError("age必须在10~60之间")


if __name__ == '__main__':
    hu = Rectangle("huajianli", 20)
    print(hu.name)
    print(hu.age)
    hu.age = 12
    hu.name = "huj"
    print(hu.name)
    # hu.age = 2  #报错



