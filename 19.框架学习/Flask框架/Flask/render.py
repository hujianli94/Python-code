#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/19 15:47
# filename: render.py
from flask import Flask,render_template

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

@app.route('/')
def hello_world():
    context = {
        'age':20,
        'users':['tom','jack','alice'],
        'person':{
            'name':'hujianli',
            'age':18
        }
    }
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)