#!/usr/bin/env python
#-*- coding:utf8 -*-
import time

def timer(parameter):

    def out_wrapper(func):

        def wrapper(*args,**kwargs):
            if parameter == "task1":
                start = time.time()
                func(*args,**kwargs)
                stop = time.time()
                print("the task1 run time is :",stop - start)
            elif parameter == "task2":
                start = time.time()
                func(*args,**kwargs)
                stop = time.time()
                print("the task2 run time is :",stop - start)
        return wrapper
    return out_wrapper


@timer("task1")
def task1():
    time.sleep(2)
    print("in the task1")

@timer("task2")
def task2():
    time.sleep(3)
    print("in the task2")

if __name__ == '__main__':
    task1()
    print("我是分割线".center(100, "*"))
    task2()