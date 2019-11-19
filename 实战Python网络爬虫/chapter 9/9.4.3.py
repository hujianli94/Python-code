from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获取输入框标签对象
element = driver.find_element_by_id('kw')
# 输入框输入内容
element.send_keys("Python你")
time.sleep(2)

# 删除最后的一个文字
element.send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 添加输入空格键 + “教程”
element.send_keys(Keys.SPACE)
element.send_keys("教程")
time.sleep(2)

# ctrl+a 全选输入框内容
element.send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# ctrl+x 剪切输入框内容
element.send_keys(Keys.CONTROL, 'x')
time.sleep(2)

# ctrl+v 粘贴内容到输入框
element.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 通过回车键来代替单击操作
driver.find_element_by_id('su').send_keys(Keys.ENTER)
