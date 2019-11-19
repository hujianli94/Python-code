#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/10 16:29
# filename: 内部函数的局部变量互访.py

def foo():
    # 局部变量

    name = "唐三藏"

    def bar():
        nonlocal name
        print(name)
        name = "孙悟空"
        print(name)

    bar()


foo()
