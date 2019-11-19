#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 15:17
# filename: 类中定义内部类.py
class Car:
    class Door:
        def open(self):
            print("open door....")

    class Wheel:
        def run(self):
            print("car run")


if __name__ == '__main__':
    car = Car()         #实例化car
    backDoor = car.Door()       #内部类的实例化1
    frontDoor = car.Door()       #内部类的实例化2
    backDoor.open()
    frontDoor.open()

    wheel = car.Wheel()
    wheel.run()
