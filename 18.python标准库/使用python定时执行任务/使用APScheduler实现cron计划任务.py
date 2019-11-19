#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/1 13:09
# filename: 使用APScheduler实现cron计划任务.py
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    """
    # hour = 19, minute = 23 这里表示每天的19：23分执行任务。
    hour =19 , minute =23
    hour ='19', minute ='23'
    minute = '*/3' 表示每 5 分钟执行一次
    hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务
    """
    scheduler.add_job(tick, 'cron', hour=19, minute=23)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
