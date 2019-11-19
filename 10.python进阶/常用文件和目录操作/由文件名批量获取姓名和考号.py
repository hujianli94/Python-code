#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
filenames = []       #所有文件名的存放列表

for a,b,files in os.walk('test'):       #获取当前目录下test目录中的所有文件
    if files:
        filenames.append([file[:-4] for file in files])  #扩展名为3个字母

fname = 'testexam'          #指定生成电子表格的文件名
i = 0
for files in filenames:
    f = open(fname + str(i) + ".xls", 'w')          #打开指定文件夹
    for name in files:
        f.write(name[-2:]+"\t" + name[:-2] + '\n')
    f.close()
    i +=1
print("成功生成! ")

'''bnT|||||||||
通过os.walk()对目录下的所有文件进行遍历，获取包含学生信息的所有文件名字符串放入列表filenames中，
根据指定的电子表格文件名将学生姓名和考号写入文件中
'''
