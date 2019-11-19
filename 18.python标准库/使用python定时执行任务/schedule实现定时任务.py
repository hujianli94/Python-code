#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/12 12:39
# filename: schedule实现定时任务.py

import schedule
import time
import datetime


def job():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("I'm working...")


schedule.every().second.do(job)
schedule.every(20).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
