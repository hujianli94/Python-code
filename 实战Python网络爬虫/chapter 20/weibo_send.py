import base64
import time
#获取上传图片id
def upload_pic(session, watermark, nick, file_list=[]):
    pic_id_list=[]
    #判断图片数量是否在1-9之间
    if len(file_list)>0 and len(file_list)<10:
        for i in file_list:
            url='https://picupload.weibo.com/interface/pic_upload.php?cb=https%3A%2F%2Fweibo.com%2Faj%2Fstatic%2Fupimgback.html%3F_wv%3D5%26callback%3DSTK_ijax_'+str(int(time.time()*100000))+'&mime=image%2Fjpeg&data=base64&url=weibo.com%2F'+watermark+'&markpos=1&logo=1&nick=%40'+nick+'&marks=0&app=miniblog'
            #图片以字节数据流读取，然后base64加密
            files={'b64_data':base64.b64encode(open(i, "rb").read())}
            #上传文件
            r = session.post(url, files=files)
            print(r.text)
			# 获取图片id
            get_picid=eval(r.text.split('</script>')[1])['data']['pics']['pic_1']['pid']
            pic_id_list.append(get_picid)
    return pic_id_list

#发送微博，pic_id_list是上传图片Id的列表
def send(session,watermark, location, value, addtime='', pic_id_list=[]):
	# 构建请求头
    headers={'Referer':'http://weibo.com/'+str(watermark)+'/home',
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
    #构建请求参数
    data = {'location': location, 'text': value, 'appkey': '', 'style_type': '1', 'pic_id': '', 'tid': '',
            'pdetail': '','gif_ids':'','addtime':addtime, 'rank': "0", 'rankid': '', 'module': 'stissue',
            'pub_type': 'dialog', 'pub_source': 'main_', '_t': '0'}
    #发送图片
    if pic_id_list:
        pic_id=''
        for i in pic_id_list:
            pic_id += i+'|'
        #去除最后的"|"
        if pic_id[-1]=='|':
            pic_id=pic_id[0:len(pic_id)-1]
        data['updata_img_num'] = str(len(pic_id_list))
        data['pic_id'] = pic_id
	# 构建URL
    url='https://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%s' %(int(time.time()*1000))
    r = session.post(url, data=data, headers=headers)
    if r.status_code==200:
        return True
    else:
        return False