#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/6 12:11
# filename: 04.使用辅助函数取代复杂的表达式.py

my_values = {'red': ['5'], 'green': [''], 'blue': ['0']}


# print(my_values)
# red = my_values.get('red', [''])[0] or 0
# green = my_values.get('green', [''])[0] or 0
# opicaty = my_values.get('opacity', [''])[0] or 0
# print("Red: {}".format(red))
# print("Green: {}".format(green))
# print("Opicaty: {}".format(opicaty))


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opicaty = get_first_int(my_values, 'opicaty')
print("Red: {}".format(red))
print("Green: {}".format(green))
print("Opicaty: {}".format(opicaty))
