#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
1
try:
except 语句

2.
try:
except
else:
语句

3.
try:
except
finally
语句

4.使用raise语句抛出异常

'''


def division():
    '''
    功能:分苹果
    :return:
    '''
    print("\n ==========================分苹果了=================")
    apple = int(input('请输入苹果的个数：'))
    children = int(input("请输入小朋友的人数："))
    if apple < children:
        raise ValueError("苹果太少，不够分")

    result = apple//children
    remain = apple-result*children
    if remain>0:
        print("{}个苹果，平均分给{}个小朋友，每个人分{}个，剩下{}个".format(apple,children,result,remain))
    else:
        print("{}个苹果，平均分给{}个小朋友，每人分{}个".format(apple,children,result))

if __name__ == '__main__':
    try:
        division()      #调用分苹果函数
    except (ZeroDivisionError,ValueError) as e:
        print("输入错误:",e)
    else:
        print("分苹果顺利完成.....")
    finally:
        print("进行了一次分苹果操作")














































