#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

Python创建 SMTP 对象语法如下：

import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
参数说明：

host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。
Python SMTP 对象使用 sendmail 方法发送邮件，语法如下：

SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
参数说明：

from_addr: 邮件发送者地址。
to_addrs: 字符串列表，邮件发送地址。
msg: 发送消息
这里要注意一下第三个参数，msg 是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。这个格式就是 smtp 协议中定义的格式。
'''

#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("hello,send by Python....你好.", 'plain', 'utf-8')
#注意到构造MIMEText对象时
# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。


#通过SMTP发出去
#Email地址和口令
from_addr = "1879324764@qq.com"
from_passwd = "rpesbfgwmqcycceh"   #使用网页邮件中生成的授权码
#收件人地址
to_addr = "13262662216@163.com"
#SMTP服务器地址
smtp_server = "smtp.qq.com"

try:
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, from_passwd)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
except Exception as e:
    print(e)