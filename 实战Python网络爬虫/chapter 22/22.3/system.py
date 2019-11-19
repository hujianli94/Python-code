from flask import Flask, request
app = Flask(__name__)
# app.route设置URL路径，methods是请求方式
# hello_world视图函数
@app.route('/', methods=['POST','GET'])
def hello_world():
    # 判断请求方式，返回不同结果
    # POST请求
    if request.method == 'POST':
        return "This is Post,your post data is " + request.form['Python']
    # GET请求
    else:
        return 'Hello World!'
# 系统启动运行
if __name__ == '__main__':
    app.run()
