#!/usr/bin/env python
#-*- coding:utf8 -*-
import requests
from collections import Iterable,Iterator


# 气温迭代器
class WeatherIterator(Iterator):
    # 定义构造器，返回哪些城市的天气（城市名字字符串列表）
    def __init__(self,cities):
        self.cities = cities
        # 记录迭代位置
        self.index = 0
    def getWeather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s' % (city,data['low'],data['high'])
    # next调用getWeather方法
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        # 迭代完毕，抛出异常
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

# 可迭代对象
class WeatherIterable(Iterable):
    # 定义构造器
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable([u'北京',u'上海',u'保定',u'湘潭']):
    # x就是getWeather return的结果
    print(x)
