# 导入Selenium的webdriver类
from selenium import webdriver
# 设置变量url，用于浏览器访问
url = 'https://www.baidu.com/'
# 将webdriver类实例化，将浏览器设定为Google Chrome
# 参数executable_path是设置chromedriver的路径
path = 'E:\\Python\\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
# 打开浏览器并访问百度网址
browser.get(url)
