import requests
# 运行Scrapyd的Scrapy
url = 'http://localhost:6800/schedule.json'
data = {
    # 参数project是scrapy.cfg的属性project
    'project': 'douban',
    # 参数spider是项目spider的name属性
    'spider': 'Movie'
}
r = requests.post(url, data=data)
print(r.json())

# 删除Scrapyd的Scrapy
url = 'http://localhost:6800/delproject.json'
data = {
    # 参数project是scrapy.cfg的属性project
    'project': 'douban',
}
r = requests.post(url, data=data)
print(r.json())