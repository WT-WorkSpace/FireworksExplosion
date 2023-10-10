import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import  QEvent, QRect, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QIcon, QMovie
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
import random


class LogoningWidget(QtWidgets.QDialog):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("../ui/logoning.ui", self)
        self.LikepushButton.clicked.connect(self.like)

        self.setWindowTitle("人生苦短,还好有你！")
        self.setWindowIcon(QIcon('../img/icon.png'))

        self.giflabel = self.GifLabel
        movie = QMovie("../img/logoning.gif")
        movie.setScaledSize(self.giflabel.size())
        self.giflabel.setMovie(movie)
        movie.start()

        self.NolikepushButton.clicked.connect(self.nolike)
        self.NolikepushButton.setMouseTracking(True)
        self.NolikepushButton.installEventFilter(self)

    def closeEvent(self, event):
        # 弹出对话框
        reply = QMessageBox.question(self, '往哪跑？', "你跑的了么？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 对返回的选项进行操作
        if reply == QMessageBox.Yes:
            QMessageBox.warning(self, "别跑了", "你注定是我的 (≖ ‿ ≖)✧")
        else:
            QMessageBox.warning(self, "明智", "不跑就对了嘛 (≖ ‿ ≖)✧")
        event.ignore()

    def like(self):
        QMessageBox.warning(self, "哈哈", "哥哥很开心！ (≖ ‿ ≖)✧")
        self.switch_window.emit()
        # sys.exit()

    def nolike(self):
        QMessageBox.information(self, '可以嘛', "手速不错，我喜欢！不过你还是跑不的，你注定是我的 (≖ ‿ ≖)✧")

    def eventFilter(self, object, event):
        if object == self.NolikepushButton:
            if event.type() == QEvent.Enter:
                self.doMove()
        return QWidget.eventFilter(self, object, event)

    def doMove(self):
        print("move")
        global x, y
        if self.NolikepushButton.pos() == QPoint(410, 140):
            self.anim = QPropertyAnimation(self.NolikepushButton, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QRect(410, 140, 91, 31))
            x = random.randint(40, 630)
            y = random.randint(30, 220)
            self.anim.setEndValue(QRect(x, y, 91, 31))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()
        elif self.NolikepushButton.pos() == QPoint(x, y):
            self.anim = QPropertyAnimation(self.NolikepushButton, b"geometry")
            self.anim.setDuration(200)
            self.anim.setStartValue(QRect(x, y, 91, 31))
            x = random.randint(40, 630)
            y = random.randint(30, 220)
            self.anim.setEndValue(QRect(x, y, 91, 31))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LogoningWidget()
    # 展示窗口
    w.show()
    app.exec()
