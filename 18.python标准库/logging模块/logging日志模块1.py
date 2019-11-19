#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/10/25 20:19
# filename: logging日志模块1.py
import logging

logging.basicConfig(level=logging.ERROR)  # 设置日志级别
logger = logging.getLogger(__name__)

logger.debug("this is debug.........")
logger.info("this is info .........")
logger.warning("this is warning......")
logger.error("this is error......")
logger.critical("this is critical.......")
