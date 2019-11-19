#!/usr/bin/env python
#-*- coding:utf8 -*-
s = 'spammy'
S = s[:3] + 'xx' + s[5:]
print(S)

print(s.replace('mm','xx'))

hu = 'aa$bb$cc$dd'.replace('$', 'SPAM')
print(hu)

S = 'xxxxSPAMxxxxSPAMxxxx'

where = S.find("SPAM")
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)


S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace("SPAM","EGGS",1))
