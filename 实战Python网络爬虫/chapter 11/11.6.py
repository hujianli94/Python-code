import asyncio
from aiohttp import ClientSession
# 导入数据清洗库BeautifulSoup
from bs4 import BeautifulSoup
# 导入内置的CSV库
import csv

# 定义网站访问函数getData，将网站内容返回
async def getData(url, headers):
    #  创建会话对象session
    async with ClientSession() as session:
        # 发送GET请求，并设置请求头
        async with session.get(url, headers=headers) as response:
            # 返回响应内容
            return await response.text()

def savaData(result):
    for i in result:
        soup = BeautifulSoup(i, 'html.parser')
        find_div = soup.find_all('div',class_='book-mid-info')
        for d in find_div:
            name = d.find('h4').getText()
            author = d.find('a',class_='name').getText()
            update = d.find('p',class_='update').getText()
            # 写入CSV文件
            csvFile = open('data.csv','a', newline='')
            writer = csv.writer(csvFile)
            writer.writerow([name,author,update])
            csvFile.close()

# 定义运行函数run
def run():
    for i in range(25):
        # 构建不同的URL地址并传入函数getData，最后由asyncio模块执行
        task = asyncio.ensure_future(getData(url.format(i+1),headers))
        # 将所有请求加入到列表tasks
        tasks.append(task)
        # 等待所有请求执行完成，一并返回全部的响应内容
    result = loop.run_until_complete(asyncio.gather(*tasks))
    savaData(result)
    print(len(result))

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    tasks = []
    url = "https://www.qidian.com/rank/hotsales?page={}"
    # 创建get_event_loop对象
    loop = asyncio.get_event_loop()
    # 调用函数run
    run()