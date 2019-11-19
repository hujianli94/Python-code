#!/usr/bin/env python
#-*- coding:utf8 -*-
class Person(object):
    '''
    人类
    '''
    name = "hujianli"


class Student(Person):
    def __init__(self,school_name):
        self.school = school_name


if __name__ == '__main__':
    user = Student("仙剑")
    print(user.__dict__)        #查看类属性，自省
    print(Person.__doc__)
    print(Person.__dict__)
    user.__dict__["school_addr"] = "北京"
    print(user)
    print(user.__dict__)
    print(dir(user))