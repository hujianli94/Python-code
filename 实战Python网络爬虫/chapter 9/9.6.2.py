from selenium import webdriver
import json, time
url = 'https://zhidao.baidu.com/list?cid=110'
driver = webdriver.Chrome()
driver.get(url)
# 使用Cookies登录
driver.delete_all_cookies()
f1 = open('cookie.txt')
cookie =json.loads(f1.read())
f1.close()
for c in cookie:
    driver.add_cookie(c)
driver.refresh()

# 获取问题列表
title_link = driver.find_elements_by_class_name('title-link')
for i in title_link:
    # 打开问题详细页并切换窗口
    driver.switch_to.window(driver.window_handles[0])
    href = i.get_attribute('href')
    driver.execute_script('window.open("%s");' % (href))
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    try:
        # 查找iframe，判断问题是否已被回答
        driver.find_element_by_id('ueditor_0')
        # 获取问题题目并搜索答案
        title = driver.find_element_by_class_name('ask-title ').text
        title_url = 'https://zhidao.baidu.com/search?&word=' + title
        js = 'window.open("%s");' % (title_url)
        driver.execute_script(js)
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        # 获取答案列表
        answer_list = driver.find_elements_by_class_name('dt,mb-4,line')
        for k in answer_list:
            # 打开答案详细页
            href = k.find_element_by_tag_name('a').get_attribute('href')
            driver.execute_script('window.open("%s");' % (href))
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[3])
            # 获取最佳答案
            try:
                text = driver.find_element_by_class_name('best-text,mb-10').text
            except:
                text = ''
            finally:
                # 关闭答案详情页的窗口
                driver.close()
            # 答案不为空
            if text:
                # 关闭答案列表页的窗口
                driver.switch_to.window(driver.window_handles[2])
                driver.close()
                # 将答案写在问题回答文本框上并点击提交答案按钮
                driver.switch_to.window(driver.window_handles[1])
                driver.switch_to.frame('ueditor_0')
                driver.find_element_by_xpath('/html/body').click()
                driver.find_element_by_xpath('/html/body').send_keys(text)
                # 跳回到网页的HTML
                driver.switch_to.default_content()
                # 点击提交回答按钮
                driver.find_element_by_xpath('//*[@id="answer-editor"]/div[2]/a').click()
                time.sleep(5)
                # 关闭问题详细页的窗口
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                break

    except Exception as err:
        # 除了问题列表页，关闭其他窗口
        all_handles = driver.window_handles
        for i, v in enumerate(all_handles):
            if i != 0:
                driver.switch_to.window(v)
                driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print(err)

