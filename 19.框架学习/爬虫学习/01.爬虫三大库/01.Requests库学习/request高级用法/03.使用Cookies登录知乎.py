#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/20 10:05
# filename: 03.使用Cookies登录知乎.py
import requests

headers = {

    'cookie': '_xsrf=blH4uNHhqVhWkhMSr00F5QkBd6wSkFn1; _zap=c72d2f67-65a5-4f49-8ead-fbfcbaa087e6; d_c0="AEDjrlDB6A-PTt0WfQPevqfeBoB8jWNDs-E=|1566097970"; tgw_l7_route=1834ebf1acd448097141c3bb455d5563; capsion_ticket="2|1:0|10:1566266663|14:capsion_ticket|44:OGM2ZDQzZmQ0MjBiNGI1YjgzNWNhNTJjNjcxNmRjOWU=|bab315c5cadb9f904c0fc999bfc0af781d41c1b26b97b7315b725e90c92a734c"; z_c0="2|1:0|10:1566266672|4:z_c0|92:Mi4xVUJHWUF3QUFBQUFBUU9PdVVNSG9EeVlBQUFCZ0FsVk5NS05JWGdBb0tRYlBYcXFrZ0thaG5fb09aNXN4MzBpZEFR|ac611325868d68317b9810df173f46304b29be303517b989563b5992b632f756"; tst=r',
    'Host': 'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

}

r = requests.get("https://www.zhihu.com/", headers=headers)
print(r.text)
