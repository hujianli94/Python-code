#!/usr/bin/env python
#-*- coding:utf8 -*-


def fun_bmi(name,height,weight):
    '''
    :param name:
    :param height:
    :param weight:
    :return:根据身高和体重计算bmi指数
    '''
    print(name + "的身高" + str(height) + "米\t 体重："+ str(weight) + "千克")
    bmi = weight/(height*height)        #计算BMI指数，公式为: "体重/身高的平方"
    print("您的BMI指数为：" + str(bmi))   #输出BMI指数
    #check身材是否合理

    if bmi < 18.5:
        print("您的体重过轻~~~@_@")
    if bmi >=18.5 and bmi <24.9:
        print("正常范围，注意保持...")
    if bmi >=24.9 and bmi <29.9:
        print("您的体重过重!!~~@_@~")
    if bmi>29.9:
        print("@_@肥胖。")

fun_bmi("路人甲",weight=60,height=1.83)          #关键字参数
print("".center(100,"="))
fun_bmi(weight=50,height=1.60,name="路人乙")

def mult_test(a,b,c):
    return a*b*c

print(mult_test(2,c=5,b=3))