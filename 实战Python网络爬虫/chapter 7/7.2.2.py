import time
import requests_cache

# 定义钩子函数
def make_throttle_hook(delay=1.0):
    def hook(response, *args, **kwargs):
        # 如果没有缓存，则添加延时
        if not getattr(response, 'from_cache', False):
            print('delayTime')
            time.sleep(delay)
        return response
    return hook

if __name__ == '__main__':
    requests_cache.install_cache()
    requests_cache.clear()
    # 钩子函数的使用
    s = requests_cache.CachedSession()
    s.hooks = {'response': make_throttle_hook(2)}
    s.get('http://127.0.0.1:5000/')
    s.get('http://127.0.0.1:5000/')
