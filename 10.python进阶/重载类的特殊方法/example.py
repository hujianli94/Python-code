#!/usr/bin/env python
#-*- coding:utf8 -*-

#自定义类实现类的特别的运算方式

class Book:

    def __init__(self,name="python入门到精通"):
        self.name = name

    def __add__(self, other):
        #加运算
        return self.name + ' add ' + other.name        #得到书名相加

    def __len__(self):
        return len(self.name)

if __name__ == '__main__':
    booka = Book()
    bookb = Book('Java入门到精通')
    print("len(booka):",len(booka))
    print("len(bookb):",len(bookb))
    print(booka + bookb)
