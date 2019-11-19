#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/28 9:26
# filename: 03.单行刷新版本，进度条.py
import time


def pro_bar(scale):
    print('执行开始'.center(scale // 2, '='))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}] {:.2f}s'.format(c, a, b, dur), end='')
        time.sleep(0.05)
    print('\n' + '执行结束'.center(scale // 2, '='))


pro_bar(50)
