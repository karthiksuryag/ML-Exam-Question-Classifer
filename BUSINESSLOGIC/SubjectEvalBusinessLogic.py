__author__ = 'ASUS'
import sys
from PyQt4 import QtGui
import numpy as np
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
import GUI.SubjectEvalUI_GUI
from CONNECTION.DB_Handling import DBHandler
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class subjectsEval(QDialog, GUI.SubjectEvalUI_GUI.Ui_Dialog):
    selectvalue=""
    def __init__(self):
        super(subjectsEval, self).__init__()

        self.setupUi(self)

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

        self.spinBox_Know.valueChanged.connect(self.printData)
        self.spinBox_Comp.valueChanged.connect(self.printData)
        self.spinBox_Appl.valueChanged.connect(self.printData)
        self.spinBox_Anal.valueChanged.connect(self.printData)
        self.spinBox_Synt.valueChanged.connect(self.printData)
        self.spinBox_Eval.valueChanged.connect(self.printData)
        self.pushButton_Insert.clicked.connect(self.insertSubjectEvaluation)
        self.tableWidget.cellClicked.connect(self.drawGraph)
        self.comboBox_subject.currentIndexChanged.connect(self.loaddescription)
        self.tableWidget.cellClicked.connect(self.editsubjectBloom)
        self.pushButton_Update.clicked.connect(self.updateSubEval)
        self.pushButton_Delete.clicked.connect(self.deletesubjeEval)

        self.loadtabledata()
        subjectlist = DBHandler().getData("SELECT  subject_code from subject ")
        self.comboBox_subject.clear()
        self.buttonEnable()

        b= [str(text[0]) for  text in subjectlist]
        for  value in b:
                self.comboBox_subject.addItem(value)
                print(value)
        subject = self.comboBox_subject.currentText()
        getdescription = "SELECT  description from subject where subject_code='"+ str(subject)+ "'"
        subjectDescription = DBHandler().getData(getdescription)
        self.textEdit_SubjectDescription.setText(str(subjectDescription[0][0]))

    def deletesubjeEval(self):

        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        updateData = "delete from subject_evaluation where Nos="+ str(items[0].text()) + ""
        DBHandler().setData(updateData)
        self.loadtabledata()

    def updateSubEval(self):

        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))

        comprehensionValue = self.spinBox_Comp.value()
        analysisValue = self.spinBox_Anal.value()
        synthesisValue = self.spinBox_Synt.value()
        applicationValue = self.spinBox_Appl.value()
        knowledgeValue = self.spinBox_Know.value()
        evaluationValue = self.spinBox_Eval.value()
        updateData = "update questions set evaluation_A='" + str(knowledgeValue) +\
                     "', evaluation_B='" + str(comprehensionValue) + \
                     "', evaluation_C='" + str(applicationValue) + \
                     "', evaluation_D='" + str(analysisValue) + \
                     "', evaluation_E='" + str(synthesisValue) + \
                     "', evaluation_F='" + str(evaluationValue) +  \
                     "'  where Nos=" + str(items[0].text()) + ""

        print(updateData)

        DBHandler().setData(updateData)
        self.loadtabledata()
        self.drawGraph()

    def editsubjectBloom(self,row,column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print(self.ID)
        items = self.tableWidget.selectedItems()
        selectvalue=str(items[0].text())
        print(str(items[0].text()))
        selectData = "SELECT evaluation_A,evaluation_B,evaluation_C,evaluation_D,evaluation_E,evaluation_F FROM subject_evaluation WHERE Nos ="+ str(items[0].text()) + ""
        getData = DBHandler().getData(selectData)
        print(getData[0][0])
        print(getData[0][1])
        self.spinBox_Know.setValue(getData[0][0])
        self.spinBox_Comp.setValue(getData[0][1])
        self.spinBox_Appl.setValue(getData[0][2])
        self.spinBox_Anal.setValue(getData[0][3])
        self.spinBox_Synt.setValue(getData[0][4])
        self.spinBox_Eval.setValue(getData[0][5])
        self.pushButton_Delete.setEnabled(True)
        self.pushButton_Update.setEnabled(True)

    def loaddescription(self):
        subject = self.comboBox_subject.currentText()
        getdescription = "SELECT  description from subject where subject_code='"+ str(subject)+ "'"
        subjectDescription = DBHandler().getData(getdescription)
        self.textEdit_SubjectDescription.setText(str(subjectDescription[0][0]))


    def drawGraph(self):

        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        subjectcategory = DBHandler().getData("SELECT evaluation_A,evaluation_B,evaluation_C,evaluation_D,evaluation_E,evaluation_F from subject_evaluation where Nos='"+str(items[0].text())+"' LIMIT 1")
        no_categories = len(subjectcategory[0])
        highest_wup_values = subjectcategory[0]
        index = np.arange(no_categories)
        lables=['Kno','Com','App','Ana','Syn','Eval']
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        highest_wup_values_set=[100,100,100,100,100,100]
        self.mpl.canvas.ax.bar(index, highest_wup_values_set, bar_width,

                 color='w',
                 label='Total Verbs')



        self.mpl.canvas.draw()
        self.mpl.canvas.ax.bar(index, highest_wup_values, bar_width, alpha=opacity,

                 color='mrybkg',
                 label='Total Verbs')
        self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(subjectcategory[0])-0.75)

        self.mpl.canvas.ax.set_xticks(range(len(subjectcategory[0])))
        self.mpl.canvas.ax.set_xticklabels(lables)
        self.mpl.canvas.ax.grid(True)

        #self.mpl.canvas.ax.get_yaxis().grid(True)

        self.mpl.canvas.draw()
        self.loadsubjectDescription()

    def loadsubjectDescription(self):
        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        subjectcategory = DBHandler().getData("SELECT subject from subject_evaluation where Nos='"+str(items[0].text())+"' LIMIT 1")
        description = DBHandler().getData("SELECT description from subject where subject_code='"+str(subjectcategory[0][0])+"' LIMIT 1")
        self.textEdit_SubjectDescription.setText(str(description[0][0]))

    def buttonEnable(self):
        self.pushButton_Delete.setEnabled(False)
        self.pushButton_Update.setEnabled(False)
        self.pushButton_Cancel.setEnabled(False)

    def insertSubjectEvaluation(self):

        subject = self.comboBox_subject.currentText()
        year = self.comboBox_Year.currentText()
        semester = self.comboBox_Semester.currentText()
        comprehensionValue = self.spinBox_Comp.value()
        analysisValue = self.spinBox_Anal.value()
        synthesisValue = self.spinBox_Synt.value()
        applicationValue = self.spinBox_Appl.value()
        knowledgeValue = self.spinBox_Know.value()
        evaluationValue = self.spinBox_Eval.value()
        insertsql = "insert into subject_evaluation(subject,years,semester,evaluation_A,evaluation_B" \
                    ",evaluation_C,evaluation_D,evaluation_E,evaluation_F)values('"+str(subject)+ "'," \
                    +str(year) +"," + str(semester) +","+ str(knowledgeValue) + "," +str(comprehensionValue)+ "," \
                    +str(applicationValue) +"," + str(analysisValue) +"," + str(synthesisValue)  +"," +str(evaluationValue)+")"
        DBHandler().setData(insertsql)
        self.loadtabledata()


    def loadtabledata(self):

         entertext = self.lineEdit_Search.text()
         selectData = "SELECT * FROM subject_evaluation WHERE subject like '%"+ entertext + "%'"
         wup_list = DBHandler().getData(selectData)
         print(len(wup_list))
         print(len(wup_list[0]))
         rows =  len(wup_list)
         columns = len(wup_list[0])
         i  =0
         j  =0
         self.tableWidget.clearContents()
         for i in range(0,rows):
            for j in range(0,columns):

                 item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                 self.tableWidget.setItem(i, j, item)


         print(wup_list[0][1])


    def printData(self):

        maxValue = 0

        comprehensionValue = self.spinBox_Comp.value()
        analysisValue = self.spinBox_Anal.value()
        synthesisValue = self.spinBox_Synt.value()
        applicationValue = self.spinBox_Appl.value()
        knowledgeValue = self.spinBox_Know.value()
        evaluationValue = self.spinBox_Eval.value()

        maxValue = 100 - (comprehensionValue + analysisValue + synthesisValue + applicationValue + knowledgeValue +
                          evaluationValue)

        self.spinBox_Eval.setMaximum(maxValue + evaluationValue)
        self.spinBox_Appl.setMaximum(maxValue + applicationValue)
        self.spinBox_Know.setMaximum(maxValue + knowledgeValue)
        self.spinBox_Comp.setMaximum(maxValue + comprehensionValue)
        self.spinBox_Synt.setMaximum(maxValue + synthesisValue)
        self.spinBox_Anal.setMaximum(maxValue + analysisValue)


app = QtGui.QApplication(sys.argv)
ex = subjectsEval()
ex.show()

ex.exec_()
