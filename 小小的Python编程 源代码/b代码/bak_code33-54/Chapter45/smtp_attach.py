#邮件附件 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
sender = 'xiaoxiao@sina.com'    #发件人邮箱，请改成有效邮箱
senderPSW='19990909'      #发件人邮箱密码，请勿泄漏
receivers = ['jisenfellow@sina.com']  # 接收人邮箱，请改成有效邮箱
 
#创建一个带附件的邮件对象
msg = MIMEMultipart()
msg['From'] = Header(sender)
msg['To'] =  Header('吉森老伙计','utf-8')
subject = '我是小小'
msg['Subject'] = Header(subject,'utf-8')
 
#邮件正文内容
mail_body=MIMEText('亲爱的吉森你好，附件是我的情况和图片。', 'plain', 'utf-8')
msg.attach(mail_body)
 
# 附件1，传送当前目录下的 me.txt 文件
att1 = MIMEText(open('me.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename是附件的显示名，可以任意写，中文可能会显示成其他字符
att1["Content-Disposition"] = 'attachment; filename="xiaoxiaoTXT"'
msg.attach(att1)
 
# 附件2，传送当前目录下的 me.jpg 文件
att2 = MIMEText(open('me.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="xiaoxiaoJPG"'
msg.attach(att2)
 
try:
    smtpObj = smtplib.SMTP('smtp.sina.com',25)  #请改成实际使用的邮件服务器
    smtpObj.login(sender,senderPSW)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

