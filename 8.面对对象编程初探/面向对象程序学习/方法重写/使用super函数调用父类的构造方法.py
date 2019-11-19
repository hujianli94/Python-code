#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/13 23:17
# filename: 使用super函数调用父类的构造方法.py
class Employee:
    def __init__(self, salary):
        """
        父类构造方法
        :param salary:员工工资
        """
        self.salary = salary

    def work(self):
        print("我是胡建力，我的工资是:【{}】".format(self.salary))


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print("我是一名顾客，我的职业是:【{}】，我的地址是:【{}】".format(self.favorite, self.address))


class Manager(Employee, Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print("-------- Manager的构造方法 ------------")
        # super().__init__(salary)
        super(Manager, self).__init__(salary)
        Customer.__init__(self, favorite, address)


if __name__ == '__main__':
    # 创建Manager对象
    m = Manager(25000, "IT产品", "北京")
    m.work()
    m.info()
