#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/29 10:27
# filename: 异常处理0001.py
import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")

except ValueError:
    print("Caught a  ValueError")

except TypeError:
    print("Caught a TypeError")

except Exception as e:
    print("Caught some other error :%s" % (e.__class__.__name__))

else:
    print("This code called if there is no exception")

finally:
    print("This code called is always called")

