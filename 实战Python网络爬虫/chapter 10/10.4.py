# 通过index定位
# Appium的uiautomator方法
index = '28'
ua = 'new UiSelector().index(' + index + ')'
driver.find_element_by_android_uiautomator(ua).click()

# 通过text定位
# Appium的uiautomator方法
text = '6'
ua = 'new UiSelector().text("' + text + '")'
driver.find_element_by_android_uiautomator(ua).click()

# 通过resource-id定位
resourceId = 'com.android.calculator2:id/digit_6'
# Selenium的方法
driver.find_element_by_id(resourceId)
# Appium的uiautomator方法
ua = 'new UiSelector().resourceId("' + resourceId + '")'
driver.find_element_by_android_uiautomator(ua).click()

# 通过class定位
# Selenium的方法
class_name = 'android.widget.Button'
driver.find_element_by_class_name(class_name)

# 通过content-desc定位
# Appium的uiautomator方法
# 由于数字6的属性值为空，此处选取按键C
description = '清除'
ua = 'new UiSelector().description("' + description + '")'
driver.find_element_by_android_uiautomator(ua).click()
# 方法二
driver.find_element_by_accessibility_id('清除').click()

# Xpath定位
xpath = '//android.widget.Button[contains(@text,"6")]'
driver.find_element_by_xpath(xpath).click()
