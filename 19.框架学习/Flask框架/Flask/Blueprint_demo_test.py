#!/usr/bin/env python
#-*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/23 22:08
# filename: Blueprint_demo_test.py
from flask import Flask, url_for
from Blueprint_demo.news import news_bp
from Blueprint_demo.user import user_bp

app = Flask(__name__)
# 3.注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)


@app.route("/")
def hello_world():
    return "Hello world"


with app.test_request_context():
    print(url_for('new.news_list'))     # /news/list/   通过url_for反转url的时候要加蓝图的名字
    print(url_for('user.profile'))      # /user/profile/

if __name__ == '__main__':
    app.run(debug=True)