#!/usr/bin/env python
#-*- coding:utf8 -*-

print('蚂蚁庄园'.center(50,'='))
with open('message.txt','r') as f:
    f.seek(4)
    string = f.read(4)
    print(string)
    print('\n','='*29,'over','='*29,'\n')



#读取大文件时，建议采用while循环来逐行进行读取
with open('message.txt', 'r') as f1:
    number =0   #标识符为0开始
    while True:
        number +=1
        line = f1.readline()    #逐行读取文件
        if line == '':          #如果读取完毕，则跳出循环
            break
        print(number,line,end='\n')
    print("文件读取完毕".center(50,'='))
print()

print('蚂蚁庄园'.center(50,'='))
with open('message.txt','r') as f:
    string = f.readlines()
    for line in string:
        print(line)
    print('\n','='*29,'over','='*29,'\n')