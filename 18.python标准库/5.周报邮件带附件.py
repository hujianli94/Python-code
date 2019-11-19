#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/4/17 15:18
# filename: 5.周报邮件带附件.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase  # MIME子类的基类
from email import encoders  # 导入编码器

HOST = "smtp.qq.com"
SUBJECT = u"官网业务服务质量周报"
TO = "13262662216@163.com"
FROM = "1879324764@qq.com"


def addimg(src, imgid):
    '''
    :param src: 图片路径
    :param imgid: 图片id
    :return:
    '''
    fp = open(src, 'rb')  # 打开文件
    msgImage = MIMEImage(fp.read())  # 创建MIMEImage对象，读取图片内容作为参数
    fp.close()  # 关闭文件
    msgImage.add_header('Content-ID', imgid)  # 指定图片文件的Content-ID
    return msgImage  # 返回msgImage对象


# 创建一个带附件的实例
msg = MIMEMultipart('related')
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO

# 邮件正文内容
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>", "html",
                   "utf-8")
msg.attach(msgtext)  # 将msgtext内容附加到MIMEMultipart对象中
msg.attach(addimg("img/manhua.png", 'weekly'))  # 使用MIMEMultipart对象附加MIMEImage的内容

# 附件文件1定义
# 创建一个MIMEText对象，附加表格文件（week.xlsx）
Path = "doc/"
filename = '华为云Fusioncloud整体规划.xlsx'
attachfile = MIMEBase('applocation', 'octet-stream')  # 创建对象指定主要类型和次要类型
attachfile.set_payload(open(Path + filename, 'rb').read())  # 将消息内容设置为有效载荷
attachfile.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))  # 扩展标题设置
encoders.encode_base64(attachfile)
msg.attach(attachfile)  # 附加对象加入到msg


# 附件文件2定义
# 创建一个MIMEText对象，附加表格文件（xxx.png）
Path = "img/"
filename = 'manhua.png'
attachfile_png = MIMEBase('applocation', 'octet-stream')  # 创建对象指定主要类型和次要类型
attachfile_png.set_payload(open(Path + filename, 'rb').read())  # 将消息内容设置为有效载荷
attachfile_png.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))  # 扩展标题设置
encoders.encode_base64(attachfile_png)
msg.attach(attachfile_png)  # 附加对象加入到msg


# 附件文件3定义
# 创建一个MIMEText对象，附加表格文件（xxx.pdf）
filename = 'Java从小白到大牛.pdf'
attachfile_pdf = MIMEBase('applocation', 'octet-stream')  # 创建对象指定主要类型和次要类型
attachfile_pdf.set_payload(open(filename, 'rb').read())  # 将消息内容设置为有效载荷
attachfile_pdf.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))  # 扩展标题设置
encoders.encode_base64(attachfile_pdf)
msg.attach(attachfile_pdf)  # 附加对象加入到msg

"""
smtpObj = smtplib.SMTP([host [, port [, local_hostname]]])
语法中各个参数说明如下。 
host: SMTP服务器主机。可以指定主机的IP地址或域名（如www.baidu.com），是可选参数。 
port：如果提供了host参数，就需要指定SMTP服务使用的端口号。一般情况下SMTP的端口号为25。 
local_hostname：如果SMTP在本地主机上，只需要指定服务器地址为localhost即可。


SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
语法中各个参数说明如下。

from_addr：邮件发送者的地址。
to_addrs：字符串列表，邮件发送地址。
msg：发送消息。
"""
# try:
#     server = smtplib.SMTP()
#     server.connect(HOST, "25")        ##通过 connect 方法连接 smtp 主机
#     server.starttls()                 ## 启动安全传输模式
#     server.login("1879324764@qq.com", "ducszyrzqulyhjeg") # 邮箱账号登录校验
#     server.sendmail(FROM, TO, msg.as_string())    # 邮件发送
#     server.quit()                     # 断开 smtp 连接
#     print("邮件发送成功！")
# except Exception as e:
#     print("失败：" + str(e))

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login("1879324764@qq.com", "ducszyrzqulyhjeg")
    smtpObj.sendmail(FROM, TO, msg.as_string())
    print('邮件发送成功....')
except smtplib.SMTPException as e:
    print('Error :无法发送邮件.Case:{}'.format(e))

finally:
    smtpObj.close()
