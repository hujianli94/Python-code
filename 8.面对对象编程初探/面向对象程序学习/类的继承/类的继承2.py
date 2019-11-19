#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 17:53
# filename: 类的继承2.py
class Employee:
    def __init__(self,salary):
        self.salary = salary

    def work(self):
        print("普通员工正在写代码,工资是：",self.salary)

class Customer:
    def __init__(self,favorite,address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print("我是一个顾客，我的爱好是：{},地址是：{}".format(self.favorite,self.address))


class Manager(Employee,Customer):
    #重写父类的构造方法
    def __init__(self,salary,favorite,address):
        print("--------Manager的构造方法------------")
        #通过super()函数调用父类的构造方法
        super(Manager, self).__init__(salary)
        #同上面的效果一样
        # super().__init__(salary)
        Customer.__init__(self,favorite, address)

if __name__ == '__main__':
    m = Manager(25000,"IT产品","深圳")
    m.work()
    m.info()