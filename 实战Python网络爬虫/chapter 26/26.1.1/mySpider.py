import requests
url = 'https://www.python.org/'
r = requests.get(url)
f = open(r'd:\\spider\\data.txt', 'w')
f.write(r.text)
f.close()
