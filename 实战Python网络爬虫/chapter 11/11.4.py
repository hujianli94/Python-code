import requests
# 文件路径
path = r'F:\\video\\'
num = 0
def response(flow):
    global num
    # 视频URL的特征
    target_urls = r'/r/baiducdncnc.inter.iqiyi.com/videos/v0/'
    # 过滤重复的url
    repeat_urls = []
    if target_urls in flow.request.url and flow.request.url not in repeat_urls:
        repeat_urls.append(flow.request.url)
        # 设置视频名
        filename = path + str(num) + '.mp4'
        # 使用request获取视频url的内容
        # stream=True作用是推迟下载响应体直到访问Response.content属性
        res = requests.get(flow.request.url, stream=True)
        # 将视频写入文件夹
        with open(filename, 'ab') as f:
            f.write(res.content)
            f.flush()
            print(filename + '下载完成')
            num += 1

