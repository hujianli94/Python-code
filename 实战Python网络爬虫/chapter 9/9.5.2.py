from selenium import webdriver
import time
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
# 使用JavaScript开启新的窗口
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)
# 获取当前显示的窗口信息
current_window = driver.current_window_handle
# 获取浏览器的全部窗口信息
handles = driver.window_handles
# 设置延时可以看到切换效果
time.sleep(3)
# 根据窗口信息进行窗口切换
# 切换百度搜索的窗口
driver.switch_to_window(handles[0])
time.sleep(3)
# 切换搜狗搜索的窗口
driver.switch_to_window(handles[1])
