#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/10 17:42
# filename: 00._thread模块.py
import _thread
from time import sleep
from datetime import datetime

date_time_format = '%Y-%M-%d %H:%M:%S'


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop_one():
    print('+++线程一开始于:{}'.format(datetime.now()))
    print('+++线程一休眠4秒')
    sleep(4)
    print('+++线程一休眠结束，结束于:{}'.format(datetime.now()))


def loop_two():
    print('***线程二开始时间:{}'.format(datetime.now()))
    print('***线程二休眠2秒')
    sleep(2)
    print('***线程二休眠结束，结束时间:{}'.format(datetime.now()))


def main():
    print('------所有线程开始时间:{}'.format(datetime.now()))
    _thread.start_new_thread(loop_one, ())
    _thread.start_new_thread(loop_two, ())
    sleep(6)
    print('------所有线程结束时间:{}'.format(datetime.now()))


if __name__ == '__main__':
    main()
