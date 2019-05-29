# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PhotoWall.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(450, 578)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelImg = QtWidgets.QLabel(self.centralwidget)
        self.labelImg.setMinimumSize(QtCore.QSize(432, 432))
        self.labelImg.setMaximumSize(QtCore.QSize(432, 432))
        self.labelImg.setText("")
        self.labelImg.setPixmap(QtGui.QPixmap("image/h_lena.jpg"))
        self.labelImg.setScaledContents(True)
        self.labelImg.setObjectName("labelImg")
        self.gridLayout.addWidget(self.labelImg, 0, 0, 1, 3)
        self.labelReadPath = QtWidgets.QLabel(self.centralwidget)
        self.labelReadPath.setObjectName("labelReadPath")
        self.gridLayout.addWidget(self.labelReadPath, 1, 0, 1, 1)
        self.lineEditReadPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditReadPath.setObjectName("lineEditReadPath")
        self.gridLayout.addWidget(self.lineEditReadPath, 1, 1, 1, 1)
        self.buttonRead = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRead.setObjectName("buttonRead")
        self.gridLayout.addWidget(self.buttonRead, 1, 2, 1, 1)
        self.labelWritePath = QtWidgets.QLabel(self.centralwidget)
        self.labelWritePath.setObjectName("labelWritePath")
        self.gridLayout.addWidget(self.labelWritePath, 2, 0, 1, 1)
        self.lineEditWritePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWritePath.setObjectName("lineEditWritePath")
        self.gridLayout.addWidget(self.lineEditWritePath, 2, 1, 1, 1)
        self.buttonWrite = QtWidgets.QPushButton(self.centralwidget)
        self.buttonWrite.setObjectName("buttonWrite")
        self.gridLayout.addWidget(self.buttonWrite, 2, 2, 1, 1)
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStart.sizePolicy().hasHeightForWidth())
        self.buttonStart.setSizePolicy(sizePolicy)
        self.buttonStart.setObjectName("buttonStart")
        self.gridLayout.addWidget(self.buttonStart, 3, 0, 1, 3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "HEXAGON"))
        self.labelReadPath.setText(_translate("mainWindow", "读入路径"))
        self.buttonRead.setText(_translate("mainWindow", "浏览"))
        self.labelWritePath.setText(_translate("mainWindow", "输出路径"))
        self.buttonWrite.setText(_translate("mainWindow", "浏览"))
        self.buttonStart.setText(_translate("mainWindow", "开始"))


