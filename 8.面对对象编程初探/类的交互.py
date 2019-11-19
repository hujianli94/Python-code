#!/usr/bin/env python
# -*- coding:utf8 -*-
class Garen:
    camp = 'Demacia'

    def __init__(self, name, aggressivity=58, life_value=455):  # 初始攻击力和生命值
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):  # 普通攻击技能，攻击敌人
        enemy.life_value -= self.aggressivity  # 根据攻击力，减掉敌人生命值


class Riven:
    camp = 'Noxus'

    def __init__(self, name, aggressivity=54, life_value=4514):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


g1 = Garen('盖伦')
r1 = Riven("瑞文")

print(g1.life_value)
r1.attack(g1)  # 交互
print(g1.life_value)
