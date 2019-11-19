#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/29 11:28
# filename: 异常处理1.py

def yichang(index, flag=False):
    studyname = ["hujianli", "hujianli2", "huajianli3"]

    if flag:
        try:
            rst = studyname[index]
        except:
            print("index error.....")
        return "Try test finishing..."
    else:
        rst = studyname[index]
        return "No try test finishing"


if __name__ == '__main__':
    print("Start Right params testing....")
    print(yichang(1, True))
    print(yichang(1, False))
    print("Error params test start.....")
    #超出index范围，flag为True，进行自定义的异常
    print(yichang(4, True))
    #超出index范围，且flag为Fasle，直接触发系统内部异常
    print(yichang(4, False))
