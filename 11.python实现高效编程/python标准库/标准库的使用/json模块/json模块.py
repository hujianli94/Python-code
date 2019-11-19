#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
JSON通常用于在Web客户端和服务器数据交换，即把字符串类型的数据转换成Python基本数据类型或者将Python基本数据类型转换成字符串类型。

常用方法
方法	说明
json.loads(obj)	将字符串序列化成Python的基本数据类型，注意单引号与双引号
json.dumps(obj)	将Python的基本数据类型序列化成字符串
json.load(obj)	读取文件中的字符串，序列化成Python的基本数据类型
json.dump(obj)	将Python的基本数据类型序列化成字符串并写入到文件中
'''
dict_str = '{"k1":"v1","k2":"v2"}'
print(type(dict_str))

import json
dict_json = json.loads(dict_str)
print(dict_json)
print(type(dict_json))

#将一个列表类型的变量序列化成字符串类型
json_li = [11,22,33,44]
print(type(json_li))

#将字符串类型转换为Python的基本数据类型
json_str = json.dumps(json_li)
print(type(json_str))
print(json_str)

#把字典当作字符串存入db文件当中
dic = {"k1":123,"k2":456}
print(type(dic),dic)

import json
# 将dic转换为字符串并且写入到当前目录下面的db文件内，如果没有该文件则创建
json.dump(dic,open("db","w"))

#读取当前目录下面的db文件，把内容转换为Python的基本数据类型并赋值给result
result = json.load(open('db','r'))
print(type(result))
print(result)


