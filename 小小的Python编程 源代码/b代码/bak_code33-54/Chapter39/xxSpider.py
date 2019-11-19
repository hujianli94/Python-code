#小小爬虫：存储网页中的所有链接文字和目标url

#将下载的网页文件加载
def loadfile(file_path):
    try:
        f=open(file_path,'r',encoding='UTF-8')
        raw_txt=f.read()
        lines0=raw_txt.split("<a ")
        #lines列表的每个元素都是一个字符串，不含有"<a"，含有一个"</a>",除第一个元素外
        lines=[]
        for i in range(1,len(lines0)):
            t=lines0[i].split("</a>")   #保留<a>前面的部分
            lines.append(t[0])  
        return lines
    except:
        print("文件读取失败：loadfile()")
        raise

##html_file_path="搜狐新闻-搜狐.html"
##for i in range(30):
##    print(loadfile(html_file_path)[i])

#正则匹配链接
def search_links(raw_txt):
    import re
    ptn_link_txt='href=[\'\"]([\S]*)[\"\'].*?>([\S\s]*)'  #链接模式
    result=re.search(ptn_link_txt,raw_txt)
    link_txt="？"
    link_url="？"
    if result:
        link_txt=result.group(2)
        link_url=result.group(1)
    return link_txt+"【链接到】"+link_url

#启动爬虫
html_file_path="搜狐新闻-搜狐.html"
lines=loadfile(html_file_path)
print('共',len(lines),"行")
for i in range(0,len(lines)):
    result=search_links(lines[i])
    print(i+1,result)

