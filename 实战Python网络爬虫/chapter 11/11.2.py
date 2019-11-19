import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
target_url = 'https://y.qq.com/portal/singer_list.html'

# render.html获取JS加载后的网页信息
url = 'http://192.168.99.100:8050/render.html?url='+target_url+'&wait=5'
response = requests.get(url, headers=headers)
print(response.text)

# render.png获取网页截图
url = 'http://192.168.99.100:8050/render.png?url='+target_url+'&width=500&height=500'
response = requests.get(url, headers=headers)
with open('image.png', 'wb') as f:
    f.write(response.content)

# render.json返回请求数据
url = 'http://192.168.99.100:8050/render.json?url='+target_url+'&wait=5'
response = requests.get(url, headers=headers)
print(response.text)

# execute执行Lua脚本
# 因为Splash支持Lua脚本操作
import requests
from urllib.parse import quote
luaScript = '''
function main(splash)
    return 'Python'
end
'''
# Lua脚本转码处理
url = 'http://192.168.99.100:8050/execute?lua_source=' + quote(luaScript)
response = requests.get(url)
print(response.text)
