#!/usr/bin/env python
#-*- coding:utf8 -*-

class Complex(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "Complex(%s, %s)" %(self.real,self.imag)

    def __str__(self):
        return "(%g+%gj)" %(self.real,self.imag)

    #self + other
    def __add__(self, other):
        return Complex(self.real + other, self.imag + other)
    #self - other
    def __sub__(self, other):
        return Complex(self.real - other, self.imag - other)

if __name__ == '__main__':
    c = Complex(4, 2)
    print(c)

















