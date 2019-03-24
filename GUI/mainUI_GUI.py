# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore

import GUI.blooms_categoryUI_GUI
import GUI.blooms_verbUI_GUI
import GUI.blooms_PatternUIGUI
import BUSINESSLOGIC.SubjectBusinessLogic
import BUSINESSLOGIC.SubjectEvalBusinessLogic
import BUSINESSLOGIC.bloomsVerbBusinessLogic
import BUSINESSLOGIC.bloomsPatternBusinessLogic
import BUSINESSLOGIC.bloomsCategoryBusinessLogic
import BUSINESSLOGIC.QuestionBusinessLogic
import BUSINESSLOGIC.QuestionpaperBusinessLogic
import BUSINESSLOGIC.traningClassificationBusinessLogic
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
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1229, 786)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/application.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1229, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTaxonmy = QtGui.QMenu(self.menubar)
        self.menuTaxonmy.setObjectName(_fromUtf8("menuTaxonmy"))
        self.menuSubjects = QtGui.QMenu(self.menubar)
        self.menuSubjects.setObjectName(_fromUtf8("menuSubjects"))
        self.menuQuestion = QtGui.QMenu(self.menubar)
        self.menuQuestion.setObjectName(_fromUtf8("menuQuestion"))
        self.menuAnalysis = QtGui.QMenu(self.menubar)
        self.menuAnalysis.setObjectName(_fromUtf8("menuAnalysis"))
        self.menuReports = QtGui.QMenu(self.menubar)
        self.menuReports.setObjectName(_fromUtf8("menuReports"))
        self.menuExit = QtGui.QMenu(self.menubar)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(45, 45))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCategory = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/homework.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCategory.setIcon(icon1)
        self.actionCategory.setObjectName(_fromUtf8("actionCategory"))
        self.actionVerbs = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/notepad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVerbs.setIcon(icon2)
        self.actionVerbs.setObjectName(_fromUtf8("actionVerbs"))
        self.actionTag_Patterns = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/blackboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTag_Patterns.setIcon(icon3)
        self.actionTag_Patterns.setObjectName(_fromUtf8("actionTag_Patterns"))
        self.actionNew_Subjects = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/emblem_library.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Subjects.setIcon(icon4)
        self.actionNew_Subjects.setObjectName(_fromUtf8("actionNew_Subjects"))
        self.actionCategory_Levels = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/presentation_edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCategory_Levels.setIcon(icon5)
        self.actionCategory_Levels.setObjectName(_fromUtf8("actionCategory_Levels"))
        self.actionExtraction = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/kivio.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExtraction.setIcon(icon6)
        self.actionExtraction.setObjectName(_fromUtf8("actionExtraction"))
        self.actionClassification = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/spreadsheet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClassification.setIcon(icon7)
        self.actionClassification.setObjectName(_fromUtf8("actionClassification"))
        self.actionComparision = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/settings2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionComparision.setIcon(icon8)
        self.actionComparision.setObjectName(_fromUtf8("actionComparision"))
        self.actionAnalized_reports = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/report.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalized_reports.setIcon(icon9)
        self.actionAnalized_reports.setObjectName(_fromUtf8("actionAnalized_reports"))
        self.actionExit_Application = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/ICONS/switch_user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit_Application.setIcon(icon10)
        self.actionExit_Application.setObjectName(_fromUtf8("actionExit_Application"))
        self.menuTaxonmy.addSeparator()
        self.menuTaxonmy.addAction(self.actionCategory)
        self.menuTaxonmy.addSeparator()
        self.menuTaxonmy.addAction(self.actionVerbs)
        self.menuTaxonmy.addAction(self.actionTag_Patterns)
        self.menuSubjects.addSeparator()
        self.menuSubjects.addAction(self.actionNew_Subjects)
        self.menuSubjects.addAction(self.actionCategory_Levels)
        self.menuQuestion.addAction(self.actionExtraction)
        self.menuQuestion.addAction(self.actionClassification)
        self.menuAnalysis.addAction(self.actionComparision)
        self.menuReports.addAction(self.actionAnalized_reports)
        self.menuExit.addAction(self.actionExit_Application)
        self.menubar.addAction(self.menuTaxonmy.menuAction())
        self.menubar.addAction(self.menuSubjects.menuAction())
        self.menubar.addAction(self.menuQuestion.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionCategory)
        self.toolBar.addAction(self.actionVerbs)
        self.toolBar.addAction(self.actionTag_Patterns)
        self.toolBar.addAction(self.actionNew_Subjects)
        self.toolBar.addAction(self.actionCategory_Levels)
        self.toolBar.addAction(self.actionExtraction)
        self.toolBar.addAction(self.actionClassification)
        self.toolBar.addAction(self.actionComparision)
        self.toolBar.addAction(self.actionAnalized_reports)
        self.toolBar.addAction(self.actionExit_Application)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Taxonomy Main Window", None))
        self.menuTaxonmy.setTitle(_translate("MainWindow", "Taxonmy", None))
        self.menuSubjects.setTitle(_translate("MainWindow", "Subjects", None))
        self.menuQuestion.setTitle(_translate("MainWindow", "Question", None))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis", None))
        self.menuReports.setTitle(_translate("MainWindow", "Reports", None))
        self.menuExit.setTitle(_translate("MainWindow", "Exit", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionCategory.setText(_translate("MainWindow", "Category", None))
        self.actionVerbs.setText(_translate("MainWindow", "Verbs", None))
        self.actionTag_Patterns.setText(_translate("MainWindow", "Tag Patterns", None))
        self.actionNew_Subjects.setText(_translate("MainWindow", "New Subjects", None))
        self.actionCategory_Levels.setText(_translate("MainWindow", "Category Levels", None))
        self.actionExtraction.setText(_translate("MainWindow", "Extraction", None))
        self.actionClassification.setText(_translate("MainWindow", "Classification", None))
        self.actionComparision.setText(_translate("MainWindow", "Comparision", None))
        self.actionAnalized_reports.setText(_translate("MainWindow", "Analized reports", None))
        self.actionExit_Application.setText(_translate("MainWindow", "Exit Application", None))

        self.actionCategory.triggered.connect(self.loadcategory)
        self.actionVerbs.triggered.connect(self.loadverbs)
        self.actionTag_Patterns.triggered.connect(self.loadpatterns)
        self.actionNew_Subjects.triggered.connect(self.loadsubjects)
        self.actionCategory_Levels.triggered.connect(self.loadevaluation)
        self.actionExtraction.triggered.connect(self.loadquestionpapers)
        self.actionClassification.triggered.connect(self.loadquestions)
        self.actionComparision.triggered.connect(self.loadclassification)

    def loadclassification(self):
        ex = BUSINESSLOGIC.traningClassificationBusinessLogic.training()
        ex.show()
        ex.exec()

    def loadquestions(self):
        ex = BUSINESSLOGIC.QuestionBusinessLogic.Questions()

        ex.show()
        ex.exec()


    def loadquestionpapers(self):
        ex= BUSINESSLOGIC.QuestionpaperBusinessLogic.Questionpaper()
        ex.show()
        ex.exec()

    def loadcategory(self):
        ex = BUSINESSLOGIC.bloomsCategoryBusinessLogic.bloomscategory()
        ex.show()
        ex.exec()
    def loadverbs(self):
        ex = BUSINESSLOGIC.bloomsVerbBusinessLogic.bloomsVerbs()
        ex.show()
        ex.exec()

    def loadpatterns(self):
        ex = BUSINESSLOGIC.bloomsPatternBusinessLogic.bloomstappattern()
        ex.show()
        ex.exec()

    def loadsubjects(self):
        ex = BUSINESSLOGIC.SubjectBusinessLogic.subjects()
        ex.show()
        ex.exec()

    def loadevaluation(self):
        ex = BUSINESSLOGIC.SubjectEvalBusinessLogic.subjectsEval()
        ex.show()
        ex.exec()
import banner_rc


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

