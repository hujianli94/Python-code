#!/usr/bin/env python
# -*- coding:utf8 -*-
import datetime

day = datetime.datetime.now().weekday()
mot = ["今天是星期一:\n xxxxxx1",
       "今天是星期二:\n xxxxxx2",
       "今天是星期三:\n xxxxxx3",
       "今天是星期四:\n xxxxxx4",
       "今天是星期五:\n xxxxxx5",
       "今天是星期六:\n xxxxxx6",
       "今天是星期日:\n xxxxxx7"]
print(mot[day])

# print("I am a",\
#       "teach ",\
#       "hekkl",\
#       "dkslds")


print(40, "\t", end="")
print(50, "\t", end="")
print(60, "\t", end="")

print()
print("hello\tworld")
#在普通字符串前面加r，表示字符串是原始字符串，没有转义
print(r"hello \t world")