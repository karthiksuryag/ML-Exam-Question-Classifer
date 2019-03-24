# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blooms_PatternUI.ui'
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
        Dialog.resize(1053, 545)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(290, 380, 741, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Subject_No_label = QtGui.QLabel(self.groupBox)
        self.Subject_No_label.setGeometry(QtCore.QRect(10, 30, 53, 16))
        self.Subject_No_label.setObjectName(_fromUtf8("Subject_No_label"))
        self.tagpatternno_text = QtGui.QLineEdit(self.groupBox)
        self.tagpatternno_text.setGeometry(QtCore.QRect(110, 30, 113, 22))
        self.tagpatternno_text.setObjectName(_fromUtf8("tagpatternno_text"))
        self.subject_desc_label = QtGui.QLabel(self.groupBox)
        self.subject_desc_label.setGeometry(QtCore.QRect(280, 30, 81, 16))
        self.subject_desc_label.setObjectName(_fromUtf8("subject_desc_label"))
        self.textEdit_tagpattern = QtGui.QTextEdit(self.groupBox)
        self.textEdit_tagpattern.setGeometry(QtCore.QRect(380, 20, 351, 31))
        self.textEdit_tagpattern.setObjectName(_fromUtf8("textEdit_tagpattern"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 460, 741, 71))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.cancel_button = QtGui.QPushButton(self.groupBox_2)
        self.cancel_button.setGeometry(QtCore.QRect(620, 20, 93, 28))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.update_button = QtGui.QPushButton(self.groupBox_2)
        self.update_button.setGeometry(QtCore.QRect(510, 20, 93, 28))
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.delete_button = QtGui.QPushButton(self.groupBox_2)
        self.delete_button.setGeometry(QtCore.QRect(400, 20, 93, 28))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 10, 411, 121))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(190, 0, 231, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Searchbox_text_tagpattern = QtGui.QLineEdit(self.groupBox_3)
        self.Searchbox_text_tagpattern.setGeometry(QtCore.QRect(120, 50, 271, 31))
        self.Searchbox_text_tagpattern.setObjectName(_fromUtf8("Searchbox_text_tagpattern"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 1021, 231))
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 581, 121))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 231, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(430, 10, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 171, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Insert_button_tagpattern = QtGui.QPushButton(self.groupBox_4)
        self.Insert_button_tagpattern.setGeometry(QtCore.QRect(470, 80, 93, 28))
        self.Insert_button_tagpattern.setObjectName(_fromUtf8("Insert_button_tagpattern"))
        self.textAdd_tagpattern = QtGui.QTextEdit(self.groupBox_4)
        self.textAdd_tagpattern.setGeometry(QtCore.QRect(210, 40, 351, 31))
        self.textAdd_tagpattern.setObjectName(_fromUtf8("textAdd_tagpattern"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 390, 261, 141))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 261, 51))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Searchbox_text_nopattern = QtGui.QLineEdit(self.groupBox_5)
        self.Searchbox_text_nopattern.setGeometry(QtCore.QRect(120, 20, 141, 31))
        self.Searchbox_text_nopattern.setObjectName(_fromUtf8("Searchbox_text_nopattern"))
        self.generate_button = QtGui.QPushButton(self.groupBox_5)
        self.generate_button.setGeometry(QtCore.QRect(160, 77, 93, 51))
        self.generate_button.setObjectName(_fromUtf8("generate_button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Blooms Question Stem Tag pattern", None))
        self.groupBox.setTitle(_translate("Dialog", "Tag pattern Edit", None))
        self.Subject_No_label.setText(_translate("Dialog", "No", None))
        self.subject_desc_label.setText(_translate("Dialog", "Description", None))
        self.cancel_button.setText(_translate("Dialog", "Cancel", None))
        self.update_button.setText(_translate("Dialog", "Update", None))
        self.delete_button.setText(_translate("Dialog", "Delete", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Enter the search criteria to update</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Select the Taxonmy</span></p><p><br/></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Enter the Question pattern</span></p><p><br/></p></body></html>", None))
        self.Insert_button_tagpattern.setText(_translate("Dialog", "Insert", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">Enter No keyword to select the ungenerated </span></p><p><span style=\" color:#00007f;\">question stems</span></p><p><br/></p></body></html>", None))
        self.generate_button.setText(_translate("Dialog", "Generate", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())