from spider import request

# GET请求
url = 'http://httpbin.org/get'
# url = ['http://httpbin.org/get']
params = {
    'pyReptile': 'spiderGet'
}
cookies = {
    'pyReptile': 'spiderCookies'
}
# URL去重或分布式，设置Redis数据库连接参数
redis_host = '127.0.0.1'

r = request.get(url, params=params, cookies=cookies, redis_host=redis_host)
print(r.get('text', ''))
# print(r[0]['text'])

# POST请求
url = 'http://httpbin.org/post'
# url = ['http://httpbin.org/post']
data = {
    'pyReptile': 'spiderPost'
}
cookies = {
    'pyReptile': 'spiderCookies'
}
r = request.post(url, data=data, cookies=cookies)
print(r.get('text', ''))
# print(r[0]['text'])
