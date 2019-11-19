#!/usr/bin/env python
#-*- coding:utf8 -*-
def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return "user"
        return User

    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

if __name__ == '__main__':
    Myclass = create_class("user")
    my_obj = Myclass()
    print(my_obj)    #user
    print(type(my_obj))     #<class '__main__.create_class.<locals>.User'>