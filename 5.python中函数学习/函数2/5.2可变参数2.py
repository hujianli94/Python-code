#!/usr/bin/env python
#-*- coding:utf8 -*-
def fun_bmi(*name):
    '''
    :param name:
    :param height:
    :param weight:
    :return:根据身高和体重计算bmi指数
    '''
    for item in name:
        for args1 in item:
            name = args1[0]
            height = args1[1]
            weight = args1[2]
            print(name + "的身高" + str(height) + "米\t 体重："+ str(weight) + "千克")
            bmi = weight/(height*height)        #计算BMI指数，公式为: "体重/身高的平方"
            print("您的BMI指数为：" + str(bmi))   #输出BMI指数
            #check身材是否合理
            print()

            if bmi < 18.5:
                print("您的体重过轻~~~@_@")
            if bmi >=18.5 and bmi <24.9:
                print("正常范围，注意保持...")
            if bmi >=24.9 and bmi <29.9:
                print("您的体重过重!!~~@_@~")
            if bmi>29.9:
                print("@_@肥胖。")

list1 = [["hujianli",1.79,65], ['huxiaojian',1.78,90], ['jianli',1.81,100]]
fun_bmi(list1)