#!/usr/bin/env python
#-*- coding:utf8 -*-
import pickle
class Bird(object):
    have_feather = True
    reproduction_method = "egg"


with open("summer.pk1", "rb") as f:
    summer = pickle.load(f)

print(summer.have_feather)
print(summer.reproduction_method)
