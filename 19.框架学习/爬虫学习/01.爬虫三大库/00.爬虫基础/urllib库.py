import re
import urllib.request


# 下载文件
# filename = urllib.request高级用法.urlretrieve("https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9415923190155813440%22%7D&n_type=0&p_from=1",filename="test.html")
filename = urllib.request.urlretrieve("https://mbd.baidu.com",filename="test.html")
