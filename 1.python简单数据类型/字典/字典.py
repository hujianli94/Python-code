#!/usr/bin/env python
#-*- coding:utf8 -*-
ab = { 'Swaroop': 'swaroopch@byteofpython.info','Larry' : 'larry@wall.org'}
ab['c'] = 80
print(ab)
del ab['c']
print(ab)

li = ["a","b","c"]
print(dict(enumerate(li)))

#定义字典
word = {"che":"车","chen":"陈","cheng":"称","chi":"吃"}
print(word)

key = ["che","chen","cheng","chi"]  #定义索引列表
vlaue = ["车", "陈","称","吃"]      #定义汉字列表
zip1 = dict(zip(key,vlaue))         #将对象转换为字典
print(zip1)
print(zip1["che"])
print(zip1.get("chen"))             #键存在，返回值
print(zip1.get("chenj"))            #键不存在，返回None
print(zip1.get("chene","查无此人"))       #键不存在，返回默认值


dict1 = {}
#dict1.fromkeys()
name = ["hujianli","jianli","xiaojian","jianlihu"]
dictionary = dict.fromkeys(name)        #创建一个只有键的字典
print(dictionary)


#del dictionary             #删除字典

dictionary.clear()  #清除字典当中的所有元素，变成一个空字典
print(dictionary)


#遍历字典的键和值
dic2 = {"依梦":"水瓶座","胡建力":"巨蟹座","小健":"狮子座"}
"""
dic2.items()
"""
#遍历键和值
for key1, vlaue1 in dic2.items():
    print(key1,'=====>',vlaue1)

#遍历键
for key1 in dic2.keys():
    print("key is {}".format(key1))

#遍历值
for vlaue in dic2.values():
    print("value is {}".format(vlaue))


hu1 = list(zip(['a','b','c'],[1,2,3]))
print(hu1)

hu2 = dict(zip(['a','b','c'],[1,2,3]))
print(hu2)


