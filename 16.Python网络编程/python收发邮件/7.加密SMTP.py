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
smtp_port = 587
server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)


msg = MIMEText('<html><body><h1>小健的博客</h1>' +
    '<p>博客浏览地址: <a href="https://xiaojian722.readthedocs.io/en/latest/index.html">小健的自动化运维之路</a> 开启学习旅程</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('%s %s <%s>' % ("hujianli","test",from_addr))
msg['To'] = _format_addr('收件者 <%s>' % to_addr)
msg['Subject'] = Header('邮件的主题信息……', 'utf-8').encode()
try:
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, from_passwd)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print("邮件发送成功！")
except Exception as e:
    print("email 发送失败",e)