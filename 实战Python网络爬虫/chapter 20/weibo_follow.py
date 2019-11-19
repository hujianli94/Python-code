import time
# 关注微博，session是用户登录后会话，follow_url是被关注用户的微博首页
def follow_weibo(session, follow_url):
	# 构建请求头
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent,
        'Referer': follow_url
    }
    follow_info = {'oid': '', 'onick': '', 'location': ''}
    r = session.get(follow_url)
    response = r.text
    follow_info['oid'] = response.split("$CONFIG['oid']='")[1].split("';")[0]
    follow_info['onick'] = response.split("$CONFIG['onick']='")[1].split("';")[0]
    follow_info['location'] = response.split("$CONFIG['location']='")[1].split("';")[0]
	# 关注URL，参数__rnd为时间戳
    url = 'https://www.weibo.com/aj/f/followed?ajwvr=6&__rnd=' + \
        str(int(time.time() * 1000))
    data = {
        'uid': follow_info['oid'],
        'objectid': '',
        'f': '1',
        'extra': '',
        'refer_sort': '',
        'refer_flag': '1005050001_',
        'location': follow_info['location'],
        'oid': follow_info['oid'],
        'wforce': '1',
        'nogroup': 'false',
        'fnick': follow_info['onick'],
        'refer_lflag': '',
        'refer_from': 'profile_headerv6',
        '_t': '0'
    }
    r = session.post(url, data=data, headers=headers)
	# 判断是否关注成功
    if (r.json()['code']) == '100000':
        return (follow_info['onick'] + '关注成功')
    else:
        return (follow_info['onick'] + '关注失败')
