#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/15 16:02
# filename: __repr__方法.py
class Apple:
    # 实现构造方法
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __repr__(self):
        '''
        重写__repr__()方法，实现Apple对象的“自我描述”
        :return:
        '''
        return "Apple[color=" + self.color + ", weight=" + str(self.weight) + "]"


if __name__ == '__main__':
    hu = Apple("红色", 5.68)
    print(hu)

