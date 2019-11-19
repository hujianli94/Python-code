from appium import webdriver
desired_caps = {}
# 设置Android系统信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'huawei-lld_al20-30KNW18730002140'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
# 向Appium-Server发送请求实现连接
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
