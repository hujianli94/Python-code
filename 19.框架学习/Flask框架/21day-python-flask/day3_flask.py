#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/25 16:58
# filename: day3_flask.py
import flask

html_txt = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <body>
    <h2>  收到GET请求 </h2>
    <form method='post'>        
        <input type="submit" value="发送POST请求" />
    </form>
</head>

</body>
</html>

"""
app = flask.Flask(__name__)  # 实例化主类Flask


@app.route("/route", methods=["GET", "POST"])
def hello():  # 定义业务函数
    if flask.request.method == "GET":  # 判断收到的请求是否为GET
        return html_txt
    else:
        return "收到POST请求，我是Flask"


@app.route("/hello/<name>")
def hello2(name):
    return "你好, " + name + "!"


if __name__ == '__main__':
    app.run(debug=True)
