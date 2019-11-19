# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weibo_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("border-image:url(ico/bg.jpg)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.main_release = QtWidgets.QPushButton(Form)
        self.main_release.setGeometry(QtCore.QRect(310, 60, 181, 41))
        self.main_release.setStyleSheet("border-image:url(ico/release.png)")
        self.main_release.setText("")
        self.main_release.setObjectName("main_release")
        self.main_collect = QtWidgets.QPushButton(Form)
        self.main_collect.setGeometry(QtCore.QRect(310, 130, 181, 41))
        self.main_collect.setStyleSheet("border-image:url(ico/collect.png)")
        self.main_collect.setText("")
        self.main_collect.setObjectName("main_collect")
        self.main_service = QtWidgets.QPushButton(Form)
        self.main_service.setGeometry(QtCore.QRect(310, 200, 181, 41))
        self.main_service.setStyleSheet("border-image:url(ico/server.png)")
        self.main_service.setText("")
        self.main_service.setObjectName("main_service")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "微博爬虫软件"))

