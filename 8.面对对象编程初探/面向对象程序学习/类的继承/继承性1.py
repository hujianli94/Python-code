#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/18 7:51
# filename: 继承性1.py
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        template = "Person [name={0},age={1}]"
        s = template.format(self.name, self.age)
        return s


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school  # 所在学校

    def info(self):
        '''
        方法重写
        :return:
        '''
        template = "Person [name={0},age={1},school={2}]"
        s = template.format(self.name, self.age,self.school)
        return s


if __name__ == '__main__':
    hujianli1 = Person("胡建力", 18)
    print(hujianli1.info())

    hujianli2 = Student("胡建力", 18, "西点大")
    print(hujianli2.info())
