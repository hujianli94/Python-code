import re
import time
# 微博点赞
def like_weibo(session, like_url):
    # 获取点赞用户的前16条微博
    r = session.get(like_url)
    # 获取location
    location = r.text.split("$CONFIG['location']='")[1].split("';")[0]
    # 获取mid
    mid_list = re.findall(r'mid=(.\d+)&name', r.text, re.S)
    # 构建请求头
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent,
        'Referer': like_url
    }
    # 点赞功能，参数mid默认是第一条微博
    url = 'https://weibo.com/aj/v6/like/add?ajwvr=6&__rnd=' + (str(int(time.time() * 1000)))
    data = {
        'location': location,
        'version': 'mini',
        'qid': 'heart',
        'mid': mid_list[0],
        'loc': 'profile',
        'cuslike': '1',
        '_t': '0'
    }
    r = session.post(url, data=data, headers=headers)
    # 根据返回内容判断是否成功
    if (r.json()['code']) == '100000':
        return ('点赞成功')
    else:
        return ('点赞失败')

# 转发评论微博
def forward_weibo(session, forward_url, reason):
    # 获取点赞用户的前16条微博
    r = session.get(forward_url)
    # 获取location
    location = r.text.split("$CONFIG['location']='")[1].split("';")[0]
    page_id = r.text.split("$CONFIG['page_id']='")[1].split("';")[0]
    domain = r.text.split("$CONFIG['domain']='")[1].split("';")[0]
    # 获取mid
    mid_list = re.findall(r'mid=(.\d+)&name', r.text, re.S)
    # 构建请求头
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent,
        'Referer': forward_url
    }
    # 转发评论
    url = 'https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain='+ domain +'&__rnd=' + (str(int(time.time() * 1000)))
    data = {
        'pic_src': '',
        'pic_id': '',
        'appkey': '',
        'mid': mid_list[0],
        'style_type': '1',
        'mark': '',
        'reason': reason,
        'location': location,
        'pdetail': page_id,
        'module': '',
        'page_module_id': '',
        'refer_sort': '',
        'is_comment_base': '1',
        'rank': '0',
        'rankid': '',
        '_t': '0'
    }
    r = session.post(url, data=data, headers=headers)
    # 根据返回内容判断是否成功
    if (r.json()['code']) == '100000':
        return ('转发成功')
    else:
        return ('转发失败')