#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/21 13:29
# filename: 01.post方法.py
import requests

url = "https://accounts.douban.com"

headers = {
    'Cookie': 'bid=uWfPo5t8SbU; _vwo_uuid_v2=DB1333011A2A21830E29E8EE912542282|9dc2d0b2193bffe49f2b6682e67394a1; gr_user_id=162a142e-7c6c-46df-9237-db2c427c5b7f; douban-fav-remind=1; __yadk_uid=vj37JPEEb9L2Q3UFZa9U8B4MEyVzQ91v; __gads=ID=d995405eae157057:T=1558079617:S=ALNI_MaE9V_n1RzmuHc1BOgR3jKcQoqamQ; _ga=GA1.2.346628374.1559738261; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; ll="118254"; ct=y; __utmz=30149280.1563081781.7.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="3040149_2995812_1407437_1403307_34434166_34431483_30434690_26274202_30437866_26919485"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1563687048%2C%22https%3A%2F%2Fmusic.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.346628374.1559738261.1563113716.1563687050.12; __utmc=30149280; __utmt=1; dbcl2="175181423:u9apU0YA3j4"; ck=Eoy_; _pk_id.100001.8cb4=f68226eb49681388.1560563142.4.1563687245.1562298063.; __utmv=30149280.17518; __utmb=30149280.4.10.1563687050'
}

r = requests.get(url, headers=headers)
print(r.text)