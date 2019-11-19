#!/usr/bin/env python
# -*- coding:utf8 -*-
# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def info(self):
#         print("学生:{}； 分数{}".format(self.name,self.score))

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print("学生:{}； 分数{}".format(self.__name, self.__score))

    def set_score(self, score):
        if 0 < score <= 100:
            self.__score = score
        else:
            print("请输入0~100之间的数字")

    def get_score(self):
        return self.__score


if __name__ == '__main__':
    hu = Student("hujianli", "100")
    hu.info()
    print("修改前的分数{}".format(hu.get_score()))
    hu.set_score(0)
    print("修改后的分数{}".format(hu.get_score()))
