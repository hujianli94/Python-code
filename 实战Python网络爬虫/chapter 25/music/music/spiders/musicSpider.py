# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
import math,requests
from music.items import MusicItem
from scrapy.spider import Spider
from urllib.parse import quote

class QQMusic(Spider):
    name = 'Music'
    allowed_domains = ['qq.com']
    # start_urls是歌手列表URL
    start_urls = [
        'https://u.y.qq.com/cgi-bin/musicu.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A',
        '%2C%22sin%22%3A0%2C%22cur_page%22%3A1%7D%7D%7D'
        ]
    # 遍历歌手字母分类A-Z和特殊符号#
    def start_requests(self):
        lua = """function main(splash)
              splash:go("https://y.qq.com/")
              splash:wait(3)
              splash:go("https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&jsonpCallback=MusicJsonCallbacksinger_track&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid=001fNHEf1SFEFN&order=listen&begin=0&num=30&songstatus=1")
              splash:wait(3)
              return {
                splash:get_cookies()
              }
            end"""
        url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(lua)
        response = requests.get(url)
        print(response.json())
        cookie_dict = {}
        for i in response.json()['1']:
            cookie_dict[i['name']] = i['value']
        self.guid = cookie_dict['pgv_pvid']
        self.cookies = cookie_dict
        for index in range(1, 28):
            url = self.start_urls[0] +(str(index))+self.start_urls[1]
            yield scrapy.Request(url, dont_filter=True, callback=self.get_genre_singer, meta={'index': index})

    # 获取每个字母分类下的每页歌手
    def get_genre_singer(self, response):
        index = response.meta['index']
        # 从函数start_requests得出响应内容，获取总页数
        # str(response.body.decode('utf-8'))
        pagenum = json.loads(response.body.decode('utf-8'))['singerList']['data']['total']
        # 生成列表
        page_list = [x for x in range(1, pagenum+1)]
        for page in page_list:
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A10000%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A' + str(
                index) + '%2C%22sin%22%3A' + str((page - 1) * 80) + '%2C%22cur_page%22%3A' + str(page) + '%7D%7D%7D'
            # dont_filter取消重复请求。
            yield scrapy.Request(url, dont_filter=True, callback=self.get_singer_songs)

    # 获取每一个歌手信息
    def get_singer_songs(self, response):
        # 获取每个字母分类下的每页歌手的全部信息
        singermid_list = json.loads(response.body.decode('utf-8'))['singerList']['data']['singerlist']
        for k in singermid_list:
            url ='https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&singermid=%s&order=listen&begin=0&num=30&songstatus=1' % (k['singer_mid'])
            yield scrapy.Request(url, dont_filter=True, callback=self.get_singer_info, meta={'singermid': k['singer_mid']})

    # 获取歌手的每一页歌曲
    def get_singer_info(self, response):
        # 参数传递获取singermid
        singermid = response.meta['singermid']
        # 获取歌手的名字，总页数
        singer_info = json.loads(response.body.decode('utf-8'))
        song_singer = singer_info['data']['singer_name']
        songcount = singer_info['data']['total']
        pagecount = math.ceil(int(songcount) / 30)
        for p in range(pagecount):
            url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&singermid=%s' \
                  '&order=listen&begin=%s&num=30&songstatus=1' % (singermid, p * 30)
            yield scrapy.Request(url, dont_filter=True, callback=self.get_song_info, meta={'song_singer': song_singer})

    # 获取每一页的每一首歌曲信息
    def get_song_info(self, response):
        # 参数传递获取歌手名字
        song_singer = response.meta['song_singer']
        music_data = json.loads(response.body.decode('utf-8'))['data']['list']
        for i in music_data:
            songmid = i['musicData']['songmid']
            url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%22' + self.guid + '%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22' + self.guid + '%22%2C%22songmid%22%3A%5B%22' + songmid + '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D'
            yield scrapy.Request(url, dont_filter=True, callback=self.get_data, meta={'i':i, 'song_singer': song_singer},
                                cookies=self.cookies)

    # 每一首歌曲信息
    def get_data(self, response):
        # 参数传递
        # song_singer为歌手名字
        # i为歌曲信息
        song_singer = response.meta['song_singer']
        i = response.meta['i']
        # items.py文件的类的实例化，用于传递数据给pipelines.py实现存储
        items = MusicItem()
        # 获取下载歌曲的purl
        purl = json.loads(response.body.decode('utf-8'))['req_0']['data']['midurlinfo'][0]['purl']
        # 数据写入items，用于传递数据给pipelines.py实现存储
        items['song_url'] = 'http://isure.stream.qqmusic.qq.com/%s' %(purl)
        items['song_singer'] = song_singer
        items['song_name'] = i['musicData']['songname']
        items['song_ablum'] = i['musicData']['albumname']
        items['song_interval'] = i['musicData']['interval']
        items['song_songmid'] = i['musicData']['songmid']
        yield items
