#!/usr/bin/env python
#-*- coding:utf8 -*-
import threading
def thrfun(x,y):
    for i in range(x,y):
        print(str(i*i)+";")
ta = threading.Thread(target=thrfun,args=(1,6))
tb = threading.Thread(target=thrfun,args=(16,21))
ta.start()
tb.start()
