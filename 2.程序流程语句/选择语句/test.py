#!/usr/bin/env python
#-*- coding:utf8 -*-
print("\n 为了您和家人的安全，请不要酒后开车\n")
var1=int(input("请输入每100毫升血液中的酒精含量度数："))

if var1 <20:
    print("您的血液中酒精含量为:{},可以开车，建议找个代驾。".format(var1))
else:
    if 80 >= var1 >=20:
        print("您血液中酒精含量为{},已经超标，不要开车，谢谢！".format(var1))
    else:
        print("您血液中酒精含量为{},请不要开车....严重超标。".format(var1))