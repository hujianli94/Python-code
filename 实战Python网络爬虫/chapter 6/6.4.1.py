import requests
url = 'https://www.python.org/static/img/python-logo.png'
r = requests.get(url)
f = open('python.jpg', 'wb')
# r.content获取响应内容（字节流）
f.write(r.content)
f.close()

