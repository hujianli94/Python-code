#!/usr/bin/env python
#-*- coding:utf8 -*-
_width = 800
_height = 600

def change(w,h):
    global _width   #全局变量
    global _height  #全局变量
    _width = w  # 重新为宽度赋值
    _height = h  # 重新为高度赋值

def getWidth():
    global _width   #全局变量
    return _width

def getHeigh():
    global _height   #全局变量
    return _height

