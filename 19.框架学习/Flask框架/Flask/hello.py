#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/23 20:44
# filename: hello.py
from flask import Flask, redirect,render_template


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!你好啊，小健"


@app.route("/hujianli")
def index():
    return "This is index! ......"


# 匹配任意的数据类型，http://127.0.0.1:5000/user/XXX
@app.route("/user/<username>")
def user_login(username):
    return "Hello {}".format(username)


# 只匹配整数型 http://127.0.0.1:5000/post/123，输入字符串会报错
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post:{}".format(post_id)


@app.route("/huxiaojian")
def index3():
    return redirect("http://www.baidu.com")


@app.route("/user/<username>")
def user_login(username):
    # 显示该用户的信息
    mydic = {"key1": 1111, "key2": 22222}
    return render_template("user.html", name=username, dic=mydic)


if __name__ == '__main__':
    app.debug = True
    app.run()

