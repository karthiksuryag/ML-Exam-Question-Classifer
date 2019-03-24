import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.blooms_categoryUI_GUI
from CONNECTION.DB_Handling import DBHandler


class bloomscategory(QDialog, GUI.blooms_categoryUI_GUI.Ui_Dialog):

    def __init__(self):
        super(bloomscategory, self).__init__()

        self.setupUi(self)
        self.Searchbox_text.textChanged.connect(self.loadtabledata)
        self.tableWidget.cellClicked.connect(self.loadselection)
        self.update_button.clicked.connect(self.updateTaxonomy)
        #self.cancel_button.clicked.connect(self.removeTaxonomy)

    def updateTaxonomy(self):

        taxonomyNO= self.Subject_no_text.text()
        description =self.Subject_description_text.text()
        updateData = "update blooms_taxonomy set taxonomy_namel='" + description + "' where taxonomy_id=" + taxonomyNO + ""
        DBHandler().setData(updateData)
        self.loadtabledata()



    def loadtabledata(self):

         entertext = self.Searchbox_text.text()
         selectData = "SELECT taxonomy_id,taxonomy_namel FROM blooms_taxonomy WHERE taxonomy_namel like '%"+ entertext + "%'"
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
                 item.setBackground(brush)
                 self.tableWidget.setItem(i, j, item)


         print(wup_list[0][1])


    def loadselection(self,row,column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.itemAt(row, column)
        self.ID = item.text()
        print(self.ID)
        items = self.tableWidget.selectedItems()
        print(str(items[0].text()))
        selectData = "SELECT taxonomy_id,taxonomy_namel FROM blooms_taxonomy WHERE taxonomy_id ="+ str(items[0].text()) + ""
        getData = DBHandler().getData(selectData)
        print(getData[0][0])
        print(getData[0][1])
        self.Subject_no_text.setText(str(getData[0][0]))
        self.Subject_no_text.setDisabled(True)
        self.Subject_description_text.setText(str(getData[0][1]))


