#!/usr/bin/env python
#-*- coding:utf8 -*-
def fun_demo():
    '''
    局部变量
    :return:
    '''
    message = '唯有在被追赶的时候，你才能真正的奔跑。'
    print('局部变量message=',message)

fun_demo()  #调用函数
#print('局部变量message=',message)      #报错，函数体外，变量不生效
print()

#全局变量
message = '唯有在被追赶的时候，你才能真正的奔跑。'
def fun_demo():
    '''
    局部变量
    :return:
    '''
   # message = '唯有在被追赶的时候，你才能真正的奔跑。'
    print('函数体内：全局变量message=', message)


fun_demo()
print("函数体外，全局变量message=",message)
print()
print(" global 来修改全局变量 ".center(100,"*"))
message = '唯有在被追赶的时候，你才能真正的奔跑。'
def fun_demo():
    '''
    局部变量
    :return:
    '''
    global message
    message = '失望之酒，希望之杯.....'
    print('函数体内：全局变量message=', message)

fun_demo()
print("函数体外:全局变量message=",message)


print()
print(" 模拟松树做梦 ".center(100,"*"))
pinetree = '我是一棵松树' #全局变量(松树)
def fun_christmastree():    #定义一个函数
    '''
    功能；一个梦，无返回值
    :return:
    '''
    pinetree = '挂上彩灯、礼物....我编程一颗圣诞树@~@\n' #定义一个局部变量
    print(pinetree)
#函数体外
print('\n下雪了.....\n')
print("="*15, '开始做梦.....', '='*15)
fun_christmastree()  #调用函数
print("="*15, '梦醒了.....', '='*15)

pinetree = '我身上落满雪花, ' + pinetree + '-_-'
print(pinetree)


