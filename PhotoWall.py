import os
import sys
import cv2
import numpy as np

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

import hexagon
import ui_PhotoWall


class PhotoWall(QMainWindow, ui_PhotoWall.Ui_mainWindow):
    def __init__(self, parent=None):
        super(PhotoWall, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 初始化
        QApplication.setStyle('Fusion')
        self.buttonRead.clicked.connect(self.buttonRead_clicked)
        self.buttonWrite.clicked.connect(self.buttonWrite_clicked)
        self.buttonStart.clicked.connect(self.buttonStart_clicked)
        self.setWindowIcon(QIcon('image/photowall.ico'))
        self.labelImg.setPixmap(QPixmap("image/h_lena.jpg"))
        self.statusbar.showMessage("初始化完成", 3000)

    def buttonStart_clicked(self):
        for name in self.namelist:
            oriImgPath = self.readPath + '/' + name
            proImgPath = self.writePath + '/h_' + name
            # self.labelImg.setPixmap(QPixmap(oriImgPath))
            #oriImg = cv2.imread(oriImgPath)
            oriImg = cv2.imdecode(np.fromfile(
                oriImgPath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            proImg = hexagon.hexagonImg(oriImg)
            cv2.imencode('.jpg', proImg)[1].tofile(proImgPath)  # 保存图片
            self.labelImg.setPixmap(QPixmap(proImgPath))
            #cv2.imshow("HEXAGON", proImg)
            cv2.waitKey(5)
        self.statusbar.showMessage("Finashed!!", 5000)
        QMessageBox.information(self, "成功", "图像转换完成！",
                                QMessageBox.Ok, QMessageBox.Ok)

    def buttonRead_clicked(self):
        self.readPath = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        if self.readPath:
            # 得到该目录下所有图片文件列表
            self.namelist = []
            for file in os.listdir(self.readPath):
                if os.path.splitext(file)[1] in ('.jpg', 'jpeg', 'JPEG', '.JPG', '.png', '.tif'):
                    self.namelist.append(file)
            self.lineEditReadPath.setText(self.readPath)
            if(not (self.lineEditWritePath.text())):
                self.lineEditWritePath.setText(self.readPath)
                self.writePath = self.readPath
            self.buttonStart.setEnabled(True)
            self.statusbar.showMessage("路径设置为："+self.readPath, 2000)
        else:
            self.statusbar.showMessage("打开路径失败", 3000)

    def buttonWrite_clicked(self):
        self.writePath = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        if self.writePath:
            self.lineEditWritePath.setText(self.writePath)
            if(not self.lineEditReadPath.text()):
                self.lineEditReadPath.setText(self.writePath)
                self.readPath = self.writePath
            self.buttonStart.setEnabled(True)
            self.statusbar.showMessage("路径设置为："+self.writePath, 2000)
        else:
            self.statusbar.showMessage("打开路径失败", 3000)


if __name__ == "__main__":
    app = QApplication(sys.argv)        # QApplication对象
    mainUI = PhotoWall()                      # 主窗口
    mainUI.show()
    sys.exit(app.exec_())               # 进入该程序的主循环
