import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
import json


class LoginWidget(QtWidgets.QDialog):
    switch_logoning = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("../ui/logon.ui", self)
        self.Logon_Button.clicked.connect(self.logon)
        self.Login_Button.clicked.connect(self.login)

        '''登陆界面中的图像显示'''
        self.image_path = "../img/name.png"
        self.img_label.setAlignment(Qt.AlignCenter)
        # self.img_label.setStyleSheet("background-color: yellow; color: black;")
        pixmap = QPixmap(self.image_path).scaled(self.img_label.width(), self.img_label.height(),
                                                 Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)

        self.setWindowTitle("人生苦短,还好有你！")
        self.setWindowIcon(QIcon('../img/icon.png'))

    def closeEvent(self, event):
        # 弹出对话框
        reply = QMessageBox.question(self, '往哪跑？', "你跑的了么？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 对返回的选项进行操作
        if reply == QMessageBox.Yes:
            QMessageBox.warning(self, "别跑了", "你注定是我的 (≖ ‿ ≖)✧")
        else:
            QMessageBox.warning(self, "明智", "不跑就对了嘛 (≖ ‿ ≖)✧")
        event.ignore()

    def logon(self):
        user_name = self.Username_LineEdit.text()
        password = self.Password_LineEdit.text()
        def json2dict(json_path):
            with open(json_path, 'r', encoding='UTF-8') as f:
                json_dict = json.loads(f.read())
            return json_dict
        data = json2dict("../data/data.json")
        if user_name in data and password == data[user_name]:
            self.TextBrowser.setText("欢迎%s" % user_name)
            self.TextBrowser.repaint()
            self.switch_logoning.emit()
        else:
            self.TextBrowser.setText("用户名或密码错误....请重试")
            self.TextBrowser.repaint()
            QMessageBox.warning(self, "登录失败", "用户名或密码错误")
    def login(self):
        QMessageBox.warning(self, "注册失败", "暂时未开放其他人注册")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginWidget()
    # 展示窗口
    w.show()
    app.exec()
