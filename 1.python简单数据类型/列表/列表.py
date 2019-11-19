#!/usr/bin/env python
# -*- coding:utf8 -*-
lsit1 = ["a", 1, "b", 2.0]
print(lsit1[1])     #1
print(lsit1[2])     #b
print(lsit1[-2])    #b
print(lsit1[::-1])  # 反转列表      [2.0, 'b', 1, 'a']

lsit2 = [3, 4, 5, 6]
print(lsit1 + lsit2)        #['a', 1, 'b', 2.0, 3, 4, 5, 6]

lsit3 = ["python"]
print(lsit3 * 3)            #['python', 'python', 'python']

print("apped()".center(100, "#"))
alst = [1, 2, 3, 4, 5]
alst.append("hu")
print(alst)                 # [1, 2, 3, 4, 5, 'hu']

print("count()".center(100, "#"))
print(alst.count(1))                    #1

print("在列表后追加另一个列表".center(100, "#"))
alst.extend(["1", "哈哈"])
print(alst)                         # [1, 2, 3, 4, 5, 'hu', '1', '哈哈']
print("查找列表中出现的下标".center(100, "#"))
print(alst.index(2))                    # 1

print("在下标处插入元素".center(100, "#"))
alst.insert(2, "hu")
print(alst)                 #[1, 2, 'hu', 3, 4, 5, 'hu', '1', '哈哈']

print("返回删除的列表元素，最后一个".center(100, "#"))
pop_num = alst.pop()
print(pop_num)              # 哈哈
print(alst)                 # [1, 2, 'hu', 3, 4, 5, 'hu', '1']

print("删除列表的元素2".center(100, "#"))
alst.remove(2)
print(alst)                 # [1, 'hu', 3, 4, 5, 'hu', '1']

print("反转列表，颠倒".center(100, "#"))
alst.reverse()
print(alst)                     # ['1', 'hu', 5, 4, 3, 'hu', 1]

alst1 = [6, 2, 3, 4, 5]
print("对列表进行排序".center(100, "#"))
alst1.sort()
print(alst1)                    #[2, 3, 4, 5, 6]
