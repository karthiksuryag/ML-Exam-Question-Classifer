# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubjectEvalUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from GUI.canvasCreator import MplWidget
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(892, 784)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 871, 251))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(390, 0, 61, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 171, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox_subject = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_subject.setGeometry(QtCore.QRect(160, 10, 191, 22))
        self.comboBox_subject.setObjectName(_fromUtf8("comboBox_subject"))
        self.comboBox_Year = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_Year.setGeometry(QtCore.QRect(470, 10, 121, 22))
        self.comboBox_Year.setObjectName(_fromUtf8("comboBox_Year"))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.comboBox_Year.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(640, 0, 61, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_Semester = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_Semester.setGeometry(QtCore.QRect(730, 10, 121, 22))
        self.comboBox_Semester.setObjectName(_fromUtf8("comboBox_Semester"))
        self.comboBox_Semester.addItem(_fromUtf8(""))
        self.comboBox_Semester.addItem(_fromUtf8(""))
        self.comboBox_Semester.addItem(_fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(110, 60, 741, 121))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.dial_Appl = QtGui.QDial(self.groupBox)
        self.dial_Appl.setGeometry(QtCore.QRect(300, 10, 50, 64))
        self.dial_Appl.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.dial_Appl.setObjectName(_fromUtf8("dial_Appl"))
        self.dial_Comp = QtGui.QDial(self.groupBox)
        self.dial_Comp.setGeometry(QtCore.QRect(180, 10, 50, 64))
        self.dial_Comp.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 127);"))
        self.dial_Comp.setObjectName(_fromUtf8("dial_Comp"))
        self.dial_Know = QtGui.QDial(self.groupBox)
        self.dial_Know.setGeometry(QtCore.QRect(60, 10, 50, 64))
        self.dial_Know.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 255);"))
        self.dial_Know.setObjectName(_fromUtf8("dial_Know"))
        self.dial_Anal = QtGui.QDial(self.groupBox)
        self.dial_Anal.setGeometry(QtCore.QRect(420, 10, 50, 64))
        self.dial_Anal.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 255);"))
        self.dial_Anal.setObjectName(_fromUtf8("dial_Anal"))
        self.dial_Synt = QtGui.QDial(self.groupBox)
        self.dial_Synt.setGeometry(QtCore.QRect(540, 10, 50, 64))
        self.dial_Synt.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.dial_Synt.setObjectName(_fromUtf8("dial_Synt"))
        self.dial_Eval = QtGui.QDial(self.groupBox)
        self.dial_Eval.setGeometry(QtCore.QRect(670, 10, 50, 64))
        self.dial_Eval.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(85, 170, 0);"))
        self.dial_Eval.setObjectName(_fromUtf8("dial_Eval"))
        self.spinBox_Eval = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Eval.setGeometry(QtCore.QRect(660, 90, 61, 22))
        self.spinBox_Eval.setObjectName(_fromUtf8("spinBox_Eval"))
        self.spinBox_Synt = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Synt.setGeometry(QtCore.QRect(530, 90, 61, 22))
        self.spinBox_Synt.setObjectName(_fromUtf8("spinBox_Synt"))
        self.spinBox_Anal = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Anal.setGeometry(QtCore.QRect(410, 90, 61, 22))
        self.spinBox_Anal.setObjectName(_fromUtf8("spinBox_Anal"))
        self.spinBox_Appl = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Appl.setGeometry(QtCore.QRect(290, 90, 61, 22))
        self.spinBox_Appl.setObjectName(_fromUtf8("spinBox_Appl"))
        self.spinBox_Comp = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Comp.setGeometry(QtCore.QRect(180, 90, 61, 22))
        self.spinBox_Comp.setObjectName(_fromUtf8("spinBox_Comp"))
        self.spinBox_Know = QtGui.QSpinBox(self.groupBox)
        self.spinBox_Know.setGeometry(QtCore.QRect(60, 90, 61, 22))
        self.spinBox_Know.setObjectName(_fromUtf8("spinBox_Know"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(50, -10, 81, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(170, -10, 81, 41))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(410, -10, 81, 41))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(530, -10, 81, 41))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(660, -10, 81, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(400, 50, 81, 41))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_Add = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Add.setGeometry(QtCore.QRect(750, 210, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}"))
        self.pushButton_Add.setObjectName(_fromUtf8("pushButton_Add"))
        self.pushButton_Insert = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Insert.setGeometry(QtCore.QRect(630, 210, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Insert.setFont(font)
        self.pushButton_Insert.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}"))
        self.pushButton_Insert.setObjectName(_fromUtf8("pushButton_Insert"))
        self.pushButton_Cancel = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(520, 210, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cancel.setFont(font)
        self.pushButton_Cancel.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}"))
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.pushButton_Update = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Update.setGeometry(QtCore.QRect(400, 210, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Update.setFont(font)
        self.pushButton_Update.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}"))
        self.pushButton_Update.setObjectName(_fromUtf8("pushButton_Update"))
        self.pushButton_Delete = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_Delete.setGeometry(QtCore.QRect(280, 210, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Delete.setFont(font)
        self.pushButton_Delete.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}"))
        self.pushButton_Delete.setObjectName(_fromUtf8("pushButton_Delete"))
        self.lineEdit_Search = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_Search.setGeometry(QtCore.QRect(112, 211, 141, 31))
        self.lineEdit_Search.setInputMask(_fromUtf8(""))
        self.lineEdit_Search.setObjectName(_fromUtf8("lineEdit_Search"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 210, 171, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(0, 70, 121, 101))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 270, 871, 151))
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 430, 471, 301))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit_SubjectDescription = QtGui.QTextEdit(Dialog)
        self.textEdit_SubjectDescription.setGeometry(QtCore.QRect(490, 430, 391, 301))
        self.textEdit_SubjectDescription.setObjectName(_fromUtf8("textEdit_SubjectDescription"))
        self.mpl = MplWidget()
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 720, 469, 61))
        self.label_15.setObjectName(_fromUtf8("label_15"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.dial_Know, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Know.setValue)
        QtCore.QObject.connect(self.spinBox_Know, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Know.setValue)
        QtCore.QObject.connect(self.dial_Comp, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Comp.setValue)
        QtCore.QObject.connect(self.spinBox_Comp, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Comp.setValue)
        QtCore.QObject.connect(self.dial_Appl, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Appl.setValue)
        QtCore.QObject.connect(self.spinBox_Appl, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Appl.setValue)
        QtCore.QObject.connect(self.dial_Anal, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Anal.setValue)
        QtCore.QObject.connect(self.spinBox_Anal, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Anal.setValue)
        QtCore.QObject.connect(self.dial_Synt, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Synt.setValue)
        QtCore.QObject.connect(self.spinBox_Synt, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Synt.setValue)
        QtCore.QObject.connect(self.dial_Eval, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBox_Eval.setValue)
        QtCore.QObject.connect(self.spinBox_Eval, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial_Eval.setValue)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Course Subjects", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Year</p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Subject Code</p></body></html>", None))
        self.comboBox_Year.setItemText(0, _translate("Dialog", "2015", None))
        self.comboBox_Year.setItemText(1, _translate("Dialog", "2016", None))
        self.comboBox_Year.setItemText(2, _translate("Dialog", "2017", None))
        self.comboBox_Year.setItemText(3, _translate("Dialog", "2018", None))
        self.comboBox_Year.setItemText(4, _translate("Dialog", "2019", None))
        self.comboBox_Year.setItemText(5, _translate("Dialog", "2020", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Semester</p></body></html>", None))
        self.comboBox_Semester.setItemText(0, _translate("Dialog", "1", None))
        self.comboBox_Semester.setItemText(1, _translate("Dialog", "2", None))
        self.comboBox_Semester.setItemText(2, _translate("Dialog", "3", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#6913ff;\">Knowledge</span></p></body></html>", None))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#6913ff;\">Comprehension</span></p></body></html>", None))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#5555ff;\">Analysis</span></p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#5555ff;\">Synthesis</span></p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#5555ff;\">Evaluation</span></p></body></html>", None))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#5555ff;\">Application</span></p></body></html>", None))
        self.pushButton_Add.setText(_translate("Dialog", "Add", None))
        self.pushButton_Insert.setText(_translate("Dialog", "Insert", None))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_Update.setText(_translate("Dialog", "Update", None))
        self.pushButton_Delete.setText(_translate("Dialog", "Delete", None))
        self.lineEdit_Search.setPlaceholderText(_translate("Dialog", "Enter Subject", None))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p>Search</p></body></html>", None))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p>Blooms Taxonomy</p><p>Subject Evaluation</p><p>Measurements</p></body></html>", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Subject", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Year", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Semest", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Know", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Compre", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Appli", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Analy", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Synthe", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Evalua", None))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>Blooms taxonomy category subject evaluation percentage </p></body></html>", None))
        self.horizontalLayout.addWidget(self.mpl)
