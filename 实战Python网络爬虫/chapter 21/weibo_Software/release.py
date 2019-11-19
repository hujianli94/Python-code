from PyQt5 import QtCore, QtGui, QtWidgets
from weibo_release import Ui_Dialog
from weibo import *
from PyQt5.QtCore import QBasicTimer
import csv, time, datetime
import os, configparser
import requests
import sys


# 微博发布
class weibo_release_logic(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(weibo_release_logic, self).__init__(parent)
        self.setupUi(self)
        # 设置logo
        self.setWindowIcon(QtGui.QIcon('ico/logo.png'))
        # 设置数据表格
        self.release_table.setHorizontalHeaderLabels(['账号', '密码', '内容', '图片', '定时发布'])
        self.release_table.setRowCount(1)
        # 表格绑定tableset，让表格自动添加行数
        self.release_table.currentCellChanged['int', 'int', 'int', 'int'].connect(self.tableset)
        # 设置表格的表头
        self.release_table.verticalHeader().setStyleSheet("QHeaderView::section {background:rgb(230, 230, 230)}")
        self.release_table.horizontalHeader().setStyleSheet("QHeaderView::section {background:rgb(230, 230, 230)}")

        # 导入CSV
        self.importcsv.clicked.connect(self.importcsv_def)
        # 导出CSV
        self.exportcsv.clicked.connect(self.exportcsv_def)
        # 图片按钮绑定功能函数
        self.release_pic.clicked.connect(self.showDialog)
        # 发布按钮绑定功能函数
        self.release_bt.clicked.connect(self.timer_and_weibo)
        # 验证代理按钮绑定功能函数
        self.user_check_proxy.clicked.connect(self.check_proxy)
        # 数据表格设定键盘事件
        self.release_table.activated['QModelIndex'].connect(self.keyPressEvent)

        # 定时发布设置
        now = datetime.datetime.now()
        now_year = now.strftime('%Y')
        now_month = now.strftime('%m')
        now_day = now.strftime('%d')
        now_hour = now.strftime('%H')
        now_minute = now.strftime('%M')
        self.dateEdit.setDate(QtCore.QDate(int(now_year), int(now_month), int(now_day)))
        # 将定时发送的时间设置为当前时间
        self.hour.setCurrentText(now_hour)
        self.minute.setCurrentText(now_minute)
        # 当时间控件发生改变而触发的方法，判断设定的时间是否符合微博的延时发送
        self.hour.currentIndexChanged['int'].connect(self.set_time)
        self.minute.currentIndexChanged['int'].connect(self.set_time)
        self.dateEdit.dateChanged['QDate'].connect(self.set_time)
        # 初始化类属性
        self.pic_list = []
        self.timer = QBasicTimer()
        self.step = 0
        self.index = 0
        self.row_number_list = []
        self.session_dict = {}

    # 定义键盘事件，用于快速删除数据表格的整行数据
    def keyPressEvent(self, e):
        keyEvent = QtGui.QKeyEvent(e)
        getrow = self.release_table.currentRow()
        if keyEvent.key() == QtCore.Qt.Key_Delete:
            self.release_table.removeRow(getrow)
            self.tableset()

    # 发博微博
    def release_weibo(self):
        # 验证用户和发布微博,先判断用户登录状态
        self.check_proxy()
        # 登录验证用户
        username = self.release_table.item(self.row_number_list[self.index], 0).text().strip()
        password = self.release_table.item(self.row_number_list[self.index], 1).text().strip()
        # 判断是否已登录过
        if username in self.session_dict.keys() and self.proxies == {}:
            user = self.session_dict[username]
            time.sleep(3)
        else:
            user = login(username, password, proxies=self.proxies)
        # 登录成功
        if user['code'] == '1000':
            # 写入session_dict
            self.session_dict[username] = user
            # 获取登录信息
            session = user['session']
            person_info = user['info']
            location = person_info['location']
            watermark = person_info['watermark']
            nick = person_info['nick']
            # 判断是否有图片
            pic = self.release_table.item(self.row_number_list[self.index], 3)
            if pic:
                if pic.text():
                    for i in pic.text().split(','):
                        i = i.replace(r'\\', '')
                        if os.path.exists(i):
                            self.pic_list.append(i)
            # 设置函数参数
            self.value = self.release_table.item(self.row_number_list[self.index], 2).text()
            try:
                self.addtime = self.release_table.item(self.row_number_list[self.index], 4).text()
            except:
                self.addtime = ''
            # 上存图片
            if self.pic_list:
                pic_list = upload_pic(watermark, nick, session, file_list=self.pic_list, proxies=self.proxies)
                send_type = 'pic'
                self.pic_list = []
            else:
                pic_list = []
                send_type = 'words'
            # 发送微博
            send_status = send_weibo(watermark, location, self.value, session, self.addtime, pic_id_list=pic_list,
                                     send_type=send_type, proxies=self.proxies)
            if send_status:
                status_info = '用户：' + username + ' 微博发布成功' + '\n'
                # 设置当前表格所在行的颜色,绿色
                self.fill_rpg(127, 255, 170)
                self.success_number += 1
            else:
                status_info = '用户：' + username + ' 微博发布失败' + '\n'
                self.fail_number += 1
            # 写入状态信息
            self.state_value.setPlainText(status_info + self.warm_info + self.state_value.toPlainText())
        # 登录失败
        elif user['code'] == '1001':
            self.state_value.setPlainText(
                '用户：' + username + ' 登录失败,失败原因：微博账号密码错误或者验证码识别错误' + '\n' + self.state_value.toPlainText())
            # 设置当前表格所在行的颜色，黄色
            self.fill_rpg(255, 255, 0)
            self.fail_number += 1
        elif user['code'] == '1002':
            self.state_value.setPlainText(
                '用户：' + username + ' 登录失败,失败原因：验证码账号密码错误或者余额不足' + '\n' + self.state_value.toPlainText())
            # 设置当前表格所在行的颜色，棕色
            self.fill_rpg(244, 164, 96)
            self.fail_number += 1
        self.index += 1

    # 定义进度条
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.release_bt.setText('发布')
            self.state_value.setPlainText('发布完成：成功 ' + str(self.success_number) + ' 个，失败 ' + str(
                self.fail_number) + ' 个' + '\n' + self.state_value.toPlainText())
            self.step = 0
            self.row_number_list = []
            self.index = 0
            self.proxies = {}
            self.warm_info = ''
            self.pic_list = []
            self.value = ''
            return
        # 发博微博
        self.release_weibo()
        # 延时，等待下一个
        self.step = self.step + self.speed
        time.sleep(self.time_delay)
        self.progressBar.setValue(self.step)

    # 进度条、按钮和微博发布结合使用
    def timer_and_weibo(self):
        if self.step == 0:
            # 初始化
            # 初始化软件要求
            self.step = 0
            self.speed = 0
            # 计算发布的延时时间
            self.time_delay = (self.release_delay.currentIndex() * 5)
            # 统计个数
            self.success_number = 0
            self.fail_number = 0

            # 遍历数据表格的每一行，判断每行的数据是否合理
            rownumber = self.release_table.rowCount()
            for i in range(rownumber):
                fill_color = True
                # 判断表格（账号、密码和内容）是否为空
                username = self.release_table.item(i, 0)
                password = self.release_table.item(i, 1)
                content = self.release_table.item(i, 2)
                # 微博内容的长度不能超过2000
                if username.text() and password.text() and content.text() and len(content.text()) <= 2000:
                    self.row_number_list.append(i)
                    fill_color = False
                # 根据fill_color结果判断是否需要设置颜色
                for k in range(5):
                    if self.release_table.item(i, k):
                        value = self.release_table.item(i, k).text()
                    else:
                        value = ""
                    newItem = QtWidgets.QTableWidgetItem(value)
                    if fill_color:
                        if i in self.row_number_list:
                            self.row_number_list.remove(i)
                        newItem.setBackground(QtGui.QColor(200, 111, 100))
                    self.release_table.setItem(i, k, newItem)
            # 去除重复的内容
            self.row_number_list = sorted(set(self.row_number_list))
            # 获取微博发布的用户数，计算进度条的间距
            pagenumber = len(self.row_number_list) if len(self.row_number_list) else 1
            self.speed = 100 / pagenumber

        # 暂停与开始
        if self.timer.isActive():
            self.timer.stop()
            self.release_bt.setText('继续发布')
        elif self.timer.isActive() == False and self.row_number_list:
            self.timer.start(100, self)
            self.release_bt.setText('暂停发布')

    # 表格填充颜色
    def fill_rpg(self, r, p, g, ):
        for k in range(5):
            if self.release_table.item(self.row_number_list[self.index], k):
                value = self.release_table.item(self.row_number_list[self.index], k).text()
            else:
                value = ""
            newItem = QtWidgets.QTableWidgetItem(value)
            newItem.setBackground(QtGui.QColor(r, p, g))
            self.release_table.setItem(self.row_number_list[self.index], k, newItem)

    # 将CSV文件写入数据表格
    def importcsv_def(self):
        mkdir('temp')
        if os.path.exists('./temp/dispatch.csv'):
            # 清空现有数据
            self.release_table.setRowCount(0)
            # 读取数据
            flie = open('./temp/dispatch.csv', 'r', encoding='gb18030')
            csv_reader = csv.reader(flie)
            for index, row in enumerate(iter(csv_reader)):
                if index != 0:
                    self.release_table.setRowCount(self.release_table.rowCount() + 1)
                    rownumber = self.release_table.rowCount()
                    for i in range(5):
                        newItem = QtWidgets.QTableWidgetItem(row[i])
                        self.release_table.setItem(rownumber - 1, i, newItem)
            self.state_value.setPlainText('导入成功' + '\n' + self.state_value.toPlainText())
            flie.close()
        else:
            self.state_value.setPlainText('找不到文件：dispatch.csv' + '\n' + self.state_value.toPlainText())
        self.release_table.resizeRowsToContents()

    # 将表格的数据导出CSV文件
    def exportcsv_def(self):
        mkdir('temp')
        temp_list = []
        rownumber = self.release_table.rowCount()
        f = open('temp/dispatch.csv', 'w', newline='', encoding='gb18030')
        writer = csv.writer(f)
        writer.writerow(['账号', '密码', '内容', '图片', '定时发布'])
        for i in range(rownumber):
            for k in range(5):
                value = ''
                ojb = self.release_table.item(i, k)
                if ojb:
                    # 先判断ojb是否为None，在判断ojb的值是否为空
                    if ojb.text():
                        value = ojb.text()
                temp_list.append(value)
            writer.writerow(temp_list)
            temp_list = []
        f.close()
        self.state_value.setPlainText('导出成功' + '\n' + self.state_value.toPlainText())

    # 表格自动添加行数
    def tableset(self):
        rownumber = self.release_table.rowCount()
        if rownumber == 0:
            self.release_table.setRowCount(rownumber + 1)
        if self.release_table.item(rownumber - 1, 0):
            if self.release_table.item(rownumber - 1, 0).text():
                self.release_table.setRowCount(rownumber + 1)
        self.release_table.resizeRowsToContents()

    # 设置定时发送
    def set_time(self):
        getrow = self.release_table.currentRow()
        getrow = 0 if getrow < 0 else getrow
        # 提取日期
        get_date = str(self.dateEdit.date()).split('(')[1].split(')')[0].strip()
        # 设置日期格式
        get_time = '-'.join(get_date.split(',')).replace(' ','')
        # 为日期添加小时和分钟
        get_time += ' '+ self.hour.currentText() + ':' + self.minute.currentText()
        # 计算设定的时间与现在的时间差
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        time_difference = datetime.datetime.strptime(get_time, '%Y-%m-%d %H:%M') - datetime.datetime.strptime(now,
                                                                                                              '%Y-%m-%d %H:%M')
        # 判断时间是否符合微博延时发送，若符合则写入对应的表格
        if time_difference.days >= 0:
            time_seconds = time_difference.seconds
            if time_seconds >= 300 or time_difference.days > 0:
                newItem = QtWidgets.QTableWidgetItem(get_time)
                self.release_table.setItem(getrow, 4, newItem)
                self.release_table.resizeRowsToContents()
            else:
                self.state_value.setPlainText('只能发5分钟后的定时微博哦。' + '\n' + self.state_value.toPlainText())
        else:
            self.state_value.setPlainText('只能发5分钟后的定时微博哦。' + '\n' + self.state_value.toPlainText())

    # 验证代理IP
    def check_proxy(self):
        proxy_text = ''
        # 获取代理IP单号
        conf = configparser.ConfigParser()
        if os.path.exists('./temp/conf.ini'):
            conf.read('./temp/conf.ini')
            if 'config' in conf.keys():
                temp = conf['config']
                if 'proxies' in temp.keys():
                    proxy_text = conf['config']['proxies'].strip()
        if proxy_text:
            # 获取代理IP
            url = 'http://api.ip.data5u.com/socks/get.html?order=' + proxy_text + '&json=1&type=1&sep=3'
            r = requests.get(url)
            info = r.json().get('data', '')
            if info:
                ip = info[0].get('ip')
                port = info[0].get('port')
                self.proxies = dict(http='http://' + str(ip) + ':' + str(port))
            # 判断IP代理是否过期
            if not r.json().get('success', ''):
                self.proxies = {}
                self.warm_info = '单号未充值或者单号已经到期' + '\n'
            else:
                self.warm_info = '验证成功' + '\n'
        else:
            self.warm_info = '请设置你的代理IP单号' + '\n'
        self.state_value.setPlainText(self.warm_info + self.state_value.toPlainText())

    # 添加图片
    def showDialog(self):
        # 打开文件对话框
        foldername = QtWidgets.QFileDialog.getExistingDirectory(self, '请选择图片所在文件夹', './')
        result = ''
        if foldername:
            pathDir = os.listdir(foldername)
            for allDir in pathDir:
                if len(self.pic_list) < 9 and ('.jpg' in allDir or '.png' in allDir or '.gif' in allDir):
                    child = os.path.join('%s/%s' % (foldername, allDir))
                    result = result + child + ','
                    get_value = self.state_value.toPlainText()
                    get_value += child + ' 添加成功' + '\n'
                    self.state_value.setPlainText(get_value)
                    self.pic_list.append(child)
        # 在已选的数据行里写入图片路径
        getrow = self.release_table.currentRow()
        getrow = 0 if getrow < 0 else getrow
        newItem = QtWidgets.QTableWidgetItem(result)
        self.release_table.setItem(getrow, 3, newItem)
        self.release_table.resizeRowsToContents()
        self.pic_list = []

    # 返回主界面
    def show_win(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.show()

    def close_win(self):
        self.close()

# 文件运行入口
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = weibo_release_logic()
    ex.show_win()
    sys.exit(app.exec_())
