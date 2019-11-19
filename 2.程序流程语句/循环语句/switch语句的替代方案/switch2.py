#!/usr/bin/env python
#-*- coding:utf8 -*-

class switch(object):
  def __init__(self, value):
    self.value = value
    self.fall = False

  def __iter__(self):
    """Return the match method once, then stop"""
    yield self.match
    raise StopIteration

  def match(self, *args):
    """Indicate whether or not to enter a case suite"""
    if self.fall or not args:
      return True
    elif self.value in args: # changed for v1.5, see below
      self.fall = True
      return True
    else:
      return False


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = '+'
x = 10
y = 20
for case in switch(v):
    if case('+'):
        print(x+y)
        break
    if case('-'):
        print(x-y)
        break
    if case('*'):
        print(x*y)
        break
    if case('/'):
        print(x/y)
        break
    if case():      #do nothing
        print()
        break
