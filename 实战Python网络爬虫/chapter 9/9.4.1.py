from selenium import webdriver
url = 'https://ssl.zc.qq.com/v3/index-chs.html?from=pt'
driver = webdriver.Chrome()
driver.get(url)
# 输入名字和密码
driver.find_element_by_id('nickname').send_keys('pythonAuto')
driver.find_element_by_id('password').send_keys('pythonAuto123')
# 获取手机号码下方的tips内容
tipsValue = driver.find_element_by_xpath(
'//div[3]/div[2]/div[1]/form/div[7]/div').text
print(tipsValue)
# 勾选同时开通QQ空间
driver.find_element_by_class_name('checkbox').click()
# 点击“注册”按钮
driver.find_element_by_id('get_acc').submit()
