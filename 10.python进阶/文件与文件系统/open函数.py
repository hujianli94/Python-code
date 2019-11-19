#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
a               附加数据
b               二进制数据模式
x               新建一个文件，可写
+               打开文件直接更新
t               文本模式（默认）

file.read([n])          将整个文件读入的字符串中，或指定n字节
file.readline([n])      读入文件的一行到字符串中
file.readlines()        将整个文件按行读入到列表中
file.write(s)           向文件中写入字符串
file.writelines(lines)  向文件中写入一个行数列表
file.close()            关闭打开的文件
'''


#演示处理文件中数据的例子
def file_hdl(name='python.txt'):
    '''
    打开文件处理函数
    '''
    f =open(name)   #打开文件
    res = 0
    i = 0
    for line in f:
        i +=1
        print("第{}行的数据是:{}".format(i, line.strip()))
        res +=len(line)
    print("这些数据的总和为：{}".format(res))
    f.close()

if __name__ == '__main__':
    file_hdl()

print()

def file_hdl(name='python.txt'):
    with open(name) as f:
        res =0
        i = 0
        for line in f:
            i +=1
            print("第{}行的数据为{}".format(i,line.strip()))
            res += len(line)
    print("这些数的和为:{}".format(res))

if __name__ == '__main__':
    file_hdl()










