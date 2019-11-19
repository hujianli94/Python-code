#!/usr/bin/env python
#-*- coding:utf8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#通过SMTP发出去
#Email地址和口令
from_addr = "1879324764@qq.com"
from_passwd = "rpesbfgwmqcycceh"   #使用网页邮件中生成的授权码
#收件人地址
to_addr = "13262662216@163.com"
#SMTP服务器地址
smtp_server = "smtp.qq.com"


msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('%s %s <%s>' % ("hujianli","test",from_addr))
msg['To'] = _format_addr('收件者 <%s>' % to_addr)
msg['Subject'] = Header('邮件的主题信息……', 'utf-8').encode()


if __name__ == '__main__':
    #开始发送邮件
    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, from_passwd)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)



#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1879324764@qq.com"   #用户名
mail_pass="rpesbfgwmqcycceh"  #口令


sender = "1879324764@qq.com"
receivers = ["13262662216@163.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")


#!/usr/bin/env python
#-*- coding:utf8 -*-
import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT =25


def send_mail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    smtp_server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    print("Connecting to mail server.")

    try:
        smtp_server.ehlo()
        print("Starting Encrypted Seccion.")

        smtp_server.starttls()
        smtp_server.ehlo()
        print("Logging Into Mail Server")

        smtp_server.login(user,pwd)
        print("Sending mail ..")

        smtp_server.sendmail(user,to,msg.as_string())
    except Exception as err:
        print("Sending Mail Failed :{0}".format(err))
    finally:
        smtp_server.quit()


def main():
    send_mail('1879324764@qq.com','qvhsgcjnkvyccedc','13262662216@163.com','Inportant','Test message')

if __name__ == '__main__':
    main()