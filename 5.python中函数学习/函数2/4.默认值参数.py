#!/usr/bin/env python
#-*- coding:utf8 -*-
#默认值参数必须位于所有参数的最后


#默认值参数一定要设置到所有参数的最后！！

def deam(obj=None):   #定义函数，并设置默认值,默认值参数最好为不可变对象
    if obj == None:
        obj = []
        print("形参的值：",obj)
        obj.append(1)
        print("向形参添加参数....")
    print(obj)

deam()

def hello(name='Python'):
    print('你好,{0}!'.format(name))

print("无参数调用时的输出：")
hello()
print("有参数('Jonson')调用时的输出：")
hello("Jonson")

#声明函数时，当有无默认值参数和有默认值参数时，必选先声明无默认值参数，后声明有默认值参数

def hello2(hi='你好',name='Python'):
    print("{0} {1}".format(hi,name))

print("有一个参数（'Jonson'）调用时的输出:")
hello2("Jonson")

print("有二个参数('hi','Jonson')调用时的输出:")
hello2('hi','Jonson')
