#!/usr/bin/env python
#-*- coding:utf8 -*-

class rangehu(object):
    def __init__(self,start,end,sep=1):
        self.start = start
        self.end = end
        self.sep = sep

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t +=self.sep

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -=self.sep

if __name__ == '__main__':
    for x in rangehu(1,10,2):
        print(x)
    print("正向迭代完毕.....")

    for x1 in reversed(rangehu(1,20,2)):
        print(x1)
    print("反向迭代完毕......")