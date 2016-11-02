# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(652, 327)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 211, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.LAB = QtGui.QLabel(self.centralWidget)
        self.LAB.setGeometry(QtCore.QRect(60, 70, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Reference Sans Serif"))
        font.setPointSize(16)
        self.LAB.setFont(font)
        self.LAB.setObjectName(_fromUtf8("LAB"))
        self.label1 = QtGui.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(260, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Sans Serif"))
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.pitch = QtGui.QLabel(self.centralWidget)
        self.pitch.setGeometry(QtCore.QRect(240, 110, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pitch.setFont(font)
        self.pitch.setTextFormat(QtCore.Qt.RichText)
        self.pitch.setIndent(16)
        self.pitch.setObjectName(_fromUtf8("pitch"))
        self.roll = QtGui.QLabel(self.centralWidget)
        self.roll.setGeometry(QtCore.QRect(50, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.roll.setFont(font)
        self.roll.setIndent(14)
        self.roll.setObjectName(_fromUtf8("roll"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(446, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.light = QtGui.QLabel(self.centralWidget)
        self.light.setGeometry(QtCore.QRect(450, 110, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.light.setFont(font)
        self.light.setObjectName(_fromUtf8("light"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#aa0000; vertical-align:super;\">IOT SENSOR NODE 1</span></p></body></html>", None))
        self.LAB.setText(_translate("MainWindow", "ROLL", None))
        self.label1.setText(_translate("MainWindow", "PITCH", None))
        self.pitch.setText(_translate("MainWindow", "0", None))
        self.roll.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "LIGHT %", None))
        self.light.setText(_translate("MainWindow", "0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

