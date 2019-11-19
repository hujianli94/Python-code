#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
构造方法
__init__
'''
class Geeese:
    '''
    大雁类,类名采用首字母大写，驼峰式约定俗成定义法
    '''
    #属性
    #方法
    def __init__(self,beak,wing,claw):
        '''
        :return:可以访问类的属性和方法
        '''
        self.beak = beak
        print("我是大雁类,我有以下特征: ")
        print(beak)     #喙
        print(wing)     #翅膀
        print(claw)     #爪子


beak_1 = "喙的基部较高，长度和头的长度几乎相等"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是噗状的"
widGoose = Geeese(beak_1, wing_1, claw_1)     #创建大雁类的实例
# widGoose1 = Geeese()    #创建第二个实例
# print(widGoose)
# print(widGoose1)

print()
'''
 getattr():返回一个对象属性或方法。
 hasattr():判断一个对象是否具有属性或方法。返回一个布尔值。
 setattr():给对象属性重新赋值或添加。如果属性不存在则添加，否则重新赋值。
 delattr()：删除对象属性。
'''
print("getattr".center(100,"-"))
print(getattr(widGoose,"beak","nothing"))
print(getattr(widGoose,"beak1","nothing"))
print("hasattr".center(100,"-"))
print(hasattr(widGoose,"aa"))
print(hasattr(widGoose,"beak"))
print("setattr".center(100,"-"))
setattr(widGoose,"age",22)
setattr(widGoose,"beak","吃零食")
print(widGoose.__dict__)
print("delattr".center(100,"-"))
delattr(widGoose,"age")
print(widGoose.__dict__)
