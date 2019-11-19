#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/5/21 16:37
# filename: logging读取配置文件.py
import logging
import logging.config

logging.config.fileConfig("logger.conf")        #配置信息从文件logger.conf中读取
logger = logging.getLogger("logger1")           #从配置文件中读取logger1配置信息创建日志器

logger.debug("这是DEBUG级别信息")
logger.info("这是INFO级别信息")
logger.warning("这是WARNING级别信息")
logger.error("这是ERROR级别信息")
logger.critical("这是CRITICAL级别信息")


def funlog():
    logger.info("进入funlog函数")


logger.info("调用funlog函数。")
funlog()
