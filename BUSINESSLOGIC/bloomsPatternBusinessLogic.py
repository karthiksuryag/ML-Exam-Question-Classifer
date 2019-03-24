from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.blooms_PatternUIGUI
from CONNECTION.DB_Handling import DBHandler
from ALGORITHMS.taxonomy_pattern_Generation import pattern_generation
class bloomstappattern(QDialog, GUI.blooms_PatternUIGUI.Ui_Dialog):

    def __init__(self):
        super(bloomstappattern, self).__init__()

        self.setupUi(self)
        bloomstaxonomy = DBHandler().getData("SELECT  taxonomy_namel from blooms_taxonomy ")
        self.comboBox.clear()


        b= [str(text[0]) for  text in bloomstaxonomy]
        for  value in b:
                self.comboBox.addItem(value)
                print(value)

        self.comboBox.currentIndexChanged.connect(self.loadtabledata)
        self.Insert_button_tagpattern.clicked.connect(self.insertpattern)
        self.generate_button.clicked.connect(self.generatePatterners)
        self.delete_button.clicked.connect(self.deletepatterns)
        self.update_button.clicked.connect(self.updatepatterns)
        self.Searchbox_text_tagpattern.textChanged.connect(self.loadsearchtabledata)
        self.tableWidget.cellClicked.connect(self.editpattern)

    def updatepatterns(self):

        tagpatternNo= self.tagpatternno_text.text()
        tappatterns = self.textEdit_tagpattern.toPlainText()

        updateData = "update question_stems set question_stem='" + tappatterns +  "', Tag_pattern='no',grammer_tag_pattern='no',pattern_set='no'  where id=" + tagpatternNo + ""
        print(updateData)

        DBHandler().setData(updateData)
        self.loadsearchtabledata()


    def deletepatterns(self):

        tagpatternNo= self.tagpatternno_text.text()

        updateData = "delete from question_stems where id="+ tagpatternNo + ""
        DBHandler().setData(updateData)
        self.loadsearchtabledata()

    def editpattern(self,row,column):

        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print(self.ID)
        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        selectData = "SELECT id, question_stem FROM question_stems WHERE id ="+ str(items[0].text()) + ""
        getData = DBHandler().getData(selectData)
        print(getData[0][0])
        print(getData[0][1])
        self.tagpatternno_text.setText(str(getData[0][0]))
        self.tagpatternno_text.setDisabled(True)
        self.textEdit_tagpattern.setText(str(getData[0][1]))

    def loadsearchtabledata(self):
         entertext = self.Searchbox_text_tagpattern.text()
         selectData = "SELECT id,question_stem,Tag_pattern,grammer_tag_pattern FROM question_stems WHERE question_stem like '%"+ entertext + "%'"
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

    def generatePatterners(self):
        pattern_generation().generation()
        self.loadtabledata()

    def loadtabledata(self):
         self.tableWidget.clear()
        # entertext = self.Searchbox_text.text()
         selectData = "SELECT id,question_stem,Tag_pattern,grammer_tag_pattern FROM question_stems WHERE pattern_set='no'"
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
                 brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                 brush.setStyle(QtCore.Qt.SolidPattern)
                 self.tableWidget.setItem(i, j, item)


         print(wup_list[0][1])


    def insertpattern(self):

        tagpattern = self.textAdd_tagpattern.toPlainText()
        bloomscategory = self.comboBox.currentText()
        selectData = "SELECT taxonomy_id,taxonomy_namel FROM blooms_taxonomy WHERE taxonomy_namel like '%"+ bloomscategory + "%'"
        wup_list = DBHandler().getData(selectData)
        print(wup_list)
        insertsql = "insert into question_stems(taxonomy_id,question_stem)values("+str(wup_list[0][0])+ ",'"+str(tagpattern)+"')"
        print(insertsql)
        DBHandler().setData(insertsql)
        self.loadtabledata()

