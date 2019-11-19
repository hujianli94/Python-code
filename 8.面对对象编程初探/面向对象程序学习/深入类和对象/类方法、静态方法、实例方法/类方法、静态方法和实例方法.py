#!/usr/bin/env python
# -*- coding:utf8 -*-
class Date():
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法不用写self
    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        # 静态方法不好的地方是采用硬编码，如果用类方法的话就不会了
        return Date(int(year), int(month), int(day))

    # 类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        # cls：传进来的类,而不是像静态方法把类写死了
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return '%s/%s/%s' % (self.year, self.month, self.day)


if __name__ == "__main__":
    new_day = Date(2018, 5, 9)
    # 实例方法
    new_day.tomorrow()
    print(new_day)  # 2018/5/10

    # 静态方法
    date_str = '2018-05-09'
    new_day = Date.parse_from_string(date_str)
    print(new_day)  # 2018/5/9

    # 类方法
    date_str = '2018-05-09'
    new_day = Date.from_string(date_str)
    print(new_day)  # 2018/5/9
