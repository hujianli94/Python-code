#!/usr/bin/env python
# -*- coding:utf8 -*-
def pre_str(pre=''):
    def decorator(old_function):
        def new_function(a, b):
            print("*" * 30)
            print(pre + ' input', "用户名:", a)
            print(pre + ' input', "密码:", b)
            print("*" * 30)
            return old_function(a, b)

        return new_function

    return decorator


# 不带参数，默认值参数
@pre_str()
def sum_str(a, b):
    return a, b


# 装饰square_sum()，带参数^_^
@pre_str("^_^")
def square_sum(a, b):
    return a, b


# 装饰器square_diff(),带参数T_T
@pre_str("T_T")
def square_diff(a, b):
    return a, b


if __name__ == '__main__':
    print(sum_str("xiaojian722", "admin#123"))
    print(square_sum("hujianli", "123.com"))
    print(square_diff("hujianli", "1234.com"))
