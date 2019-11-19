#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/23 22:04
# filename: user.py
from flask import Blueprint

# 1.定义一个蓝图，'user':蓝图的名字,url_prefix='/user'：给url加一个前缀，注意后面不要加'/'
user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route("/profile")
def profile():
    return "个人中心"