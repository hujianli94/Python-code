#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
如果参数名前加上一个星号，* 表示该餐是一个可变长参数。如果依次将所有的其他变量都赋予值之后，剩下的参数将会收集在
一个元祖中，元祖的名称就是前面带星号的参数名
'''

def change_para_num(*tpl):
    print(type(tpl))
    print(tpl)

change_para_num(1)
change_para_num(1, 2, 3)
print("演示一个同时有三种类型的参数的函数定义及调用".center(100,"*"))
def change_para_mum2(*tpl,a,b=0):
    print("tpl:",tpl)
    print("a:",a)
    print("b:",b)

change_para_mum2(1,2,3,a=5)

#定义了收集关键字参数的示例
def change_para_dct(a,b=0,**adct):
    print("adct:",adct)     #收集关键字参数到字典中，多余的关键字参数，运行时会被放入adct字典中
    print("a:",a)
    print("b:",b)

change_para_dct(1,k=3,b=2,c=3)
