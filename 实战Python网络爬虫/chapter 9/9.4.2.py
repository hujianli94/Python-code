from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
url = 'https://passport.bilibili.com/login'
driver = webdriver.Chrome()
driver.get(url)
# 双击登录
element = driver.find_element_by_class_name('tit')
ActionChains(driver).double_click(element).perform()
# 设置延时，否则会导致操作过快
time.sleep(3)
# 拖拉滑条
element = driver.find_element_by_class_name('gt_slider_knob,gt_show')
ActionChains(driver).drag_and_drop_by_offset(element, 100, 0).perform()
