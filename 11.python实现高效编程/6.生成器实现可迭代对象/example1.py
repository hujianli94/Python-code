#!/usr/bin/env python
#-*- coding:utf8 -*-
class PrimeNumbers:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def isPrimeNum(self,k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isPrimeNum(k):
                yield k

if __name__ == '__main__':
    nu = 0  #计数器
    for i in PrimeNumbers(1,200):
        print(i)
        nu +=1

    print("found number:",nu)

