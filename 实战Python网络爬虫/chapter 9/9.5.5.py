from selenium import webdriver
import time
# 启动浏览器
driver = webdriver.Chrome()
driver.get('https://www.youdao.com')
time.sleep(5)
# 添加Cookies
driver.add_cookie({'name': 'Login_User', 'value': 'PassWord'})
# 获取全部Cookies
all_cookies = driver.get_cookies()
print('全部的Cookies为：', all_cookies)
# 获取name为Login_User的Cookie内容
one_cookie = driver.get_cookie('Login_User')
print('单个的Cookie为：', one_cookie)
# 删除name为Login_User的Cookie
driver.delete_cookie('Login_User')
surplus_cookies = driver.get_cookies()
print('剩余的Cookie为：', surplus_cookies)
# 删除全部Cookies
driver.delete_all_cookies()
surplus_cookies = driver.get_cookies()
print('剩余的Cookie为：', surplus_cookies)
