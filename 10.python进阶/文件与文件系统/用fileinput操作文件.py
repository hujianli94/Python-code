#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
1.input()   返回能够用于迭代一个或多个文件中所有行的对象；
2.filename() 返回当前文件的名称
3.lineno()  返回当前读取行的数量
4.isfirstline() 返回当前行是否文件的第一行
5.filelineno()  返回当前读取行在文件中的行数
input 也支持上下文管理，可以使用with语句来进行操作，不用再使用后手工关闭对象
'''
import fileinput
def demo_fileinput():
    with fileinput.input(['fpa.txt','fpb.txt']) as lines:       #用with语句
        for line in lines:
            print("总第{}行，".format(fileinput.lineno()),"文件{}中第{}行".format(fileinput.filename(),fileinput.filelineno()))
            print(line.strip())

if __name__ == '__main__':
    demo_fileinput()











