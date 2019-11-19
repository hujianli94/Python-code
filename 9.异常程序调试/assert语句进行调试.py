#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
assert expression [,reason]
断言操作
'''

def division():
    '''
    功能:分苹果
    :return:
    '''
    print("\n ==========================分苹果了=================")
    apple = int(input('请输入苹果的个数：'))
    children = int(input("请输入小朋友的人数："))
    assert apple > children, '苹果不够分'
    result = apple//children
    remain = apple-result*children
    if remain>0:
        print("{}个苹果，平均分给{}个小朋友，每个人分{}个，剩下{}个".format(apple,children,result,remain))
    else:
        print("{}个苹果，平均分给{}个小朋友，每人分{}个".format(apple,children,result))

if __name__ == '__main__':
    try:
        division()      #调用分苹果函数
    except Exception as e:
        print("输入有误: ",e)













































