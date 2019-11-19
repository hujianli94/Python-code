from PyQt5 import QtCore, QtGui, QtWidgets
from weibo_collect import Ui_Dialog
from weibo import *
from PyQt5.QtCore import QBasicTimer
import csv, time, os, configparser, sys

# 热门微博采集
class weibo_collect_logic(QtWidgets.QWidget, Ui_Dialog):

    def __init__(self, parent=None):
        super(weibo_collect_logic, self).__init__(parent)
        self.setupUi(self)
        # 设置左上方的logo
        self.setWindowIcon(QtGui.QIcon('ico/logo.png'))
        # 设置表格的表头格式
        self.collect_data.setHorizontalHeaderLabels(['用户', '文本内容', '图片', '视频', '采集日期'])
        self.collect_data.verticalHeader().setStyleSheet("QHeaderView::section {background:rgb(230, 230, 230)}")
        self.collect_data.horizontalHeader().setStyleSheet("QHeaderView::section {background:rgb(230, 230, 230)}")
        # 设置按钮'采集'的功能
        self.collect_start.clicked.connect(self.collect_weibo_data)
        # 定义进度条对象
        self.timer = QBasicTimer()
        self.step = 0
        # 设置属性，在函数之间调用
        self.session = ''
        self.keyword = ''
        self.pagenumber = 1
        # 读取配置文件
        conf = configparser.ConfigParser()
        if os.path.exists('./temp/conf.ini'):
            conf.read('./temp/conf.ini')
            if 'config' in conf.keys():
                temp = conf['config']
                if 'collect_username' in temp.keys():
                    self.collect_user.setText(conf['config']['collect_username'])
                if 'collect_password' in temp.keys():
                    self.collect_password.setText(conf['config']['collect_password'])

    # 进度条
    def timerEvent(self, event):
        # 进度条已满，即完成采集，执行初始化，为下次采集准备
        if self.step >= 100:
            self.timer.stop()
            self.collect_state.setPlainText('采集完成' + '\n' + self.collect_state.toPlainText())
            self.collect_start.setText('开始采集')
            self.step = 0
            self.session = ''
            self.pagenumber = 1
            self.write_table()
            return
        # 调用函数collect_weibo，采集微博
        collect_weibo(keyword=self.keyword, session=self.session, pagenumber=self.pagenumber, proxies={},
                      get_img=self.get_img, get_video=self.get_video)
        # 爬取完成后，设置进度条
        self.pagenumber += 1
        self.step = self.step + self.speed
        self.progressBar.setValue(self.step)
        time.sleep(2)

    # 绑定'开始采集'按钮的功能函数
    def collect_weibo_data(self):
        if self.step == 0:
            # 获取采集选项
            self.get_img = self.select_pic.isChecked()
            self.get_video = self.select_video.isChecked()
            self.keyword = self.collect_keyword.text().strip()

            # 清空datatable数据
            self.collect_data.setRowCount(0)
            # 获取登录账号密码
            username = self.collect_user.text().strip()
            password = self.collect_password.text().strip()
            # 登录
            if username and password and self.keyword:
                # 登录验证
                login_info = login(username, password)
                # 判断验证结果
                if 'session' in login_info.keys():
                    self.session = login_info['session']
                    # 写入配置文件
                    conf = configparser.ConfigParser()
                    if os.path.exists('./temp/conf.ini'):
                        conf.read('./temp/conf.ini')
                    else:
                        conf.add_section('config')
                    conf.set('config', 'collect_username', username)
                    conf.set('config', 'collect_password', password)
                    conf.write(open('./temp/conf.ini', 'w'))

            # 根据爬取页数进行分段处理
            if self.collect_page.currentIndex() == 0:
                pagenumber = 10
            elif self.collect_page.currentIndex() == 1:
                pagenumber = 20
            else:
                pagenumber = 50
            self.speed = 100 / pagenumber

        # 暂停或开始微博采集
        if self.timer.isActive():
            self.timer.stop()
            self.collect_start.setText('继续采集')
        elif self.timer.isActive() == False and self.session and self.keyword:
            self.timer.start(100, self)
            self.collect_start.setText('暂停采集')
        # 判断关键词是否为空
        elif self.keyword == '':
            self.collect_state.setPlainText('请输入关键词' + '\n' + self.collect_state.toPlainText())
        # 判断当前微博是否已登录
        elif self.session == '':
            self.collect_state.setPlainText('微博账号或密码错误' + '\n' + self.collect_state.toPlainText())
    # 读取CSV文件，将文件内容写入Table
    def write_table(self):
        if os.path.exists('./temp/data.csv'):
            csv_reader = csv.reader(open('./temp/data.csv', 'r', encoding='gb18030'))
            for index, row in enumerate(iter(csv_reader)):
                if index != 0:
                    self.collect_data.setRowCount(self.collect_data.rowCount() + 1)
                    rownumber = self.collect_data.rowCount()
                    for i in range(5):
                        newItem = QtWidgets.QTableWidgetItem(row[i])
                        self.collect_data.setItem(rownumber - 1, i, newItem)
            self.collect_data.sortByColumn(6, QtCore.Qt.DescendingOrder)

    # 定义界面运行函数
    def show_win(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.show()
    # 定义界面的关闭函数
    def close_win(self):
        self.close()

# 软件的运行入口
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = weibo_collect_logic()
    ex.show_win()
    sys.exit(app.exec_())
