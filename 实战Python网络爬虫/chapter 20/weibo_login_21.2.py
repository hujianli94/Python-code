import requests
import time
import urllib
import base64
import rsa
import binascii
import re
# 登录前准备
def get_server_data(su):
    # 构建URL
    prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.19)&_=%s' %(su, str(int(time.time() * 1000)))
    pre_data_res = session.get(prelogin_url, headers=headers, proxies=proxies)
    # 将响应内容转换字典格式
    sever_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))
    return sever_data

# 账号加密
def get_su(username):
    # 使用urllib.parse.quote_plus对 email 地址或手机号码的特殊符号编码处理
    # 然后使用 base64 加密
    username_quote = urllib.parse.quote_plus(username)
    username_base64 = base64.b64encode(username_quote.encode("utf-8"))
    return username_base64.decode("utf-8")

# 密码加密，servertime, nonce, pubkey来自图16-2的数据
def get_password(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    # 创建公钥
    key = rsa.PublicKey(rsaPublickey, 65537)
    # 拼接明文
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    message = message.encode("utf-8")
    # 加密
    passwd = rsa.encrypt(message, key)
    # 将加密信息转换为16进制
    passwd = binascii.b2a_hex(passwd)
    return passwd

# 用户登录
def login(username, password):
    # 获取servertime、nonce、rsakv、su和sp
    su = get_su(username)
    sever_data = get_server_data(su)
    servertime = sever_data["servertime"]
    nonce = sever_data['nonce']
    rsakv = sever_data["rsakv"]
    pubkey = sever_data["pubkey"]
    sp = get_password(password, servertime, nonce, pubkey)
	# 构建请求参数
    data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'useticket': '1',
        'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
        'vsnf': '1',
        'su': su,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sp': sp,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
        }
	# 用户登录
    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    login_page = session.post(login_url, data=data)
    login_loop = (login_page.content.decode("GBK"))
	# 网页跳转URL，获取用户信息
    pa = r'location\.replace\([\'"](.*?)[\'"]\)'
    loop_url = re.findall(pa, login_loop)[0]
    login_index = session.get(loop_url)
    uuid = login_index.text
    uuid_pa = r'"uniqueid":"(.*?)"'
    uuid_res = re.findall(uuid_pa, uuid, re.S)[0]
    # 根据uniqueid构建微博首页URL
    web_weibo_url = "http://weibo.com/%s" % uuid_res
    weibo_page = session.get(web_weibo_url)
    response = weibo_page.text
    person_info = {}
    if '$CONFIG' in response:
        person_info['nick'] = response.split("$CONFIG['nick']='")[1].split("';")[0]
        person_info['watermark'] = response.split("$CONFIG['watermark']='")[1].split("';")[0]
        person_info['location'] = response.split("$CONFIG['location']='")[1].split("';")[0]
        person_info['uid'] = response.split("$CONFIG['uid']='")[1].split("';")[0]
        person_info['domain'] = response.split("$CONFIG['domain']='")[1].split("';")[0]
        person_info['oid'] = response.split("$CONFIG['oid']='")[1].split("';")[0]
        print('登陆成功，你的用户名为：' + person_info['nick'])
    else:
        print('登陆失败')
    return person_info

if __name__ == "__main__":
    # 构造请求头
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent
    }
    # 代理IP
    proxies = {}
    # 新建会话
    session = requests.session()
    user_info = login('13435423143','YONGxiang314')
