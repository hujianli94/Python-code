# ！/usr/bin/env python
# -*-coding:utf-8 -*-

#需求2:发送邮件正文加附件

import time
import smtplib

from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(info,file_paths):
    # 发件人地址
    from_addr = '1879324764@qq.com'
    # 邮箱密码
    password = 'rpesbfgwmqcycceh'
    # 收件人地址,可同时添加多个
    to_addrs = [
        '13262662216@163.com',
        'hujl<hujl@futongcloud.com.cn>',
    ]
    # 邮箱服务器地址
    smtp_server = 'smtp.qq.com'

    local_time = time.strftime('%Y-%m-%d %H:%M:%S')

    content = '''
        小伙伴们，everybody
        {info}
        邮件发送时间时间: {local_time}
    '''.format(info=info, local_time=local_time)
    # 设置邮件信息
    msg = MIMEMultipart()
    body = MIMEText(content.encode(), 'plain', 'utf-8')
    msg.attach(body)


    # 构造附件
    for file_name in file_paths:
        attachment = MIMEBase('application', 'octet-stream')#参数的意义未深究
        attachment.set_payload(open(file_name, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition','attachment', filename=file_name)# 前2个参数意义未深究
        msg.attach(attachment)

    msg['From'] = _format_addr('胡小健 <%s>' % from_addr)
    msg['To'] = _format_addr('501运维小伙子们 <%s>' % to_addrs)
    msg['Subject'] = Header('活动计划表', 'utf-8').encode()

    # 发送邮件
    server = smtplib.SMTP_SSL(host=smtp_server, port=465)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addrs=to_addrs, msg=msg.as_string())

    server.quit()

if __name__ == '__main__':
    info = '''
        早上好,吃饭了吗~
        小胡，小健，小力。小肥脸、林梦成
    '''
    file_paths=["1.SMTP发送邮件_test.py"]
    send_email(info, file_paths)



import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '1879324764@qq.com'
#pwd为qq邮箱的授权码
pwd = 'qvhsgcjnkvyccedc' ##
#发件人的邮箱
sender_qq_mail = '1879324764@qq.com'
#收件人邮箱
receiver = '13262662216@163.com'

#邮件的正文内容
mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"
#邮件标题
mail_title = 'Maxsu的邮件'

#邮件正文内容
msg = MIMEMultipart()
#msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

#邮件正文内容
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))


# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('发送邮件.py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="sedmain1.py"'
msg.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('check_port.py', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="check_port.py"'
msg.attach(att2)


#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
