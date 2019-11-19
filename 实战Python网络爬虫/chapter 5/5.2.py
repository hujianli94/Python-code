# 导入urllib
import urllib.request
# 打开URL
response = urllib.request.urlopen('https://movie.douban.com/', None, 2)
# 读取返回的内容
html = response.read().decode('utf8')
# 写入txt
f = open('code1.txt', 'w', encoding='utf8')
f.write(html)
f.close()
