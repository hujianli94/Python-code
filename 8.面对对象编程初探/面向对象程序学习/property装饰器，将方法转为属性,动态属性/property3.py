#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 18:08
# filename: property3.py
class Cell:

    # 使用@property修饰方法，相关与设置getter方法

    @property
    def state(self):
        return self._state

    # 为state属性设置setter方法
    @state.setter
    def state(self, value):
        if "alive" in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    # 为is_dead属性设置getter方法
    # 只有getter方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell()

# 修改state属性
c.state = 'Alive'

# 访问state属性
print(c.state)

# 访问is_dead属性
print(c.is_dead)
