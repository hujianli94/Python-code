#!/usr/bin/env python
#-*- coding:utf8 -*-
class Bird(object):
    def chirp(self):
        print("make sound")


class Chicken(Bird):
    def chirp(self):
        super(Chicken, self).chirp()
        print("ji")


if __name__ == '__main__':
    print("第一次实例化".center(100, "="))
    bird = Bird()
    bird.chirp()

    print("第二次实例化".center(100, "="))
    summer = Chicken()      #调用被覆盖的方法
    summer.chirp()

print("="*100)

__metaclass__ = type

class Person:
    def __init__(self):
        self.height = 160

    def about(self,name):
        print("{} is about {}".format(name,self.height))

class Girl(Person):
    def __init__(self):
        self.breast = 90
        # Person.__init__(self)
        super(Girl, self).__init__()

    def about(self,name):
        print("{} is a hot girl ,she is about {} height is {}".format(name, self.height, self.breast))
        super(Girl, self).about(name)


if __name__ == '__main__':
    hu = Girl()
    hu.about("wangxiaomei")