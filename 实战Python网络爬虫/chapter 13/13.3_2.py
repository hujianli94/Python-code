Html_content = """<html><head><title> Python</title></head>
<p class="title"><b>Beautiful Soup的学习</b></p>
<p class="study">学习网址：http://blog.csdn.net/huangzhang_123
 <a href="www.xxx.com" class="abc" id="try1">web开发</a>,
<a href=" www.ccc.com " class="bcd" id="try2">网络爬虫</a> and
<a href=" www.aaa.com " class="efg" id="try3">人工智能</a>;
</p>
<p class="other">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(Html_content, "html5lib")
# 以下是查找某标签的方法：
# 获取头部的信息，返回<head></head>之间的全部内容
soup.head
# 获取title的信息，返回<title></title>之间的全部内容
soup.title
# 这是个获取tag的小窍门,可以在文档树的tag中多次调用这个方法.下面的代码可以获取<body>标签中的第一个<b>标签，
# 也就是说，soup不一定是整个html的内容，可以先定位某部分，然后用这简洁方式获取，返回
# "<b>Beautiful Soup的学习</b>"
soup.body.b
# 直接指定标签类别，返回第一个标签的内容。返回 "<a href="www.xxx.com" class="abc"
# id = "try1">web开发</a>"
soup.a
# 获取第一个的标签a。
soup.find_all('a')
#[<a href="www.xxx.com" class="abc" id="try1">web开发</a>,
#<a href=" www.ccc.com " class="bcd" id="try2">网络爬虫</a>,
#<a href=" www.aaa.com " class="efg" id="try3">人工智能</a>]
