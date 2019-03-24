# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blooms_categoryUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from CONNECTION.DB_Handling import DBHandler
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
        Dialog.resize(756, 337)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 741, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Subject_No_label = QtGui.QLabel(self.groupBox)
        self.Subject_No_label.setGeometry(QtCore.QRect(10, 30, 53, 16))
        self.Subject_No_label.setObjectName(_fromUtf8("Subject_No_label"))
        self.Subject_no_text = QtGui.QLineEdit(self.groupBox)
        self.Subject_no_text.setGeometry(QtCore.QRect(110, 30, 113, 22))
        self.Subject_no_text.setObjectName(_fromUtf8("Subject_no_text"))
        self.Subject_description_text = QtGui.QLineEdit(self.groupBox)
        self.Subject_description_text.setGeometry(QtCore.QRect(430, 30, 301, 22))
        self.Subject_description_text.setObjectName(_fromUtf8("Subject_description_text"))
        self.subject_desc_label = QtGui.QLabel(self.groupBox)
        self.subject_desc_label.setGeometry(QtCore.QRect(280, 30, 81, 16))
        self.subject_desc_label.setObjectName(_fromUtf8("subject_desc_label"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 721, 61))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cancel_button = QtGui.QPushButton(self.groupBox_2)
        self.cancel_button.setGeometry(QtCore.QRect(620, 10, 93, 28))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.update_button = QtGui.QPushButton(self.groupBox_2)
        self.update_button.setGeometry(QtCore.QRect(510, 10, 93, 28))
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 281, 151))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 231, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Searchbox_text = QtGui.QLineEdit(self.groupBox_3)
        self.Searchbox_text.setGeometry(QtCore.QRect(10, 50, 261, 31))
        self.Searchbox_text.setObjectName(_fromUtf8("Searchbox_text"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(310, 20, 431, 151))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Blooms Category", None))
        self.groupBox.setTitle(_translate("Dialog", "Subject Edit", None))
        self.Subject_No_label.setText(_translate("Dialog", "No", None))
        self.subject_desc_label.setText(_translate("Dialog", "Description", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.update_button.setText(_translate("Dialog", "Update", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Enter the search criteria to update</span></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

