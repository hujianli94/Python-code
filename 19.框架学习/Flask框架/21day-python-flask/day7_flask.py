#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/25 17:38
# filename: day7_flask.py
from flask import render_template
from flask import Flask

app = Flask(__name__)

app.route("/photo")


def hello2():
    return render_template("index.html")  # 渲染index.html文件


if __name__ == '__main__':
    app.run(debug=True)
