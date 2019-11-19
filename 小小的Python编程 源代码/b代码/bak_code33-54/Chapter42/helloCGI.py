#!C:\Users\lgd\AppData\Local\Programs\Python\Python36\python.exe

import random
menu=('黑森林蛋糕','布朗尼蛋糕','舒芙里','提拉米苏','瑞士卷')
cake=random.choice(menu)

print ("Content-type:text/html;charset=gbk")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>第一个CGI程序</title>')
print ('</head>')
print ('<body>')

print ('<h2>Hello Everyone! ',u'我是来自小小蛋糕店的',cake,'</h2>')
print ('</body>')
print ('</html>')
