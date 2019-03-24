import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.QuestionpaperUI_GUI
from CONNECTION.DB_Handling import DBHandler
class Questionpaper(QDialog, GUI.QuestionpaperUI_GUI.Ui_Dialog):

    def __init__(self):
        super(Questionpaper, self).__init__()

        self.setupUi(self)
        subjectlist = DBHandler().getData("SELECT  subject_code from subject ")
        self.comboBox_subject.clear()
        self.pushButton_Insert.clicked.connect(self.insertPapers)
        self.lineEdit_Search.textChanged.connect(self.loadtabledata)
        self.tableWidget.cellClicked.connect(self.editpattern)
        self.pushButton_Update.clicked.connect(self.updatepaper)
        self.pushButton_Delete.clicked.connect(self.deletepapers)
        b= [str(text[0]) for  text in subjectlist]
        for  value in b:
                self.comboBox_subject.addItem(value)
                print(value)

    def deletepapers(self):

        paperNo=  self.lineEdit_RemainMarks.text()


        updateData = "delete from exam_paper where No="+ paperNo + ""
        DBHandler().setData(updateData)
        self.loadtabledata()

    def updatepaper(self):

        paperNo=  self.lineEdit_RemainMarks.text()

        dates = self.dateEdit.text()
        papermarks = self.spinBox_papermarks.value()
        print(dates)
        print(papermarks)
        updateData = "update exam_paper set dates='" + str(dates) +  "', papermarks=" + str(papermarks) +  "  where No=" + str(paperNo) + ""
        print(updateData)

        DBHandler().setData(updateData)
        self.loadtabledata()

    def editpattern(self,row,column):

        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print(self.ID)
        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        selectData = "SELECT subject,years,semester,papertype,dates,papermarks  FROM exam_paper WHERE No ="+ str(items[0].text()) + ""
        getData = DBHandler().getData(selectData)
        print(getData[0][0])
        print(getData[0][1])
        value=0
        if(getData[0][1]=='2016'):
            value=1
        elif(getData[0][1]=='2017'):
            value=2

        self.lineEdit_RemainMarks.setText(str(items[0].text()))
        self.comboBox_Year.setCurrentIndex(value)
        self.comboBox_Semester.setEditText((str(getData[0][2])))
        self.comboBox_papertype.setEditText((str(getData[0][3])))
        self.dateEdit.setDate(getData[0][4])
        self.spinBox_papermarks.setValue(getData[0][5])


    def insertPapers(self):
        subject = self.comboBox_subject.currentText()
        year = self.comboBox_Year.currentText()
        semester = self.comboBox_Semester.currentText()
        date = self.dateEdit.text()
        papertype = self.comboBox_papertype.currentText()
        papermarks = self.spinBox_papermarks.value()

        insertsql = "insert into exam_paper(subject,years,semester,papertype,dates" \
                    ",papermarks)values('"+str(subject)+ "'," \
                    +str(year) +"," + str(semester) +",'"+ str(papertype) + "','" +str(date)+ "'," \
                    +str(papermarks)+")"
        DBHandler().setData(insertsql)
        self.loadtabledata()


    def loadtabledata(self):

         entertext = self.lineEdit_Search.text()
         selectData = "SELECT * FROM exam_paper WHERE subject like '%"+ entertext + "%'"
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


EX = Questionpaper()
EX.SHOW()
EX.exec_()