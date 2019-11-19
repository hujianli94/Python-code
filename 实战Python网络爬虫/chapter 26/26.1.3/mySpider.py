import requests
import time
while 1:
    # 读取配置文件的任务内容
    taskFile = open(r'd:\\spider\\task.txt')
    task = taskFile.read()
    taskFile.close()
    for i, url in enumerate(task.split(',')):
        if url:
            r = requests.get(url)
            path = r'd:\\spider\\%s.txt' %(str(i))
            f = open(path, 'w',encoding='utf-8')
            f.write(r.text)
            f.close()
    # 清空配置文件的任务内容
    taskFile = open(r'd:\\spider\\task.txt', 'w')
    taskFile.write('')
    taskFile.close()
    time.sleep(10)
