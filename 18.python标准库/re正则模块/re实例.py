#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
函数定义必须以 def 开头，def 后跟一个空格就是函数名
python变量通过匹配单词后接“=”的情况查找变量名
变量名与“=”之间有一空格
.       #匹配单个字符
*       #匹配位于*之前的0个或多个字符
+       #匹配位于+之前的一个或多个字符
|       #会匹配位于|之前或者之后的字符
^       #匹配行首
$       #匹配行尾
？       #匹配位于？之前的零个或一个字符
\       #表示位于\之后的为转义字符
[]      #匹配位于[]中的任何一个字符如r[ae]d会匹配"rad","red等
()      #将位于（）内的内容当作一个整体
{}      #按{}中的次数进行匹配
\d      #匹配一个数字字符
\D      #匹配一个非数字字符
\n      #匹配一个换行符
\r      #匹配一个回车符
\s      #匹配任何空白字符，包括空格、制表符、换页符等，等价于[\f\n\r\t\v]
\S      #匹配任何非空白字符，等价于[^\f\n\r\t\v]
\t      #匹配一个制表符
\w      #匹配包括下划线的任何单词字符，等价于"[A-Za-z0-9]"
\W      #匹配任何非单词字符，登记于"[A-Za-z0-9]"


"""
import re
import sys
def DealWithFunc(s):
    r = re.compile(r'''
                   (?<=def\s)               #前边必须含有def且def后跟一个空格
                   \w+                      #匹配函数名
                   \(.*?\)                  #匹配参数
                   (?=:)                    #后边必须跟一个：
                   ''',re.X | re.U)         #设置编译选项，忽略模式中的注释
    return r.findall(s)


def DealWithVar(s):
    vars = []                       #定义一个列表，分两种情况处理
    r = re.compile(r'''
                    \b              #匹配单词开始
                    \w+             #匹配变量名
                    (?=\s=)         #处理为变量赋值的情况
                    ''',re.X | re.U)
    vars.extend(r.findall(s))
    r = re.compile(r'''
                    (?<=for\s)      #处理变量位于for语句中的情况
                    \w+             #匹配变量名
                    \s              #匹配空格
                    (?=in)          #匹配in
                    ''',re.X|re.U)  #设置编译选项，忽略模式中的注释
    vars.extend(r.findall(s))
    return vars

if len(sys.argv) ==1:           #判断命令行是否有输入，没有则要求输入要处理的文件
    sour = input("请输入要处理的文件路径：")
else:
    sour = sys.argv[1]

file = open(sour,encoding="utf-8")  #打开文件
s = file.readlines()        #将文件读入到s中
file.close()
print("*"*100)
print(sour, "中的函数有: ")
print("*"*100)
i = 0           #i为函数所在的行号
#循环处理每一行，匹配函数并输出函数所在的行号，以及函数的原型
for line in s:
    i +=1
    function = DealWithFunc(line)
    if len(function) == 1:
        print("Line:",i,"\t",function[0])
print("*"*100)
print(sour, '中的变量有：')
print("*"*100)
i = 0
#循环处理每一行，匹配其中的变量，输出变量所在的行号，以及变量名
for line in s:
    i +=1
    var = DealWithVar(line)
    if len(var) ==1:
        print("Line:", i, '\t', var[0])

