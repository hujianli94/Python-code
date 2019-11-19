#!/usr/bin/env python
#-*- coding:utf8 -*-
import random

#取 10 ~20 之间的3个随机数
for i in range(3):
    a = random.randrange(10,20)
    print(a,end=" ")


if __name__ == '__main__':
    checkcode = ''      #保存验证码的变量
    for i in range(4):
        index = random.randrange(0,4)               #生成一个0~3中的一个数
        if index != i and index +1 !=i:
            checkcode += chr(random.randint(97, 122))        #生成A~Z中的一个小写字母
        elif index +1 ==i:
            checkcode  += chr(random.randint(65, 90))         #生成A~Z中的一个大写字母
        else:
            checkcode += str(random.randint(1, 9))            #生成1~9中的一个数字

    print(checkcode)