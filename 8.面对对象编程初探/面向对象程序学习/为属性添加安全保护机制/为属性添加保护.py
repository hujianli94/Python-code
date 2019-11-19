#!/usr/bin/env python
#-*- coding:utf8 -*-

#通过装饰器方法来获取私有属性
class TVShow:       #电视节目类
    def __init__(self, show):
        self.__show = show

    @property               #属性装饰器，是把类中的方法当做属性来访问
    def show(self):
        '''
        定义方法
        :return:私有属性
        '''
        return self.__show

tvshow = TVShow("正在播放《战狼2》")  #创建类的实例
print("默认输出: ", tvshow.show)     #获取属性值

#修改装饰器的值会报错
'''
tvshow.show = "正在播放《红海行动》"
print("默认输出: ", tvshow.show)     #获取属性值
'''