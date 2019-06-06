# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadSingleButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadSingleButton.setGeometry(QtCore.QRect(370, 271, 99, 27))
        self.loadSingleButton.setObjectName("loadSingleButton")
        self.n_split = QtWidgets.QSpinBox(self.centralwidget)
        self.n_split.setGeometry(QtCore.QRect(130, 271, 171, 27))
        self.n_split.setMaximum(65535)
        self.n_split.setSingleStep(10000)
        self.n_split.setObjectName("n_split")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(14, 276, 121, 17))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 24, 471, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.errorDisplay = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.errorDisplay.setGeometry(QtCore.QRect(0, 0, 471, 211))
        self.errorDisplay.setObjectName("errorDisplay")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 244, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 111, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadSingleButton.setText(_translate("MainWindow", "文件导入"))
        self.label.setText(_translate("MainWindow", "单文件电话条数："))
        self.label_2.setText(_translate("MainWindow", "非法号码列表："))


