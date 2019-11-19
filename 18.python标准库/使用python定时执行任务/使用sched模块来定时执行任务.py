#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/20 16:35
# filename: 使用sched模块来定时执行任务.py
import time, os
import sched

schedule = sched.scheduler(time.time, time.sleep)


def execute_command(cmd, inc):
    os.system(cmd)
    schedule.enter(inc, 0, execute_command, (cmd, inc))


def main(cmd, inc):
    schedule.enter(0, 0, execute_command, (cmd, inc))
    schedule.run()


if __name__ == '__main__':
    main("netstat -an", 10)
