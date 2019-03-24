import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.QuestionUI_GUI
import nltk
import time
from CONNECTION.DB_Handling import DBHandler
from ALGORITHMS.taxonomy_Lemmatizer import Lemmatizer
from ALGORITHMS.taxonomy_VerbFinder import ExtractVerb
from ALGORITHMS.taxonomy_Wordnet_Algorithm import SimilarityChecker
from ALGORITHMS.taxonomy_TagpatternGensim import SementicSimilarityChecker
from ALGORITHMS.taxonomy_normalizeW_L_G_Tag import Normilize_algoWLGTag
from ALGORITHMS.taxonomy_convert_RankW_L_G_Tag import Getthepriority
from ALGORITHMS.taxonomy_Cosine_Algorithm import cosine_similarity_checker
from ALGORITHMS.taxonomy_CosinePreprocess import CosinePreprocess
from ALGORITHMS.taxonomy_G_AllQuestion_Algorithm import SementicSimilarityCheckerAll
from ALGORITHMS.taxonomy_All_database import taxonomy_allDatabase
from ALGORITHMS.taxonomy_Extract import Extract
class Questions(QDialog, GUI.QuestionUI_GUI.Ui_Dialog):

    def __init__(self):
        super(Questions, self).__init__()

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
        self.pushButton_Insert.clicked.connect(self.enterquestion)
        self.pushButton_Generate.clicked.connect(self.questiondataGenerate)
        self.tableWidget.cellClicked.connect(self.editpattern)
        self.pushButton_Update.clicked.connect(self.updateQuestion)
        self.pushButton_Delete.clicked.connect(self.deleteQuestions)
        self.pushButton_browse.clicked.connect(self.openFile)
        self.pushButton_extract.clicked.connect(self.extractQuestions)


    def extractQuestions(self):
        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemester = self.comboBox_Semester.currentText()
        getpaperno = self.lineEdit_Paperno.text()
        question = self.textEdit_Question.toPlainText()
        questionmark = self.spinBox_Questionmarks.text()
        print(getyear,getsubject,getsemester,getpaperno,question,questionmark)

        if (len(self.lineEdit_filelocation.text()) != 0):
            file = open(self.lineEdit_filelocation.text(),'r')
            Extract().BreakText(file,getyear,getsubject,getsemester,getpaperno)

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,"Open File")
        self.lineEdit_filelocation.setText(fileName)
    def deleteQuestions(self):

        QuestionNo=  self.lineEdit_RemainMarks.text()


        DeletequestionList = "delete from question_list where question_id="+ QuestionNo + ""
        DBHandler().setData(DeletequestionList)
        question_analysis = "delete from question_analysis where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis)
        question_analysis_groupresults = "delete from question_analysis_groupresults where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_groupresults)
        question_analysis_normalized_groupresults = "delete from question_analysis_normalized_groupresults where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_normalized_groupresults)
        question_analysis_stem = "delete from question_analysis_stem where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_stem)
        question_dataset = "delete from question_dataset where question_id="+ QuestionNo + ""
        DBHandler().setData(question_dataset)
        question_gem_simliar_no = "delete from question_gem_simliar_no where question_id="+ QuestionNo + ""
        DBHandler().setData(question_gem_simliar_no)
        question_max_cosine = "delete from question_max_cosine where question_id="+ QuestionNo + ""
        DBHandler().setData(question_max_cosine)


        self.loadquestionlist()

    def editpattern(self,row,column):

        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print(self.ID)
        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        selectData = "SELECT question,questionmarks,question_id  FROM question_list WHERE question_id ="+ str(items[0].text()) + ""
        getData = DBHandler().getData(selectData)
        print(getData[0][0])
        print(getData[0][1])


        self.textEdit_Question.setText(str(getData[0][0]))
        self.spinBox_Questionmarks.setValue((getData[0][1]))
        self.lineEdit_RemainMarks.setText(str(getData[0][2]))

    def updateQuestion(self):

        QuestionNo=  self.lineEdit_RemainMarks.text()

        newquestion = self.textEdit_Question.toPlainText()
        questionMarks = self.spinBox_Questionmarks.value()
        print(newquestion)
        print(questionMarks)
        updateData = "update question_list set question='" + str(newquestion) +  "', questionmarks=" + str(questionMarks) + ", process_complete='no' ,Question_category= 0  where question_id=" + str(QuestionNo) + ""
        print(updateData)

        DBHandler().setData(updateData)
        question_analysis = "delete from question_analysis where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis)
        question_analysis_groupresults = "delete from question_analysis_groupresults where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_groupresults)
        question_analysis_normalized_groupresults = "delete from question_analysis_normalized_groupresults where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_normalized_groupresults)
        question_analysis_stem = "delete from question_analysis_stem where question_id="+ QuestionNo + ""
        DBHandler().setData(question_analysis_stem)
        question_dataset = "delete from question_dataset where question_id="+ QuestionNo + ""
        DBHandler().setData(question_dataset)
        question_gem_simliar_no = "delete from question_gem_simliar_no where question_id="+ QuestionNo + ""
        DBHandler().setData(question_gem_simliar_no)
        question_max_cosine = "delete from question_max_cosine where question_id="+ QuestionNo + ""
        DBHandler().setData(question_max_cosine)
        self.loadquestionlist()


    def questiondataGenerate(self):
        getpaperno = self.lineEdit_Paperno.text()
        print(getpaperno)
        getquestionlist="SELECT * from question_list where process_complete ='no' and paperno="+getpaperno+ ""
        questionsList = DBHandler().getData(getquestionlist)
        print(questionsList)

        taxonomyList = []

        for question in questionsList:
            print(question[2])
            sentenses =nltk.sent_tokenize(question[2])
            sentences =[nltk.word_tokenize(sent) for sent in sentenses]
            sentences =[nltk.pos_tag(sent) for sent in sentences]
            verbList = Lemmatizer().getLematizedWord(
                    #ExtractVerb().searchVerbs1(ExtractVerb().wordTagger(WordTokeninzer().tokenize_word(question[2],1),1)))
                     ExtractVerb().searchVerbs11(sentences))

            newList = []
            for i in range(6):
                taxonomyLineList = DBHandler().getData(
                        "SELECT verb from taxonomy_verb_list where taxonomy_id=" + str(i + 1))
                taxonomyWordList = []

                for line in taxonomyLineList:
                    for word in line:
                        taxonomyWordList.append(word)
                if len(verbList) > 0 and len(taxonomyWordList) > 0:
                    temp = SimilarityChecker().calsulateSimilarity(verbList, taxonomyWordList,question[0],question[1],(i+1))

            SementicSimilarityChecker().tagpattern_Gensim_Algorithm(question[0],question[1],question[2])
            Normilize_algoWLGTag().normalize_WLGT(getpaperno,question[0])
            Getthepriority().normalized_group_rank(getpaperno,question[0])
            cosine_similarity_checker().generateCosinepatterns(getpaperno,question[0])
            CosinePreprocess().cosinePreprocess_papers(getpaperno,question[0])
            SementicSimilarityCheckerAll().allquestionGensim(question[0],question[2])
            taxonomy_allDatabase().inserttoDatabase(question[0])
            time.sleep(2)
            getsqlvalues = "UPDATE question_list SET process_complete='yes' WHERE question_id = '"+str(question[0])+"'"
            print(getsqlvalues)
            DBHandler().setData(getsqlvalues)

            self.loadquestionlist()

            print("loadquestion")



    def enterquestion(self):
        getyear = self.comboBox_Year.currentText()
        getsubject = self.comboBox_subject.currentText()
        getsemester = self.comboBox_Semester.currentText()
        getpaperno = self.lineEdit_Paperno.text()
        question = self.textEdit_Question.toPlainText()
        questionmark = self.spinBox_Questionmarks.text()
        print(getyear,getsubject,getsemester,getpaperno,question,questionmark)
        insertquestion ="insert into question_list(subject_code,question,Years,Semester,questionmarks,paperno)" \
                        "values('"+getsubject+ "','"+ question +"',"+getyear \
                        +"," +getsemester+","+questionmark +","+getpaperno+")"
        print(insertquestion)
        DBHandler().setData(insertquestion)
        self.loadquestionlist()

    def loadquestionlist(self):

         entertext = self.lineEdit_Search.text()
         getpaperno = self.lineEdit_Paperno.text()

         selectData = "SELECT question_id,process_complete,questionmarks" \
                      ",question FROM question_list WHERE subject_code " \
                      "like '%"+ entertext + "%' and paperno=" +getpaperno+ ""
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
                     brush = QtGui.QBrush(QtGui.QColor(154, 232,80))
                     brush.setStyle(QtCore.Qt.SolidPattern)
                     item.setBackground(brush)
                 elif(wup_list[i][1]=='no'):
                     brush = QtGui.QBrush(QtGui.QColor(231, 214,25))
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


