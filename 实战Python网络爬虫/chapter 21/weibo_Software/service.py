from PyQt5 import QtCore, QtGui, QtWidgets
from weibo_service import Ui_Dialog
import requests
import configparser
import os
import sys

# 相关服务的功能逻辑
class weibo_service_logic(QtWidgets.QWidget, Ui_Dialog):
    # 重写初始化函数
    def __init__(self, parent=None):
        super(weibo_service_logic, self).__init__(parent)
        self.setupUi(self)
        # 设置左上方的logo
        self.setWindowIcon(QtGui.QIcon('ico/logo.png'))
        # 设置按钮'购买打码服务'的功能
        self.buy_code.clicked.connect(self.buy_code_def)
        # 设置按钮'购买代理服务'的功能
        self.buy_proxy.clicked.connect(self.buy_proxy_def)
        # 设置打码服务的按钮'验证'的功能
        self.code_bt.clicked.connect(self.set_code)
        # 设置代理服务的按钮'验证'的功能
        self.proxy_bt.clicked.connect(self.set_proxy)
        # 设置打码服务的按钮'清空'的功能
        self.code_clean.clicked.connect(self.code_clean_def)
        # 设置代理服务的按钮'清空'的功能
        self.proxy_clean.clicked.connect(self.proxy_clean_def)

        # 读取配置文件，软件再次运行无需重复设置
        conf = configparser.ConfigParser()
        if os.path.exists('./temp/conf.ini'):
            conf.read('./temp/conf.ini')
            if 'config' in conf.keys():
                temp = conf['config']
                if 'proxies' in temp.keys():
                    self.proxy_text.setText(conf['config']['proxies'])
                if 'user' in temp.keys():
                    self.code_account.setText(conf['config']['user'])
                if 'password' in temp.keys():
                    self.code_password.setText(conf['config']['password'])

    # 购买打码服务
    def buy_code_def(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.yundama.com/'))

    # 购买代理IP服务
    def buy_proxy_def(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.data5u.com/?developer=dac1a741824a5bfd87eb04a27216f2f8'))

    # 验证单号
    def set_proxy(self):
        proxy_key = self.proxy_text.text().strip()
        if proxy_key:
            # 获取代理IP
            url = 'http://api.ip.data5u.com/dynamic/get.html?order=' + proxy_key + '&random=true&sep=5'
            r = requests.get(url)
            # 判断IP代理是否过期
            if 'success' in str(r.text):
                warm_info = '单号未充值或者单号已经到期'
            else:
                warm_info = '验证成功'
                # 写入配置文件
                conf = configparser.ConfigParser()
                if os.path.exists('./temp/conf.ini'):
                    conf.read('./temp/conf.ini')
                else:
                    conf.add_section('config')
                conf.set('config', 'proxies', proxy_key)
                conf.write(open('./temp/conf.ini', 'w'))

        else:
            warm_info = '请输入单号'
        self.proxy_status.setText(warm_info)

    # 验证打码服务
    def set_code(self):
        username = self.code_account.text().strip()
        password = self.code_password.text().strip()
        url = 'http://api.yundama.com/api.php?method=balance'
        data = {'username': username, 'password': password,
                'appkey': 'c5e26d1a207df586d7aaec21522dd446',
                'appid': '4055'}
        r = requests.post(url, data=data)
        if r.json()['ret'] == 0:
            # 账号正常
            # 写入配置文件
            conf = configparser.ConfigParser()
            if os.path.exists('./temp/conf.ini'):
                conf.read('./temp/conf.ini')
            else:
                conf.add_section('config')
            conf.set('config', 'yunmauser', username)
            conf.set('config', 'yunmapassword', password)
            conf.write(open('./temp/conf.ini', 'w'))

            self.proxy_status.setText('验证成功,余额为' + str(r.json()['balance']))
        elif r.json()['ret'] == -1001:
            self.proxy_status.setText('打码平台账号密码错误')
        elif r.json()['ret'] == -1007:
            self.proxy_status.setText('打码平台余额为0，请及时充值')

    # 清空单号设置
    def proxy_clean_def(self):
        conf = configparser.ConfigParser()
        if os.path.exists('./temp/conf.ini'):
            conf.read('./temp/conf.ini')
            conf.set('config', 'proxies', '')
            conf.write(open('./temp/conf.ini', 'w'))
        self.proxy_status.setText('已清空单号')
        self.proxy_text.setText('')

    # 清空打码设置
    def code_clean_def(self):
        conf = configparser.ConfigParser()
        if os.path.exists('./temp/conf.ini'):
            conf.read('./temp/conf.ini')
            conf.set('config', 'yunmauser', '')
            conf.set('config', 'yunmapassword', '')
            conf.write(open('./temp/conf.ini', 'w'))
        self.proxy_status.setText('已清空打码平台账号密码')
        self.code_account.setText('')
        self.code_password.setText('')

    # 运行界面
    def show_win(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.show()
    # 关闭界面
    def close_win(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = weibo_service_logic()
    ex.show()
    sys.exit(app.exec_())
