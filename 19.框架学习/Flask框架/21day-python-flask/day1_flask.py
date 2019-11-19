#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/25 16:48
# filename: day1_flask.py
import flask            # 导入flask
app =flask.Flask(__name__)      # 实例化主类Flask


@app.route("/")     #装饰器（实现URL地址）
def hello():
    return "你好，我是flask！"



if __name__ == '__main__':
    app.run(debug=True)