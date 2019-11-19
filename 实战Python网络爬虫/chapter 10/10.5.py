from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'huawei-lld_al20-30KNW18730002140',
    'appPackage': 'com.sankuai.meituan',
    'appActivity': 'com.meituan.android.pt.homepage.activity.MainActivity',
    # 设置中文输入
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
# 向Appium-Server发送请求实现连接
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
# 点击系统提示框
for i in range(2):
    resourceId = 'com.android.packageinstaller:id/permission_allow_button'
    driver.find_element_by_id(resourceId).click()
    time.sleep(3)
# 点击首页输入框
resourceId = 'com.sankuai.meituan:id/search_edit'
driver.find_element_by_id(resourceId).click()
time.sleep(3)
# 输入搜索内容
resourceId = 'com.sankuai.meituan:id/search_edit'
driver.find_element_by_id(resourceId).send_keys('广州长隆')


# 获得手机屏幕分辨率x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
	
# 向上滑动
def swipeUp(t):
    local = getSize()
    x = int(local[0] * 0.5)
    y1 = int(local[1] * 0.75)
    y2 = int(local[1] * 0.25)
    driver.swipe(x, y1, x, y2, t)
	
# 向下滑动
def swipeDown(t):
    local = getSize()
    x = int(local[0] * 0.5)
    y1 = int(local[1] * 0.25)
    y2 = int(local[1] * 0.75)
    driver.swipe(x, y1, x, y2, t)
	
# 向左滑动
def swipLeft(t):
    local = getSize()
    x1 = int(local[0] * 0.75)
    y = int(local[1] * 0.5)
    x2 = int(local[0] * 0.05)
    driver.swipe(x1, y, x2, y, t)
	
# 向右滑动
def swipRight(t):
    local = getSize()
    x1 = int(local[0] * 0.05)
    y = int(local[1] * 0.5)
    x2 = int(local[0] * 0.75)
    driver.swipe(x1, y, x2, y, t)
