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
    flask.session["name"] = name
    return html_txt


@app.route("/get_info")
def get_cks():
    name = "name" in flask.session and flask.session['name']    #获取session
    if name:
        return "获取的回话信息是：" + name
    else:
        return "没有相应回话信息"


if __name__ == '__main__':
    app.secret_key = 'sdadajasgfajsgasjgdajgasgasahsuq$$#$%^'
    app.run(debug=True)
