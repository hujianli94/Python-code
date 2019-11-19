#!/usr/bin/env python
#-*- coding:utf8 -*-
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

print(__name__)     #在自身执行时__name__的值为__main__,外部调用时__name__的值为程序名称

if __name__ == '__main__':
    #函数体外
    print('\n下雪了.....\n')
    print("="*15, '开始做梦.....', '='*15)
    fun_christmastree()  #调用函数
    print("="*15, '梦醒了.....', '='*15)

    pinetree = '我身上落满雪花, ' + pinetree + '-_-'