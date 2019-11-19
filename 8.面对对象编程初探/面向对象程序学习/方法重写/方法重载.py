#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
class fangfa1:
    def __init__(self):
        pass

    def speak(self):
        print("hujianli say .....")


class Fangfa2(fangfa1):
    def __init__(self):
        pass

    def speak(self):
        """
        方法重载，子类和父类有相同的方法时，子类默认会修改掉父类的方法
        :return:
        """
        print("xiaojian  say ......")


if __name__ == '__main__':
    hu = Fangfa2()
    hu.speak()
'''


class Bird(object):
    def chirp(self):
        print("make sound")

class Chicken(Bird):
    def chirp(self):
        super().chirp()
        print("ji")

if __name__ == '__main__':
    bird = Bird()
    bird.chirp()

    summer = Chicken()
    summer.chirp()