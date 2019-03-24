# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subjectUI.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1107, 550)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(690, 300, 411, 61))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(200, -10, 211, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Searchbox_text_tagpattern = QtGui.QLineEdit(self.groupBox_3)
        self.Searchbox_text_tagpattern.setGeometry(QtCore.QRect(130, 20, 271, 31))
        self.Searchbox_text_tagpattern.setObjectName(_fromUtf8("Searchbox_text_tagpattern"))
        self.label_3.raise_()
        self.Searchbox_text_tagpattern.raise_()
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 581, 271))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 231, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 171, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Insert_button_subject = QtGui.QPushButton(self.groupBox_4)
        self.Insert_button_subject.setGeometry(QtCore.QRect(480, 230, 93, 28))
        self.Insert_button_subject.setObjectName(_fromUtf8("Insert_button_subject"))
        self.textAdd_subname = QtGui.QTextEdit(self.groupBox_4)
        self.textAdd_subname.setGeometry(QtCore.QRect(220, 40, 351, 31))
        self.textAdd_subname.setObjectName(_fromUtf8("textAdd_subname"))
        self.textAdd_subcode = QtGui.QTextEdit(self.groupBox_4)
        self.textAdd_subcode.setGeometry(QtCore.QRect(340, 0, 231, 31))
        self.textAdd_subcode.setObjectName(_fromUtf8("textAdd_subcode"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 231, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.doubleSpinBox_subcredit = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_subcredit.setGeometry(QtCore.QRect(460, 81, 111, 31))
        self.doubleSpinBox_subcredit.setObjectName(_fromUtf8("doubleSpinBox_subcredit"))
        self.textAdd_subdescription = QtGui.QTextEdit(self.groupBox_4)
        self.textAdd_subdescription.setGeometry(QtCore.QRect(220, 120, 351, 101))
        self.textAdd_subdescription.setObjectName(_fromUtf8("textAdd_subdescription"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 370, 1081, 151))
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(600, 10, 491, 281))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 231, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 541, 41))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textEdit_subname = QtGui.QTextEdit(self.groupBox_5)
        self.textEdit_subname.setGeometry(QtCore.QRect(130, 40, 351, 31))
        self.textEdit_subname.setObjectName(_fromUtf8("textEdit_subname"))
        self.textEdit_subcode = QtGui.QTextEdit(self.groupBox_5)
        self.textEdit_subcode.setGeometry(QtCore.QRect(250, 0, 231, 31))
        self.textEdit_subcode.setObjectName(_fromUtf8("textEdit_subcode"))
        self.label_9 = QtGui.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 231, 41))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.doubleSpinBox_editcredit = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_editcredit.setGeometry(QtCore.QRect(370, 81, 111, 31))
        self.doubleSpinBox_editcredit.setObjectName(_fromUtf8("doubleSpinBox_editcredit"))
        self.textEdit_description = QtGui.QTextEdit(self.groupBox_5)
        self.textEdit_description.setGeometry(QtCore.QRect(130, 120, 351, 101))
        self.textEdit_description.setObjectName(_fromUtf8("textEdit_description"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 230, 341, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cancel_button = QtGui.QPushButton(self.groupBox_2)
        self.cancel_button.setGeometry(QtCore.QRect(240, 0, 93, 28))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.update_button = QtGui.QPushButton(self.groupBox_2)
        self.update_button.setGeometry(QtCore.QRect(130, 0, 93, 28))
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.delete_button = QtGui.QPushButton(self.groupBox_2)
        self.delete_button.setGeometry(QtCore.QRect(20, 0, 93, 28))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Course Subjects", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Enter the search criteria to update</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Subject Name</p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Subject Code</p></body></html>", None))
        self.Insert_button_subject.setText(_translate("Dialog", "Insert", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>No of Credits</p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>Subject Name</p></body></html>", None))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p>Subject Code</p></body></html>", None))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>No of Credits</p></body></html>", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.update_button.setText(_translate("Dialog", "Update", None))
        self.delete_button.setText(_translate("Dialog", "Delete", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

