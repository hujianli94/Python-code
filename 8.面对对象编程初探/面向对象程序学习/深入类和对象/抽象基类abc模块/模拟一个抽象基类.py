#!/usr/bin/env python
#-*- coding:utf8 -*-
#模拟一个抽象基类

#写一个抽象基类，它的子类必须要重写抽象基类里面的方法
import abc
#定义一个抽象基类
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get(self,key):
        pass

    @abc.abstractclassmethod
    def set(self,key,value):
        pass

#子类,必须有抽象基类里面的方法，get和set
#假入不写set方法会报错

class RedisCache(CacheBase):
    def get(self,key):
        pass

    def set(self,key,value):
        pass

redis_cache = RedisCache()
