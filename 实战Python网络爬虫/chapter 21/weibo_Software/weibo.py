import time
import base64
import rsa
import math
import random
import binascii
import requests
import re, json, urllib, csv, datetime, os
from weibo_verify_code import code_verificate
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

#############
# 登录微博
#############
index_url = "http://weibo.com/login.php"
yundama_username = 'beeto'
yundama_password = 'beeto123'
verify_code_path = ''

def get_pincode_url(pcid):
    size = 0
    url = "http://login.sina.com.cn/cgi/pin.php"
    pincode_url = '{}?r={}&s={}&p={}'.format(url, math.floor(random.random() * 100000000), size, pcid)
    return pincode_url

def get_img(url, headers):
    resp = requests.get(url, headers=headers, stream=True)
    global verify_code_path
    mkdir('temp/code')
    verify_code_path = './temp/code/%s.png' % (str(int(time.time() * 1000)))
    with open(verify_code_path, 'wb') as f:
        for chunk in resp.iter_content(1000):
            f.write(chunk)

def get_su(username):
    """
    对 email 地址和手机号码 先 javascript 中 encodeURIComponent
    对应 Python 3 中的是 urllib.parse.quote_plus
    然后在 base64 加密后decode
    """
    username_quote = urllib.parse.quote_plus(username)
    username_base64 = base64.b64encode(username_quote.encode("utf-8"))
    return username_base64.decode("utf-8")

# 预登陆获得 servertime, nonce, pubkey, rsakv
def get_server_data(su, session, headers, proxies):
    pre_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su="
    pre_url = pre_url + su + "&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_="
    prelogin_url = pre_url + str(int(time.time() * 1000))
    pre_data_res = session.get(prelogin_url, headers=headers, proxies=proxies)
    sever_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))

    return sever_data

# 这一段用户加密密码，需要参考加密文件
def get_password(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
	# 创建公钥
    key = rsa.PublicKey(rsaPublickey, 65537)  
	# 拼接明文js加密文件中得到
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)  
    message = message.encode("utf-8")
	# 加密
    passwd = rsa.encrypt(message, key)
	# 将加密信息转换为16进制
    passwd = binascii.b2a_hex(passwd)
    return passwd

