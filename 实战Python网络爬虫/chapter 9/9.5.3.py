from selenium import webdriver
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
# 隐性等待，最长等待时间为30秒
driver.implicitly_wait(30)
driver.find_element_by_id('kw').send_keys('Python')
# 显性等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# visibility_of_element_located检查网页元素是否可见
# (By.ID, 'kw')：kw是搜索框的id属性值，By.ID是使用find_element_by_id定位
condition = expected_conditions.visibility_of_element_located((By.ID, 'kw'))
WebDriverWait(driver=driver, timeout=20, poll_frequency=0.5).until(condition)
