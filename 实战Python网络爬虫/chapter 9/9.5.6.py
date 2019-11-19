from selenium import webdriver
url = 'XXXXX'
driver = webdriver.Chrome()
driver.get(url)

""" 定位到第一个iframe """
# 通过索引定位
driver.switch_to.frame(0)
# 通过iframe的id或name属性定位
driver.switch_to.frame('iframe_a') 
# 先定位iframe再切换到iframe_a
element = driver.find_element_by_id("iframe_a")
driver.switch_to.frame(element)
# 从iframe_a跳回HTML
driver.switch_to.default_content()

""" 定位到第二个iframe """
# 通过索引定位
driver.switch_to.frame(1)
# 通过iframe的id或name属性定位
driver.switch_to.frame('iframe_b') 
# 先定位iframe再切换到iframe_b
element = driver.find_element_by_id("iframe_b")
driver.switch_to.frame(element)
# 从iframe_b跳回HTML
driver.switch_to.default_content()

""" 定位到第三个iframe """
# 定位到iframe_a
driver.switch_to.frame('iframe_a')
# 再从iframe_a切换iframe_d
driver.switch_to.frame('iframe_d')
# 从iframe_d跳回到iframe_a
driver.switch_to.parent_frame()
# 从iframe_d跳回HTML
driver.switch_to.default_content()
