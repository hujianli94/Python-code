import requests
import requests_cache
# 使用install_cache()方法
requests_cache.install_cache()
# 清除已有的缓存
requests_cache.clear()
# 访问自定义的Web系统
url = 'http://127.0.0.1:5000/'
# 创建Session会话
session = requests.session()
# 执行两次访问
for t in range(2):
    r = session.get(url)
    # from_cache是requests_cache的函数
    # 若输出True，说明生成缓存。
    print(r.from_cache)
