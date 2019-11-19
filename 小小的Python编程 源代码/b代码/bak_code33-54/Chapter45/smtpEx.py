#邮件发送程序
#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

#邮件发送程序
def mail():
    #发信人邮局
    senderEmail ="xiaoxiao@sina.com"    #请根据实际情况修改此处邮箱地址
    senderPassword = "19990909"             #请根据实际情况修改此处邮箱密码，但不要泄漏给别人

    #收件人
    receiveEmail=input("收件人：")
    subject=input("主题：")
    
    #写邮件
    print("正文：")
    txt_mail = "    "             #存储多行文本
    for line in iter(input, ""):
        txt_mail+=line+"\n"

    #发送邮件
    ret=True
    try:
        msg=MIMEText(txt_mail,'plain','utf-8')
        msg['From']=formataddr(["发件人邮箱昵称",senderEmail])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人邮箱昵称",receiveEmail])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=subject #邮件的标题

        server=smtplib.SMTP("smtp.sina.com",25)     #发件人邮箱中的SMTP服务器，端口是25
        server.login(senderEmail,senderPassword)    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(senderEmail,[receiveEmail,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送的邮件
        server.quit()   #关闭连接
    except Exception:   #如果try中的语句没有成功执行，则会执行下面的ret=False
        ret=False
        #raise
    return ret

#发邮件
ret=mail()
if ret:
    print("邮件已发送。") #如果发送成功
else:
    print("发送失败！")  #如果发送失败
