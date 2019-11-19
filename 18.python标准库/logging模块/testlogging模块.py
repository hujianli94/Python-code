#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/9/17 9:56
# filename: testlogging模块.py
import logging


class TestLoggiing(object):
    def __init__(self):
        logFormat = '%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s'
        logFileName = './testLog.txt'
        logging.basicConfig(level=logging.INFO, format=logFormat, filename=logFileName, filemode='w')
        logging.debug("debug message")
        logging.info("info message")
        logging.warning("warning message")
        logging.error("error message")
        logging.critical("critical message")


if __name__ == '__main__':
    hu = TestLoggiing()