def login(username, password, proxies={}):
    # 构造 Request headers
    verify_code = 'Nocode'
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent
    }
    # 新建会话
    session = requests.session()
    # su 是加密后的用户名
    su = get_su(username)
    sever_data = get_server_data(su, session, headers, proxies)
    servertime = sever_data["servertime"]
    nonce = sever_data['nonce']
    rsakv = sever_data["rsakv"]
    pubkey = sever_data["pubkey"]
    password_secret = get_password(password, servertime, nonce, pubkey)

    postdata = {
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
        'sp': password_secret,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    try:
        need_pin = sever_data['showpin']
        if need_pin == 1:
            if not yundama_username:
                raise Exception('由于本次登录需要验证码，请配置顶部位置云打码的用户名{}和及相关密码'.format(yundama_username))
            pcid = sever_data['pcid']
            postdata['pcid'] = pcid
            img_url = get_pincode_url(pcid)
            get_img(img_url, headers)
            verify_code = code_verificate(yundama_username, yundama_password, verify_code_path)
            postdata['door'] = verify_code

        login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
        login_page = session.post(login_url, data=postdata, headers=headers, proxies=proxies)
        login_loop = (login_page.content.decode("GBK"))
        pa = r'location\.replace\([\'"](.*?)[\'"]\)'
        loop_url = re.findall(pa, login_loop)[0]
        login_index = session.get(loop_url, headers=headers, proxies=proxies)
        uuid = login_index.text
        uuid_pa = r'"uniqueid":"(.*?)"'

        uuid_res = re.findall(uuid_pa, uuid, re.S)[0]
        web_weibo_url = "http://weibo.com/%s/profile?topnav=1&wvr=6&is_all=1" % uuid_res
        weibo_page = session.get(web_weibo_url, headers=headers, proxies=proxies)
        weibo_pa = r'<title>(.*?)</title>'
        user_name = re.findall(weibo_pa, weibo_page.content.decode("utf-8", 'ignore'), re.S)[0]
        # 获取用户信息
        response = weibo_page.text
        person_info = {}
        if '$CONFIG' in response:
            person_info['nick'] = response.split("$CONFIG['nick']='")[1].split("';")[0]
            person_info['watermark'] = response.split("$CONFIG['watermark']='")[1].split("';")[0]
            person_info['location'] = response.split("$CONFIG['location']='")[1].split("';")[0]
            person_info['uid'] = response.split("$CONFIG['uid']='")[1].split("';")[0]
            person_info['domain'] = response.split("$CONFIG['domain']='")[1].split("';")[0]
            person_info['oid'] = response.split("$CONFIG['oid']='")[1].split("';")[0]

        print('登陆成功，你的用户名为：' + user_name)

        return {'session': session, 'info': person_info, 'code': '1000'}
    except:
        if verify_code != 'Nocode' and verify_code == '':
            # 打码平台账号密码错误或者余额不足
            return {'code': '1002'}
        else:
            # 微博账号密码错误或者验证码识别错误
            return {'code': '1001'}

#############
# 发送微博
#############
# 获取上传图片id
def upload_pic(watermark, nick, session, file_list=[], proxies={}):
    return_result = []
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    headers = {
        'User-Agent': agent
    }
    if len(file_list) > 0 and len(file_list) < 10:
        for i in file_list:
            url = 'http://picupload.service.weibo.com/interface/pic_upload.php' \
                  '?mime=image/png&data=base64&url=weibo.com/' + str(watermark) + \
                  '&markpos=1&logo=&nick=@' + str(nick) + '&marks=1&app=miniblog'
            files = {
                'b64_data': base64.b64encode(open(i, "rb").read())
            }
            r = session.post(url, files=files, headers=headers, proxies=proxies)
            try:
                get_picid = json.loads(r.text.split('</script>')[1])['data']['pics']['pic_1']['pid']
                return_result.append(get_picid)
            except:
                pass
    return return_result

# 发送微博。send_type判断是否发送图片
# pic_id_list是上传图片后所生成的Id
def send_weibo(watermark, location, value, session, addtime='', pic_id_list=[], send_type='words', proxies={}):
    headers = {
        'Referer': 'https://weibo.com/' + str(watermark) + '/home',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    data = {}
    # 发送文字
    if send_type == 'words':
        data = {'location': location, 'text': value, 'appkey': '', "style_type": "1", "pic_id": "", 'tid': '',
                "pdetail": "", 'addtime': addtime,
                "rank": "0", "rankid": "", 'module': 'stissue', 'pub_type': 'dialog', 'pub_source': 'main_', '_t': '0'
                }
    # 发送图片
    elif send_type != 'words' and pic_id_list:
        pic_id = ''
        for i in pic_id_list:
            pic_id += i + '|' if len(pic_id_list) > 1 else i
        # 去除最后的|
        if pic_id[-1] == '|':
            pic_id = pic_id[0:len(pic_id) - 1]

        data = {'location': location, 'text': value, 'appkey': '', 'style_type': '1', 'pic_id': pic_id, 'tid': '',
                'pdetail': '', 'gif_ids': '', 'updata_img_num': str(len(pic_id_list)), 'addtime': addtime,
                'rank': "0", 'rankid': '', 'module': 'stissue', 'pub_type': 'dialog', 'pub_source': 'main_', '_t': '0'
                }

    url = 'https://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%s' % (int(time.time() * 1000))
    r = session.post(url, data=data, headers=headers, proxies=proxies)
    if r.status_code == 200:
        return True
    else:
        return False

#############
# 采集数据
#############
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if 'csv' in path and isExists == False:
        f = open('temp/data.csv', 'w', newline='', encoding='gb18030')
        writer = csv.writer(f)
        writer.writerow(['用户', '文本内容', '图片', '视频', '采集日期'])
        f.close()
    if not isExists and 'csv' not in path:
        os.makedirs(path)

# 线程爬取视频文件
def more_thread(get_video_value, video_path):
    if get_video_value:
        url = get_video_value['action-data'].split('video_src=')[1].split('&cover_img=')[0]
        url = 'http:' + urllib.parse.unquote(url)
        try:
            temp_value = requests.get(url)
            video = open('temp/video/' + video_path, 'wb')
            video.write(temp_value.content)
            video.close()
        except:
            pass

# 线程爬取图片
def thread_img(k, img_path):
    img_r = requests.get('http:' + k['src'])
    img = open('temp/image/' + img_path, 'wb')
    img.write(img_r.content)
    img.close()

# 获取搜索内容
def collect_weibo(keyword, session, pagenumber=1, proxies={}, get_img=False, get_video=False):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    keyword = urllib.parse.quote(keyword)
    url = 'https://s.weibo.com/weibo?q=' + keyword + '&Refer = SWeibo_bo&page=%s' % (str(pagenumber))
    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
    headers = {
        'User-Agent': agent
    }
    r = session.get(url, headers=headers, proxies=proxies)
    get_value = r.text.replace('\/', '/')
    soup = BeautifulSoup(get_value, 'html5lib')
    # 定位用户信息
    get_info = soup.find_all('div', class_="content")
    
    # 生成素材文件夹
    mkdir('temp')
    mkdir('temp/image')
    mkdir('temp/video')
    mkdir('temp/data.csv')

    for i in get_info:
        # 获取文字全部内容
        get_comment = i.find_all('p', class_='txt')
        if get_comment:
            if len(get_comment) > 1:
                get_comment = get_comment[-1]
            else:
                get_comment = get_comment[0]
            # 输出全部文字内容
            comment = get_comment.getText().strip()
            # 获取用户信息
            get_user = i.find('a', class_='name')
            if get_user:
                user_name = get_user.getText().strip()
            else:
                user_name = ''

            img_path_list = ''
            if get_img:
                # 获取图片内容
                get_img_value = i.find('ul', class_='m3')
                # 输出图片
                if get_img_value:
                    get_img_value = get_img_value.find_all('img')
                    for k in get_img_value:
                        img_path = str(int(time.time() * 1000)) + '.jpg'
                        img_path_list = img_path_list + img_path + '/'
                        pool = ThreadPoolExecutor(max_workers=1)
                        pool.submit(thread_img, k, img_path)

            video_path = ''
            if get_video:
                # 输出视频
                get_video_value = i.find('a', class_='WB_video_h5')
                if get_video_value:
                    pool = ThreadPoolExecutor(max_workers=1)
                    video_path = str(int(time.time() * 1000)) + '.mp4'
                    pool.submit(more_thread, get_video_value, video_path)
            # 用于生成csv
            f = open('temp/data.csv', 'a', newline='', encoding='gb18030')
            writer = csv.writer(f)
            writer.writerow([user_name, comment, img_path_list, video_path, now])
            f.close()

