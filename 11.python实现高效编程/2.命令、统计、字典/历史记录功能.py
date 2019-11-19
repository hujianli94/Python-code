#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
#使用双端队列deque
from collections import deque
q = deque([],5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
'''

#导入随机数模块
from random import randint
#导入双端队列模块
from collections import deque
import pickle               #序列化文件

N = randint(0, 100)         #生成1-100之间的随机数
history = deque([], 10)      #定义双端队列history，最大值是5
History_file = "history.txt"

def guess(k):
    if k == N:
        print("right")
        return True
    if k < N:
        print("{} is less than N ".format(k))
    else:
        print("{} is greater than N".format(k))
    return False

while True:
    line = input("Please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)               #先将输入添加到队列中，用于历史查询
        eval('pickle.dump(history, open(History_file, "wb"))')
        if guess(k):                    #调用函数进行判断k的值
            break
    elif line == "history" or line == "h?":             #如果输入的是history或者输入的是h？ 则打印列表的历史记录
        file_info = pickle.load(open(History_file, "rb"))
        info = [str(x) for x in file_info]
        info = ",".join(info)
        print("您的最后10条历史输入为 ==>: {}".format((info)))
    else:
        print("您输入有误...请输入数字!")
