#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
基类 object
class ClassName(基类):
    pass
'''

class Fruit:
    def __init__(self, color='绿色'):
        Fruit.color = color

    def harvest(self,color):
        print('水果是: ', color, '的！')
        print('水果已经收获.....')
        print('水果原来是: ', Fruit.color)    #输出类属性

class Apple(Fruit):
    color = '红色'

    def __init__(self):
        print('我是Apple...')
        # Fruit.__init__(self)
        super().__init__()      #调用基类的构造方法

    def harvest(self,color):
        '''
        方法的重写
        :param color:
        :return:
        '''
        print('苹果！')
        print('苹果已经收获.....')
        print('苹果原来是: ',Fruit.color,'的!')    #输出类属性

class Sapodilla(Fruit):
    def __init__(self,color):
        print('\n我是人参果')
        super().__init__(color)  #调用基类时，传递参数，修改基类的值

    def harvest(self,color):
        print('人参果是：',color,'的！')
        print('人参果已经收获.....')
        print('人参果原来是: ',Fruit.color,'的!')  #输出类属性



apple = Apple()
apple.harvest(apple.color)
print()

Sa = Sapodilla('白色')
Sa.harvest('金黄色带紫色条纹')



