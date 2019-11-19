#!/usr/bin/env python
#-*- coding:utf8 -*-
from datetime import datetime,date

class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value

if __name__ == '__main__':
    user = User("derek",date(year=1994,month=11,day=11))
    user.age = 23
    print(user._age)   # 23,setter设置的
    print(user.age)    # 24 ,动态计算出来的
