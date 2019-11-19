from appium import webdriver
import time
# 延时与检测系统提示
def check_and_delay(ts=10):
    time.sleep(ts)
    try:
        driver.find_element_by_id('android:id/button1').click()
    except: pass

# 获得屏幕坐标x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

# 屏幕向上滑动
def swipeUp(t):
    local = getSize()
    x = int(local[0] * 0.75)
    y1 = int(local[1] * 0.75)
    y2 = int(local[1] * 0.25)
    driver.swipe(x, y1, x, y2, t)

if __name__ == '__main__':
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0',
        'deviceName': 'huawei-lld_al20-30KNW18730002140',
        'appPackage': 'com.taobao.taobao',
        'appActivity': 'com.taobao.tao.homepage.MainActivity3',
        # 设置中文输入
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # 点击首页搜索框
    # 延时20秒是更好地等待系统提示框的出现
    check_and_delay(20)
    resourceId = 'com.taobao.taobao:id/home_searchedit'
    driver.find_element_by_id(resourceId).click()
    check_and_delay()
    # 点击搜索页的搜索框
    text = '玩转Python网络爬虫'
    resourceId = 'com.taobao.taobao:id/searchEdit'
    driver.find_element_by_id(resourceId).send_keys(text)
    check_and_delay()
    # 输入搜索内容
    resourceId = 'com.taobao.taobao:id/searchbtn'
    driver.find_element_by_id(resourceId).click()
    check_and_delay()
    # 点击销量排序
    sales = 'new UiSelector().description("销量")'
    driver.find_element_by_android_uiautomator(sales).click()
    check_and_delay()
    # 数据写入
    MyList = []
    for t in range(5):
        resourceId = 'com.taobao.taobao:id/auction_layout'
        info = driver.find_elements_by_id(resourceId)
        check_and_delay()
        for i in info:
            try:
                MyDict = {}
                # 获取标题
                resourceId = 'com.taobao.taobao:id/title'
                title = i.find_element_by_id(resourceId)
                MyDict['title'] = title.text.strip()
                # 获取价格
                resourceId = 'com.taobao.taobao:id/priceBlock'
                price = i.find_element_by_id(resourceId)
                MyDict['price'] = price.get_attribute("contentDescription")
                # 去重并写入列表
                if MyDict not in MyList:
                    MyList.append(MyDict)
            except: pass
        # 滑动屏幕
        swipeUp(1000)
    print(MyList)
    # 关闭淘宝App
    driver.quit()
