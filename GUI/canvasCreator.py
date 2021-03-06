from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MplCanvas(FigureCanvas):
      def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure()
        plt.xlabel('Group')
        plt.ylabel('Scores')
        self.ax = self.fig.add_subplot(111)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)


class MplWidget(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
    # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
    # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
    # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
    # add mpl widget to vertical box
        self.vbl.addWidget(self.canvas)
    # set the layout to th vertical box
        self.setLayout(self.vbl)

