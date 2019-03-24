from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import sys
import numpy as np
import GUI.TrainingUI_GUI
from CONNECTION.DB_Handling import DBHandler
from ALGORITHMS.taxonomy_Training import MachineLearning

class training(QDialog, GUI.TrainingUI_GUI.Ui_Dialog):

    def __init__(self):
        super(training, self).__init__()

        self.setupUi(self)

        subjectlist = DBHandler().getData("SELECT  DISTINCT  subject from exam_paper ")
        self.comboBox_subject.clear()
        b= [str(text[0]) for  text in subjectlist]
        for  value in b:
                self.comboBox_subject.addItem(value)
                print(value)
        self.comboBox_subject.currentIndexChanged.connect(self.loadyears)
        self.comboBox_Year.currentIndexChanged.connect(self.loadsemesters)
        self.comboBox_Semester.currentIndexChanged.connect(self.laodpapertypes)
        self.comboBox_papertype.currentIndexChanged.connect(self.loaddates)
        self.comboBox_date.currentIndexChanged.connect(self.loadmarks)
        self.pushButton_Generate.clicked.connect(self.questionClassification)
        self.comboBox_subject.currentIndexChanged.connect(self.drawGraph)


    def loadQuestionCategorizationGraph(self):
        LoadList = []
        getpaperno = self.lineEdit_Paperno.text()
        sqlpapermarks = self.lineEdit_Papermarks.text()

        sqlknowledge = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=1 ;"
        print(sqlknowledge)
        getsqlknow = DBHandler().getData(sqlknowledge)

        knowmarks = getsqlknow[0][0]
        if(knowmarks is not None):
            marks = (int(knowmarks)/int(sqlpapermarks))*100
            print(marks)
            LoadList.append(marks)
        else:
            marks = 0
            LoadList.append(marks)
        sqlcomp = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=2 ;"
        print(sqlcomp)
        getsqlcomp = DBHandler().getData(sqlcomp)

        print(getsqlcomp)
        compmarks = getsqlcomp[0][0]
        if(compmarks is not None):
            print(compmarks)
            markscomp = (int(compmarks)/int(sqlpapermarks))*100
            print(markscomp)
            LoadList.append(markscomp)
        else:
            marks = 0
            LoadList.append(marks)
        #
        sqlApplication = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=3 ;"
        print(sqlApplication)
        getsqlApplication = DBHandler().getData(sqlApplication)
        appmarks = getsqlApplication[0][0]
        if(appmarks is not None):
            marksapp = (int(appmarks)/int(sqlpapermarks))*100
            print(marksapp)
            LoadList.append(marksapp)
        else:
            marks = 0
            LoadList.append(marks)
        #
        sqlAnalysis = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=4 ;"
        print(sqlAnalysis)
        getsqlAnalysis = DBHandler().getData(sqlAnalysis)

        anamarks = getsqlAnalysis[0][0]
        if(anamarks is not None):
            marksana = (int(anamarks)/int(sqlpapermarks))*100
            print(marksana)
            LoadList.append(marksana)
        else:
            marks = 0
            LoadList.append(marks)
        #
        sqlSynthesis = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=5 ;"
        print(sqlSynthesis)
        getSynthesis = DBHandler().getData(sqlSynthesis)

        synmarks = getSynthesis[0][0]
        if(synmarks is not None):
            markssyn = (int(synmarks)/int(sqlpapermarks))*100
            print(markssyn)
            LoadList.append(markssyn)
        else:
            marks = 0
            LoadList.append(marks)
        #
        sqlEvaluation = "SELECT sum(questionmarks) FROM nlp_compare.question_list where paperno="+getpaperno+ " and Question_category=6 ;"
        print(sqlEvaluation)
        getEvaluation = DBHandler().getData(sqlEvaluation)

        evalmarks = getEvaluation[0][0]
        if(evalmarks is not None):
            markseval = (int(evalmarks)/int(sqlpapermarks))*100
            print(markseval)
            LoadList.append(markseval)
        else:
            marks = 0
            LoadList.append(marks)
        #
        print(LoadList)

        stringvalue = ', '.join(map(str, LoadList))



        self.textEdit_Recomendation.append("Subject Evaluation")
        self.textEdit_Recomendation.append(stringvalue)

        no_categories = len(LoadList)
        highest_wup_values = LoadList
        index = np.arange(no_categories)
        lables=['Kno','Com','App','Ana','Syn','Eval']
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        highest_wup_values_set=[100,100,100,100,100,100]
        self.mpl1.canvas.ax.bar(index, highest_wup_values_set, bar_width,

                 color='w',
                 label='Total Verbs')



        self.mpl1.canvas.draw()
        self.mpl1.canvas.ax.bar(index, highest_wup_values, bar_width, alpha=opacity,

                 color='mrybkg',
                 label='Total Verbs')
        self.mpl1.canvas.ax.set_xlim(xmin=-0.25, xmax=len(LoadList)-0.75)

        self.mpl1.canvas.ax.set_xticks(range(len(LoadList)))
        self.mpl1.canvas.ax.set_xticklabels(lables)
        self.mpl1.canvas.ax.grid(True)

        #self.mpl.canvas.ax.get_yaxis().grid(True)

        self.mpl1.canvas.draw()


    def drawGraph(self):

        subjectname = self.comboBox_subject.currentText()
        print(subjectname)
        subjectcategory = DBHandler().getData("SELECT evaluation_A,evaluation_B,evaluation_C,evaluation_D,evaluation_E,evaluation_F from subject_evaluation where subject='"+str(subjectname)+"' LIMIT 1")
        no_categories = len(subjectcategory[0])
        highest_wup_values = subjectcategory[0]
        stringvalue = ', '.join(map(str, highest_wup_values))

        self.textEdit_Recomendation.clear()
        self.textEdit_Recomendation.append("Paper Evaluation")
        self.textEdit_Recomendation.append(stringvalue)
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



    def questionClassification(self):
        getpaperno = self.lineEdit_Paperno.text()
        MachineLearning().questionClassification(getpaperno)
        self.loadQuestionCategorizationGraph()
        self.loadquestionlist()

    def loadquestionlist(self):


         getpaperno = self.lineEdit_Paperno.text()

         selectData = "SELECT question_id,process_complete,Question_category,questionmarks" \
                      ",question FROM question_list WHERE paperno=" +getpaperno+ ""
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
                 if(wup_list[i][1]=='yes'):
                     brush = QtGui.QBrush(QtGui.QColor(238, 238,178))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][1]=='no'):
                     brush = QtGui.QBrush(QtGui.QColor(231, 214,25))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==1):
                     brush = QtGui.QBrush(QtGui.QColor(251, 216,255))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==2):
                     brush = QtGui.QBrush(QtGui.QColor(255, 155,105))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==3):
                     brush = QtGui.QBrush(QtGui.QColor(248, 255,170))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==4):
                     brush = QtGui.QBrush(QtGui.QColor(139, 191,255))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==5):
                     brush = QtGui.QBrush(QtGui.QColor(171, 171,171))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 if(wup_list[i][2]==6):
                     brush = QtGui.QBrush(QtGui.QColor(160, 255,190))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 self.tableWidget.setItem(i, j, item)




         print(wup_list[0][1])
    def loaddates(self):

        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemester = self.comboBox_Semester.currentText()
        getpapertype = self.comboBox_papertype.currentText()
        getdates = "SELECT DISTINCT dates from exam_paper" \
                          " where years=" +getyear+ " and subject='" + getsubject +\
                          "' and semester="+getsemester+ " and papertype='"+getpapertype+ "'"
        datelist = DBHandler().getData(getdates)
        self.comboBox_date.clear()
        b= [str(text[0]) for  text in datelist]
        for  value in b:
                self.comboBox_date.addItem(value)
        self.loadquestionlist()

    def laodpapertypes(self):

        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemester = self.comboBox_Semester.currentText()
        getpapertypes = "SELECT DISTINCT papertype from exam_paper" \
                          " where years=" +getyear+ " and subject='" + getsubject + "' and semester="+getsemester+ ""
        paperset = DBHandler().getData(getpapertypes)
        self.comboBox_papertype.clear()
        self.comboBox_date.clear()
        b= [str(text[0]) for  text in paperset]
        for  value in b:
                self.comboBox_papertype.addItem(value)

    def loadmarks(self):
        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemester = self.comboBox_Semester.currentText()
        getpapertype = self.comboBox_papertype.currentText()
        getdate = self.comboBox_date.currentText()
        papermarks = "select papermarks,No from exam_paper where subject='"\
                     +getsubject+ "' and years=" + getyear + \
                        " and semester=" +getsemester+ " and papertype='" +getpapertype+ "' " \
                        "and dates= '" +getdate+ "'"
        gettotalmarks=DBHandler().getData(papermarks)
        self.lineEdit_TotalMarks.setText(str(gettotalmarks[0][0]))
        self.lineEdit_Paperno.setEnabled(False)
        paperno = gettotalmarks[0][1]
        self.lineEdit_Paperno.setText(str(paperno))
        self.lineEdit_Papermarks.setText(str(gettotalmarks[0][0]))
        nowMarks = "select sum(questionmarks) from question_list where paperno =" +str(paperno) + ""
        print(nowMarks)
        getnowMarks=DBHandler().getData(nowMarks)
        print(getnowMarks)
        if(nowMarks is not None):
            remainmarks = gettotalmarks[0][0]- getnowMarks[0][0]
            self.lineEdit_RemainMarks.setText(str(remainmarks))





    def loadyears(self):

        getsubject = self.comboBox_subject.currentText()
        getyearlist = "SELECT DISTINCT years from exam_paper where subject='" +getsubject+ "'"
        yearlist = DBHandler().getData(getyearlist)
        self.comboBox_Year.clear()
        self.comboBox_Semester.clear()
        self.comboBox_papertype.clear()
        self.comboBox_date.clear()
        b= [str(text[0]) for  text in yearlist]
        for  value in b:
                self.comboBox_Year.addItem(value)


    def loadsemesters(self):

        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemesterlist = "SELECT DISTINCT semester from exam_paper" \
                          " where years=" +getyear+ " and subject='" + getsubject + "'"
        yearlist = DBHandler().getData(getsemesterlist)
        self.comboBox_Semester.clear()
        self.comboBox_papertype.clear()
        self.comboBox_date.clear()
        b= [str(text[0]) for  text in yearlist]
        for  value in b:
                self.comboBox_Semester.addItem(value)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ex = training()
    ex.show()
    ex.exec()
    sys.exit(app.exec_())
