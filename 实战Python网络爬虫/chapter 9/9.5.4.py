from selenium import webdriver
# 设置文件保存的路径，如不设置，默认系统的Downloads文件夹
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)
# 启动浏览器
driver = webdriver.Chrome()
# 下载微信PC版安装包
driver.get('https://pc.weixin.qq.com/')
# 浏览器窗口最大化
driver.maximize_window()
# 点击下载按钮
driver.find_element_by_class_name('button').click()
