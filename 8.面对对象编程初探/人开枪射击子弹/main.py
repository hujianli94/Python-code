#!/usr/bin/env python
#-*- coding:utf8 -*-
from time import sleep
import sys
from person import Person
from gun import Gun
from bulletbox import BulletBox

#弹夹
bulletBox = BulletBox(5)

#枪
gun = Gun(bulletBox)

#人
per = Person(gun)

def viewBar(i):
    """
    进度条效果
    :param i:
    :return:    """
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\r开始射击...biu、biu、biu ----->:%.0f%%' % count)
    output.flush()






#人开火
per.fire()
viewBar(10)
per.fire()
viewBar(10)
per.fire()
viewBar(10)
per.fire()
viewBar(10)
per.fire()
viewBar(10)
per.fire()
viewBar(10)
per.fire()
print()
print("开始上子弹到枪中........")
per.fillBullet(10)
per.fire()




