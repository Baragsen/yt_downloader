
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdvancedPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget {background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 72, 37))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #1B0C66;\n"
"    border-radius: 15px;\n"
"    font-size: 14px;\n"
"    color : #FFFFFF;\n"
"    padding: 10px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1B0C66;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C5A4EE;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 80, 401, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_9.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<- BACK"))
        self.checkBox.setText(_translate("MainWindow", "Channel name"))
        self.checkBox_6.setText(_translate("MainWindow", "Length"))
        self.checkBox_4.setText(_translate("MainWindow", "Metadata"))
        self.checkBox_5.setText(_translate("MainWindow", "Video description"))
        self.checkBox_3.setText(_translate("MainWindow", "Views"))
        self.checkBox_2.setText(_translate("MainWindow", "Channel Url"))
        self.checkBox_8.setText(_translate("MainWindow", "Thumbnail url"))
        self.checkBox_7.setText(_translate("MainWindow", "Captions"))
        self.checkBox_9.setText(_translate("MainWindow", "Videos Urls"))
