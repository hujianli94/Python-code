from requests_html import HTMLSession
# 定义会话Session
session = HTMLSession()
url = 'https://movie.douban.com/'
# 发送GET请求
r = session.get(url)
# 输出网页的URL地址
print(r.html)
# 输出网页里全部URL地址
print(r.html.links)
# 输出网页里精准的URL地址
print(r.html.absolute_links)
# 输出网页的HTML信息
print(r.text)
# 输出网页的全部文本信息，即去除HTML代码
print(r.html.text)
