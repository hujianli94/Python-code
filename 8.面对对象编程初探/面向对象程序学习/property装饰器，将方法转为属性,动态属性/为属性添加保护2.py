#!/usr/bin/env python
#-*- coding:utf8 -*-

#通过装饰器方法来获取私有属性
class TVShow:       #电视节目类
    list_film = ["战狼2", "红海行动", "西游记女儿国", "熊出没变形记"]

    def __init__(self, show):
        self.__show = show      ## 私有的实例属性

    @property
    def show(self):
        '''
        :return:私有属性
        '''
        return self.__show      #返回类的实例


    @show.setter                #让属性可以进行修改
    def show(self, value):
        if value in TVShow.list_film:       #判断值是否在列表中
            self.__show = '您选择了《'+ value + "》,稍后将播放"    #修改返回值
        else:
            self.__show = "您点播的电影不存在"


tvshow = TVShow("战狼2")  #创建类的实例
print("正在播放:《", tvshow.show, "》")     #获取属性值
print("您可以从", TVShow.list_film, "中选择台点播的电影")

tvshow.show = '红海行动'
print(tvshow.show)      #获取属性值













'''
tvshow = TVShow("正在播放《战狼2》")  #创建类的实例
print("默认输出: ", tvshow.show)     #获取属性值

'''




#修改装饰器的值会报错
'''
tvshow.show = "正在播放《红海行动》"
print("默认输出: ", tvshow.show)     #获取属性值
'''
