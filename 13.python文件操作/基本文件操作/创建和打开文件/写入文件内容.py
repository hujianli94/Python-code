#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
print('\n','='*10,'蚂蚁庄园动态','='*10)
file = open('messages1.txt','a',encoding='utf-8')
file.write("this is message txt\ntest!\n")
print('\n写入了一条动态......\n')
file.flush()
file.close()
'''

list1 = ['姚明','博尔特','姆巴佩','张艺龄']
list2 = [i + '\n' for i in list1]
with open('message2.txt','w') as file:
    file.writelines(list2)
