#!/usr/bin/env python
#-*- coding:utf8 -*-
def line(a,b):
    def aline(x):
        return a**x + b
    return aline            #泛型函数中可使用不同的a、b的值

if __name__ == '__main__':
    line23 = line(2, 3)      #a、b值分别为4、5的一次函数
    line50 = line(5, 0)      #a、b值分别为5、0的一次函数
    print(line23(4))
    print(line50(2))