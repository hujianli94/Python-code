from bs4 import BeautifulSoup
import urllib
import csv
import requests
import time
import datetime
from concurrent.futures import ThreadPoolExecutor

# 多线程爬取视频文件
def thread_video(get_video_value, video_path):
    if get_video_value:
        url = get_video_value['action-data'].split('video_src=')[1].split('&cover_img=')[0]
        url = 'http:' + urllib.parse.unquote(url)
        try:
            temp_value = requests.get(url)
            video = open('video/' + video_path, 'wb')
            video.write(temp_value.content)
            video.close()
        except:
            pass

# 多线程爬取图片
def thread_img(k, img_path):
    r = requests.get('http:' + k['src'])
    img = open('image/' + img_path, 'wb')
    img.write(r.content)
    img.close()


# 采集微博
def collect(keyword, session, pagenumber=1):
    # 关键字编码
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 构建URL
    keyword = urllib.parse.quote(keyword)
    url = 'https://s.weibo.com/weibo?q=' + keyword + '&Refer = SWeibo_bo&page=%s' % (str(pagenumber))

    r = session.get(url)
    # 清洗多余的符号
    get_value = r.text.replace('\/', '/')
    soup = BeautifulSoup(get_value, 'html5lib')
    # 定位用户信息
    get_info = soup.find_all('div', class_="content")

    for i in get_info:
        # 微博内容与用户信息
        get_comment = i.find_all('p', class_='txt')
        if get_comment:
            # 输出全部文字内容
            if len(get_comment) > 1:
                get_comment = get_comment[-1]
            else:
                get_comment = get_comment[0]
            comment = get_comment.getText().strip()

            # 获取用户信息
            get_user = i.find('a', class_='name')
            if get_user:
                user_name = get_user.getText().strip()
            else:
                user_name = ''

        img_path_list = ''

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

        # 输出视频
        get_video_value = i.find('a', class_='WB_video_h5')
        if get_video_value:
            pool = ThreadPoolExecutor(max_workers=1)
            video_path = str(int(time.time() * 1000)) + '.mp4'

            pool.submit(thread_video, get_video_value, video_path)

        # 用于生成csv
        f = open('data.csv', 'a', newline='', encoding='gb18030')
        writer = csv.writer(f)
        writer.writerow([user_name, comment, img_path_list, video_path, now])
        f.close()
