# 引入BeautifulSoup
from bs4 import BeautifulSoup
# 读取MySoup.html文件
Open_file = open('MySoup.html', 'r', encoding='utf-8')
# 将MySoup.html的内容赋值给Html_Content，并关闭文件
Html_Content = Open_file.read()
Open_file.close()
# 使用html5lib解释器解释Html_Content的内容
soup = BeautifulSoup(Html_Content, "html5lib")
# 输出title
print('html title is ' + soup.title.getText())
# 查找第一个标签p,并输出
find_p = soup.find('p', id="python")
print('the first <p> is ' + find_p.getText())
# 查找全部标签p,并输出
find_all_p = soup.find_all('p')
for i, k in enumerate(find_all_p):
    print('the ' + str(i + 1) + ' p is ' + k.getText())
