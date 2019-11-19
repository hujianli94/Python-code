#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/22 9:21
# filename: 类的继承4.py
import types


class Person(object):
    def __init__(self, name="", age=20, sex='man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if type(name) != str:
            print("名字必须是字符串")
            return
        self.__name = name

    def setAge(self, age):
        if type(age) != int:
            print("年龄必须是整数")
            return
        self.__age = age

    def setSex(self, sex):
        if sex != "男" and sex != "女":
            print("性别输入错误")
            return
        self.__sex = sex

    def show(self):
        print("姓名：{0}  性别：{1}  年龄：{2}".format(self.__name, self.__age, self.__sex))


class Student(Person):
    def __init__(self, name="", age=20, sex='man', schoolyear=2018):
        super(Student, self).__init__(name, age, sex)
        self.setSchoolyear(schoolyear)

    def setSchoolyear(self, schoolyear):
        if type(schoolyear) != int:
            print("输入入学年份错误")
            return
        self.__schoolyear = schoolyear

    def show(self):
        Person.show(self)
        print("入学年份：{0}".format(self.__schoolyear))


if __name__ == '__main__':
    zhangsan = Person("张三", 18, "男", )
    zhangsan.show()

    lisi = Student("李四", 21, "男", 2019)
    lisi.show()
    lisi.setAge(20)
    lisi.setSchoolyear(2015)
    lisi.show()
