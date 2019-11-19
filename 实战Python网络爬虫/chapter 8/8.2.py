from requests_html import HTMLSession
# 定义会话Session
session = HTMLSession()
url = 'https://movie.douban.com/'
# 发送GET请求
r = session.get(url)
# 发送POST请求
r = session.post(url, data={})
# 输出网页的URL地址
print(r.html)
