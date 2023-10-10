import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from logon import LoginWidget
from logoning import LogoningWidget
from mainwindow import MainWindow


class Controller:
    def __init__(self):
        self.login = LoginWidget()
        self.window = MainWindow()
        self.logoning = LogoningWidget()

    def show_login(self):
        self.login.switch_logoning.connect(self.show_logoning)
        self.login.show()
    def show_logoning(self):
        self.logoning.switch_window.connect(self.show_main)
        self.login.hide()
        self.logoning.show()
    def show_main(self):
        self.window.exit_window.connect(self.close)
        self.logoning.hide()
        self.window.show()

    def close(self):
        QApplication.quit()
        print("退出")


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
