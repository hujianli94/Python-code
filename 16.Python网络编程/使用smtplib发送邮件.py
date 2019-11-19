#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
smtplib 标准库的使用
SMTP(host,port,local_hostname)
host:连接服务器名，可选参数；
port:服务器端口，可选参数
local_hostname：本地主机名，可选参数

login(user, password)
- user:         The user name to authenticate with.
- password:     The password for the authentication.

sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[]):
- from_addr    : The address sending this mail.
- to_addrs     : A list of addresses to send this mail to.  A bare
                 string will be treated as a list with 1 address.
- msg          : The message to send.
- mail_options : List of ESMTP options (such as 8bitmime) for the
                 mail command.
- rcpt_options : List of ESMTP options (such as DSN commands) for
                             all the rcpt commands

'''
import smtplib, email
chst = email.charset.Charset(input_charset='utf-8')
header = ('From:%s\nTo:%s\nSubject:%s\n\n'
          % ("13262662216@163.com",
             "hujianli94@126.com",
             chst.header_encode("您好，我是胡建力，Python smtplib 测试！")))
body = "你好！我是胡建力，我在发一封测试邮件！ "
email_con = header.encode("utf-8") + body.encode("utf-8")
smtp = smtplib.SMTP("smtp.163.com")
smtp.login("13262662216@163.com","cu0gu0ai@94")
smtp.sendmail('13262662216@163.com','1879324764@qq.com',email_con)
#Terminate the SMTP session.
smtp.quit()