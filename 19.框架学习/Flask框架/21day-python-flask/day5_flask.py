#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/6/25 17:23
# filename: day5_flask.py
import flask

html_txt = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    
</head>
<body>

<h2> 收到GET 请求</h2>
<a href="/get_info"> 获取cookie信息 </a>
</body>
</html>
"""

app = flask.Flask(__name__)


@app.route("/set_info/<name>")
def set_cks(name):
    name = name if name else 'anonymous'
    resp = flask.make_response(html_txt)
    resp.set_cookie("name", name)
    return resp


@app.route("/get_info")
def get_cks():
    name = flask.request.cookies.get("name")  # 获取cookie信息
    return "获取的cookie信息是：" + name


if __name__ == '__main__':
    app.run(debug=True)
