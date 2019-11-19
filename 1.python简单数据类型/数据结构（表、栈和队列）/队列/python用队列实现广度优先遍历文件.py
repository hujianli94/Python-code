#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
主要利用队列的先进先出，本案例中可以想象一下就是，先把根目录加入队列，
然后从队列中弹出根目录，并判断是否为文件夹，因为根目录是个文件夹，所以就打开这个目录，
把根里面的所有东西添加到队列中，此时队列中就是上图中A层级的所有文件，然后循环对A层级所有东西进行判断。
A层级执行完以后，B层级加入队列在执行，然后C执行,就这样直到队列为空停止。
'''
import os
from collections import deque#从收集模块中导入双端队列
class GuangDu:
    def __init__(self,path):
        "初始换函数，读取的根目录"
        self.path =path
        self.MyList =deque([])#实例化一个队列
        self.MyList.append(self.path)#把根目录路径放入队列中

    def  BianLi(self):
        "广度遍历的方法实现"
        while len(self.MyList) !=0:#当队列中为空的时候跳出循环
            path =self.MyList.popleft()#从队列中弹出一个路径
            if os.path.isdir(path):#对弹出的path路径判断是否是一个文件夹
                print("文件夹",path)#打印文件夹的路径
                myFilePath =os.listdir(path)#如果是一个文件夹，就把文件夹里面的所有东西添加进列表中，
                for line in myFilePath:#对添加到列表中的东西进行遍历
                    myPath =path +"\\"+line#形成绝对路径，
                    self.MyList.append(myPath)#把遍历的东西都加入到队列中
            else:#如果不是一个文件夹，就直接把路径打印出来，不用对其进行遍历了
                print("\t 文件",path)

    def __del__(self):
        "最终会执行的函数"
        pass

path_sc = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#初始的文件目录

file =GuangDu(path_sc)#实例化一个对象
file.BianLi()#对象调用方法
