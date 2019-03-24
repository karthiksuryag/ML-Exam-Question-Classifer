from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.blooms_verbUI_GUI
from CONNECTION.DB_Handling import DBHandler
class bloomsVerbs(QDialog, GUI.blooms_verbUI_GUI.Ui_Dialog):

    def __init__(self):
        super(bloomsVerbs, self).__init__()

        self.setupUi(self)
        self.Searchbox_text.textChanged.connect(self.loadtabledata)
        bloomstaxonomy = DBHandler().getData("SELECT  taxonomy_namel from blooms_taxonomy ")
        self.comboBox.clear()


        b= [str(text[0]) for  text in bloomstaxonomy]
        for  value in b:
                self.comboBox.addItem(value)
                print(value)
    def loadtabledata(self):

         entertext = self.Searchbox_text.text()
         self.sub_code =self.comboBox.currentText()
         selectData = "SELECT taxonomy_id FROM blooms_taxonomy WHERE taxonomy_namel = '"+ self.sub_code + "'"
         taxonomyID = DBHandler().getData(selectData)
         verbLIst = "SELECT taxonomy_id,verb FROM taxonomy_verb_list WHERE verb like '%"+ entertext + "%'" \
                    " and taxonomy_id=" + str(taxonomyID[0][0]) + ""
         wup_list = DBHandler().getData(verbLIst)
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



