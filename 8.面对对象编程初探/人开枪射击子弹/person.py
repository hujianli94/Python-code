#!/usr/bin/env python
#-*- coding:utf8 -*-
class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def fillBullet(self,count):
        self.gun.bulletBox.bulletCount = count