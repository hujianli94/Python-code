#!/usr/bin/env python
#-*- coding:utf8 -*-
import os

class ShenDu:
    def __init__(self,path):
        "初始化函数，遍历的根目录"
        self.path = path
        self.MyList =[]#创建一个文件夹列表
        self.MyList.append(self.path)#把根目录加入列表中

    def BianLi(self):
        "对于遍历的具体实现"
        while len(self.MyList) !=0:
            path =self.MyList.pop()#弹出一个路径
            if os.path.isdir(path):#对弹出的路径进行判断是否为文件夹
                print("文件夹",path)
                myFileList =os.listdir(path)#如果是文件夹，就把文件夹中所有东西加入列表
                for line in myFileList:#循环列表（过滤文件）
                    myPath =path+"\\"+line#形成绝对路径
                    if os.path.isdir(myPath):#如果是文件夹就把这个文件夹添加到文件夹列表中
                        self.MyList.append(myPath)
                    else:#如果不是则输出
                        print("文件",myPath)
            else:#如果不是则输出
                print("文件",path)

    def __del__(self):
        "最终会执行的操作"
        pass
path =os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #根目录
file =ShenDu(path) #实例化对象
file.BianLi() #执行方法

