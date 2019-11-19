#!/usr/bin/env python
#-*- coding:utf8 -*-
import time
def make(label):
    def echo(message):
        print(label + ':' + message)
    return echo


F = make("So")
F("hello.....")
time.sleep(2)
F("goodbye.....")
