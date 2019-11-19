#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
perfix = "python"               #perfix为重命名后的文件起始字符
length = 2                      #length为除去perfix后，文件名要达到的长度
base = 1                        #文件名的起始数
format = 'mdb'                  #文件名的后缀名
def PadLeft(str,num,padstr):
    stringlength = len(str)
    n = num - stringlength
    if n >= 0:
        str = padstr * n + str
    return str

#为了避免误操作，这里先提示用户
print("the files in {} will be renamed ".format(os.getcwd()))
all_files = os.listdir(os.getcwd())
print("输出当前目录下的所有文件名")
print([f for f in all_files if os.path.isfile(f)])
input_stin = input("press y to continue\n")      #获取用户输入
if input_stin.lower() != "y":           #判断用户输入，已决定是否执行重命名操作
    exit()
filenames = os.listdir(os.getcwd())     #获取当前目录中的内容
#基数减1，为了下面i = i + 1 在第一次执行时等于基数
i = base - 1
for filename in filenames:
    i +=1
    #判断当前路径是否为文件，并且不是"rename.py"
    if filename != "rename.py" and os.path.isfile(filename):
        name = str(i)           #将i转换成字符
        name = PadLeft(name,length,'0') #将name补全到指定长度
        t = filename.strip('.')         #分割文件名，以检查其是否是所要修改的类型
        m = len(t)
        if format == "":
            os.rename(filename,perfix+name+"."+t[m-1])
        else:
            if t[m-1] == format:
                os.rename(filename,perfix+name+'.'+t[m-1])
            else:
                i = i -1        #保证i连续
    else:
         i = i -1
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])  #输出当前目录下的所有文件名



