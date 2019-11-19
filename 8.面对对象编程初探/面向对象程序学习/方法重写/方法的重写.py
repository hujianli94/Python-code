#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
class ClassName(基类):
    pass
'''

class Fruit:
    color = '绿色'    #类属性

    def harvest(self,color):
        print('水果是: ', color, '的！')
        print('水果已经收获.....')
        print('水果原来是: ', Fruit.color)    #输出类属性

class Apple(Fruit):
    color = '红色'

    def __init__(self):
        print('我是Apple...')

    def harvest(self,color):
        '''
        方法的重写
        :param color:
        :return:
        '''
        print('苹果！')
        print('苹果已经收获.....')
        print('苹果原来是: ', Fruit.color)    #输出类属性

class Orange(Fruit):
    color = '橙色'

    def __init__(self):
        print('我是Orange...')

    def harvest(self,color):
        '''
        方法的重写
        :param color:
        :return:
        '''
        print('橘子！')
        print('橘子已经收获.....')
        print('橘子原来是: ', Fruit.color)    #输出类属性

apple = Apple()
apple.harvest(apple.color)
print()
orange = Orange()
orange.harvest(orange.color)


