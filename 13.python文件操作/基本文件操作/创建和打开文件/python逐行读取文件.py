#!/usr/bin/env python
#-*- coding:utf8 -*-

path = r"写入文件内容.py"
#传入要读的文件路径

file = open(path,"r",encoding="utf-8",errors="ignore")
"""
open表示打开你要执行的文件用读的方式打开
第一个参数是上面的文件path路径,第二个是所要执行的操作，（r）代表读，
#encoding="utf-8表示指定编码为“utf-8”，errors="ignore"表示读的时候遇到错误忽略

"""
while True:
    mystr = file.readline()#表示一次读取一行
    if not mystr:
    #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
        break
    print(mystr,end="")#打印每次读到的内容
