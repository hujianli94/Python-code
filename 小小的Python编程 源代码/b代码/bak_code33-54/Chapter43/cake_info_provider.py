#!C:\Users\lgd\AppData\Local\Programs\Python\Python36\python.exe

# CGI处理模块
import cgi, cgitb 

# 创建 FieldStorage 实例
form = cgi.FieldStorage() 

# 获取数据
customerName = form.getvalue('customer_name')
cakeName  = form.getvalue('cake_name')

#蛋糕数据
cake_dict={'提拉米苏':'提拉米苏（Tiramisù），为一种有名的意大利式蛋糕，又可译成堤拉米苏。提拉米苏是由泡过咖啡或兰姆酒的手指饼干，加上一层马斯卡彭、蛋黄、干酪、糖的混合物，然后再在蛋糕表面洒上一层可可粉而成。',
       '瑞士卷':'瑞士卷是海绵蛋糕（sponge cake）的一种。在烤炉中将材料烤成薄薄的蛋糕，加上了果酱和奶油（混糖奶油，牛奶蛋糊奶油等），和切碎了的果肉，卷成卷状。另外可以加上混和的可可粉和咖啡粉，形成松软的海绵质感的卷蛋糕。',
       '黑森林':'黑森林蛋糕(Schwarzwaelder Kirschtorte)是德国著名甜点，制作原料主要有脆饼面团底托、鲜奶油、樱桃酒等。是受德国法律保护的甜点之一，在德文里全名"Schwarzwaelder" 即为黑森林。它融合了樱桃的酸、奶油的甜、樱桃酒的醇香。'}
if cakeName in cake_dict.keys():
    cakeInfo=cake_dict[cakeName]
else:
    cakeInfo="暂无进一步信息"
    cakeName="未知"
if customerName==None or cutomerName=='':
    customerName='未知'
print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>获取蛋糕信息</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s顾客您好，您查询的：%s蛋糕信息如下：%s</h2>" % (customerName,cakeName,cakeInfo))
print ("</body>")
print ("</html>")
