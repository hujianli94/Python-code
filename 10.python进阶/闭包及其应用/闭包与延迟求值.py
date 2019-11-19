#!/usr/bin/env python
#-*- coding:utf8 -*-
#闭包可以实现将参数传递给一个函数，并不立即运行，已达到延迟求值的目的

def delay_fun(x,y):
    def caculator():
        return x + y
    return caculator

if __name__ == '__main__':
    print("返回一个求和的函数,并不立即求和。")
    msun = delay_fun(3,4)
    print()
    print("调用求和：")
    print(msun())