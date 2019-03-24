from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import GUI.subjectUIGUI

class subjects(QDialog, GUI.subjectUIGUI.Ui_Dialog):

    def __init__(self):
        super(subjects, self).__init__()

        self.setupUi(self)
