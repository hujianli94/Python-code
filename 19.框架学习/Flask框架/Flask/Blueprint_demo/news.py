#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/23 22:04
# filename: news.py
from flask import Blueprint

news_bp = Blueprint('new', __name__, url_prefix='/news')


@news_bp.route("/list")
def news_list():
    return "新闻列表"


