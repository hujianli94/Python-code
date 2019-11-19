import requests
import time
import urllib
import base64
import rsa
import binascii
import re
# 接入第三方API识别验证码
from weibo_verify_code import code_verificate
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

# 下载验证码图片
def get_img(pcid):
    url = 'https://login.sina.com.cn/cgi/pin.php?r=%s&s=0&p=%s' %(str(math.floor(random.random() * 100000000)),pcid)
    resp = session.get(url)
    verify_code_path = '%s.png' % (str(int(time.time() * 1000)))
    f = open(verify_code_path, 'wb')
    f.write(resp.content)
    f.close()
    return verify_code_path


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
    # 判断是否存在验证码
    if 'showpin' in sever_data.keys():
        # 添加请求参数
        pcid = sever_data['pcid']
        data['pcid'] = pcid
        # 下载验证码图片
        verify_code_path = get_img(pcid)
        # 第三方平台识别验证码
        verify_code = code_verificate(yundama_username, yundama_password, verify_code_path)
        print(verify_code)
        data['door'] = verify_code

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
    # 第三方平台账号密码
    yundama_username = 'xxx'
    yundama_password = 'xxxx'
    user_info = login('13435423143','XXXXXX')

    ############关键字搜索热门微博#############
    # # 导入微博采集功能
    # from weibo_collect import collect
    # #爬取前十页数据
    # for i in range(10):
    #     collect('#王者荣耀#',session,i)
    ############关键字搜索热门微博#############
   
    ################发布微博###################
    # # 导入微博发布模块
    # from weibo_send import upload_pic,send
    # # 获取用户信息
    # watermark = user_info['watermark']
    # nick = user_info['nick']
    # location = user_info['location']
    # # 设置图片列表
    # file_list=['aa.png','bb.png']
    # # 获取图片id列表
    # pic_id_list = upload_pic(session,watermark,nick,file_list)
    # # 发布微博
    # send(session, watermark, location, "Python爬虫", addtime='', pic_id_list=pic_id_list)
    ################发布微博###################

    ################关注用户###################
    # # 导入关注用户模块
    # from weibo_follow import follow_weibo
    # # 关注用户的首页链接
    # follow_url = 'https://weibo.com/renminwang'
    # status = follow_weibo(session, follow_url)
    # print(status)
    ################关注用户###################

    ##############点赞和转发评论###############
    # 导入点赞和转发评论模块
    from weibo_forward import forward_weibo, like_weibo
    url = 'https://weibo.com/u17t'
    # 点赞
    result = like_weibo(session, url)
    print(result)
    # 转发评论
    result = forward_weibo(session, url, 'Python网络爬虫')
    print(result)
    ##############点赞和转发评论###############