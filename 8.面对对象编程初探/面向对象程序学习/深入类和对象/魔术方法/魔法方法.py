#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
和比较相关的魔术方法
__eq__(self, other) self == other
__ne__(self, other) self != other
__lt__(self, other) self < other
__gt__(self, other) self > other
__le__(self, other) self <= other
__ge__(self, other) self >= other

和数学相关的魔术方法
__add__(self, other) self + other
__sub__(self, other) self - other
__mul__(self, other) self * other
__floordiv__(self, other) self // other
__truediv__(self, other) self / other
__mod__(self, other) self % other
__pow__(self, other) self ** other
'''

class Word():
    def __init__(self,text):
        self.text = text

    # def __eq__(self, other):
    #     if self.text.lower() == other.lower():
    #         print("True")
    #     else:
    #         print("False")

    def __add__(self, other):
        if isinstance(self.text, int):
            return self.text + other
        else:
            return False

    # def __str__(self):
    #     return self.text

    def __repr__(self):
        return 'Word("self.text")'

first = Word(10)
first.__eq__(10)
print(first)

add = first.__add__(20)
print(add)