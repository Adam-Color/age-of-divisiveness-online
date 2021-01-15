import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class BuildBuildingWindow(QMainWindow):
    """ For now just a dummy window, work in progress."""

    def __init__(self, parent, grandparent):
        super(BuildBuildingWindow, self).__init__()
        self.setWindowTitle("Build Building")
        self.resize(450, 660)
        self.parent = parent  # for calling method inside parent object (BuildUnitFlatButton)
        self.grandparent = grandparent  # for calling method inside parent's parent object (CityView)

        self.centralwidget = QtWidgets.QWidget()

        """ BUILDINGS PART """

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 211, 16))
        self.label.setText("Astronomic Tower")

        self.label_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_desc.setGeometry(QtCore.QRect(120, 50, 211, 40))
        self.label_desc.setWordWrap(True)
        self.label_desc.setStyleSheet("color: rgb(150, 150, 81)")
        self.label_desc.setText("Increases radius of city are by 1.")

        self.image_1 = QtWidgets.QLabel(self.centralwidget)
        self.image_1.setGeometry(QtCore.QRect(20, 20, 81, 71))
        pixmap = QPixmap(os.getcwd() + '/resources/images/buildings/astronomic_tower.png')
        self.image_1.setPixmap(pixmap)
        self.image_1.setScaledContents(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 211, 16))
        self.label_2.setText("Mines")

        self.label_2_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_2_desc.setGeometry(QtCore.QRect(120, 140, 211, 40))
        self.label_2_desc.setWordWrap(True)
        self.label_2_desc.setStyleSheet("color: rgb(150, 150, 81)")
        self.label_2_desc.setText("Produces extra 20 stone per turn.")

        self.image_2 = QtWidgets.QLabel(self.centralwidget)
        self.image_2.setGeometry(QtCore.QRect(20, 110, 81, 71))
        pixmap = QPixmap(os.getcwd() + '/resources/images/buildings/mines.png')
        self.image_2.setPixmap(pixmap)
        self.image_2.setScaledContents(True)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 210, 211, 16))
        self.label_9.setText("Free Market")

        self.label_9_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_9_desc.setGeometry(QtCore.QRect(120, 230, 211, 40))
        self.label_9_desc.setWordWrap(True)
        self.label_9_desc.setStyleSheet("color: rgb(150, 150, 81)")
        self.label_9_desc.setText("Every city area square brings extra 5 gold.")

        self.image_3 = QtWidgets.QLabel(self.centralwidget)
        self.image_3.setGeometry(QtCore.QRect(20, 200, 81, 71))
        pixmap = QPixmap(os.getcwd() + '/resources/images/buildings/free_market.png')
        self.image_3.setPixmap(pixmap)
        self.image_3.setScaledContents(True)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(120, 300, 211, 16))
        self.label_10.setText("Armory")

        self.label_10_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_10_desc.setGeometry(QtCore.QRect(120, 320, 211, 40))
        self.label_10_desc.setWordWrap(True)
        self.label_10_desc.setStyleSheet("color: rgb(150, 150, 81)")
        self.label_10_desc.setText("All unites cost 15% less wood and stone.")

        self.image_4 = QtWidgets.QLabel(self.centralwidget)
        self.image_4.setGeometry(QtCore.QRect(20, 290, 81, 71))
        pixmap = QPixmap(os.getcwd() + '/resources/images/buildings/armory.png')
        self.image_4.setPixmap(pixmap)
        self.image_4.setScaledContents(True)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 390, 211, 16))
        self.label_11.setText("Passiflora")

        self.label_11_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_11_desc.setGeometry(QtCore.QRect(120, 410, 211, 40))
        self.label_11_desc.setWordWrap(True)
        self.label_11_desc.setStyleSheet("color: rgb(150, 150, 81)")
        self.label_11_desc.setText("All unites cost 20% less food and gold.")

        self.image_5 = QtWidgets.QLabel(self)
        self.image_5.setGeometry(QtCore.QRect(20, 380, 81, 71))
        pixmap = QPixmap(os.getcwd() + '/resources/images/buildings/passiflora.png')
        self.image_5.setPixmap(pixmap)
        self.image_5.setScaledContents(True)

        """ COSTS PART """

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(322, 506, 41, 21))
        self.label_6.setText("food")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(122, 506, 41, 21))
        self.label_4.setText("wood")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(22, 506, 41, 21))
        self.label_3.setText("gold")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(172, 536, 41, 21))
        self.label_7.setText("time")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(202, 476, 41, 21))
        self.label_5.setText("Cost:")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(222, 506, 41, 21))
        self.label_8.setText("stone")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 570, 141, 61))
        self.pushButton.setText("Build")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(172, 506, 41, 21))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(62, 506, 41, 21))

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(362, 506, 41, 21))

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(212, 536, 41, 21))

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(272, 506, 41, 21))

        """ RADIO BUTTONS PART"""

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(350, 50, 21, 21))
        self.radioButton.setText("")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 140, 21, 21))
        self.radioButton_2.setText("")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 230, 21, 21))
        self.radioButton_3.setText("")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(350, 320, 21, 21))
        self.radioButton_4.setText("")

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(350, 410, 21, 21))
        self.radioButton_5.setText("")

        self.setCentralWidget(self.centralwidget)

    def closeEvent(self, event) -> None:
        self.parent.kill_app()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = BuildBuildingWindow(None, None)
    win.show()
    sys.exit(app.exec_())
