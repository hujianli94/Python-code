from PyQt5 import QtCore, QtGui, QtWidgets
from weibo_main import Ui_Form
from service import weibo_service_logic
from collect import weibo_collect_logic
from release import weibo_release_logic
import sys

# 软件主界面
class main_windows(QtWidgets.QWidget, Ui_Form):
    # 自定义初始化函数
    def __init__(self, parent=None):
        super(main_windows, self).__init__(parent)
        self.setupUi(self)
        # 设置logo和图片
        self.setWindowIcon(QtGui.QIcon('ico/logo.png'))
    # 定义界面运行函数
    def show_win(self):
        # setFixedSize固定界面大小
        self.setFixedSize(self.width(), self.height())
        # 将最大化按钮设为不可用
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.show()
    # 定义界面关闭函数
    def close_win(self):
        self.close()

if __name__ == '__main__':
    # 实例化PyQt5对象
    app = QtWidgets.QApplication(sys.argv)
    # 实例化软件主界面
    mw = main_windows()
    # 其他功能界面的实例化对象
    service = weibo_service_logic()
    collect = weibo_collect_logic()
    release = weibo_release_logic()
	
    # 显示软件主界面
    mw.show_win()
    # 软件主界面的按钮绑定功能函数
    mw.main_service.clicked.connect(mw.close_win)
    mw.main_service.clicked.connect(service.show_win)
    mw.main_collect.clicked.connect(mw.close_win)
    mw.main_collect.clicked.connect(collect.show_win)
    mw.main_release.clicked.connect(mw.close_win)
    mw.main_release.clicked.connect(release.show_win)

    # 其他功能界面的"主菜单"按钮绑定功能函数
    collect.main_win.clicked.connect(collect.close_win)
    collect.main_win.clicked.connect(mw.show_win)
    release.main_win.clicked.connect(release.close_win)
    release.main_win.clicked.connect(mw.show_win)
    service.main_win.clicked.connect(service.close_win)
    service.main_win.clicked.connect(mw.show_win)
    # 软件结束运行
    sys.exit(app.exec_())
