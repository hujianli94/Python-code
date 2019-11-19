#!/usr/bin/env python
#-*- coding:utf8 -*-
"abc"
"123abc"
"abc12*"
"大家"

str2='''
This is function
Return a tuple
'''
print(str2)

print("aaa\nbbb")  #换行符
print("制表符\t制表符*2") #制表符
print("print \r")
print("\\显示\\")
print("单引号\'")
print('双引号\"')

print("字符串运算".center(100,"#"))
print("aaa" + "bbbb")
print("aaa"*3)

print("字符串处理函数".center(100,'#'))
str3 = "beautiful is batter ugly"
print("source string is ",str3)
print("字符串大小写互换\n",str3.swapcase())
print("字符串转大写\n",str3.upper())
print("字符串转小写\n",str3.lower())
print("字符串首字母大写\n",str3.title())
print("字符串首字母是否大写\n",str3.istitle())
print("字符串首字母是否小写\n",str3.islower())
print("字符串的第一个字母大写\n",str3.capitalize())
print("获得字符串字母u的下标\n",str3.find("u"))
print("获得字符串中某一个字母的数量\n",str3.count("u"))
print("将字符串转换为列表，以空格分割\n",str3.split(" "))
print("以空格拼接字符串")
print(" ".join("abcd"))
print("计算字符串的长度\n",len(str3))