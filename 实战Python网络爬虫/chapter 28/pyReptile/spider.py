import asyncio
import aiohttp
import redis

# 设置默认参数
TIMEOUT = 40
REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# 实例化对象，用于发送HTTP请求
loop = asyncio.get_event_loop()


# 定义装饰器，实现URL去重或分布式处理
def distributes(func):
    def wrapper(self, url, **kwargs):
        redis_host = kwargs.get('redis_host', '')
        if redis_host:
            port = kwargs.get('port', 6379)
            db = kwargs.get('db', 1)
            redis_db = redis.Redis(host=redis_host, port=port, db=db)
            redis_data_dict = 'keys'
            if not redis_db.hexists(redis_data_dict, url):
                redis_db.hset(redis_data_dict, url, 0)
                return func(self, url, **kwargs)
            else:
                return {}
        else:
            return func(self, url, **kwargs)
    return wrapper


# 定义爬虫类
class Request(object):
    # 定义异步函数
    async def httpGet(self, url, **kwargs):
        cookies = kwargs.get('cookies', {})
        params = kwargs.get('params', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout', TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        # 带代理IP
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(url, params=params, proxy=proxy, timeout=timeout,
                                       headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        # 不带代理IP
        else:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(url, params=params, timeout=timeout,
                                       headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result

    # 定义异步函数
    async def httpPost(self, url, **kwargs):
        cookies = kwargs.get('cookies', {})
        data = kwargs.get('data', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout', TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.post(url, data=data, proxy=proxy, timeout=timeout,
                                        headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        else:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.post(url, data=data, timeout=timeout,
                                        headers=headers) as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result

    # 定义GET请求方式
    @distributes
    def get(self, url, **kwargs):
        tasks = []
        if isinstance(url, list):
            for u in url:
                task = asyncio.ensure_future(self.httpGet(u, **kwargs))
                tasks.append(task)
            result = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            result = loop.run_until_complete(self.httpGet(url, **kwargs))
        return result

    # 定义POST请求方式
    @distributes
    def post(self, url, **kwargs):
        tasks = []
        if isinstance(url, list):
            for u in url:
                task = asyncio.ensure_future(self.httpPost(u, **kwargs))
                tasks.append(task)
            result = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            result = loop.run_until_complete(self.httpPost(url, **kwargs))
        return result


# 实例化Request对象
request = Request()
