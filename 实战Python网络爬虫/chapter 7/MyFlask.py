from flask import Flask
# 创建一个Flask实例
app = Flask(__name__)

# 设置路由，即url
@app.route('/')
# url对应的函数
def hello_world():
    # 返回的页面
    return 'Hello World!'

# 程序运行
if __name__ == '__main__':
    app.run()
