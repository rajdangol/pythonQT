"""yo chai home page ma click garexi aauxa...ya chai aba specific functions haru
jastai bank ko lagi matra milne functions haru tala lekhya hunxa 
jasle garda repsonse dina lai sajilo hunxa
tya edit box ko sato chai euta figure rakhne tyo sound ko waveform jasto"""

import sys,os
import subprocess
from PyQt4 import QtGui, QtCore

class InitWindow(QtGui.QWidget):
    def __init__(self):
        super(InitWindow, self).__init__()
        self.initUI()

    def initUI(self):

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        pic = QtGui.QLabel()
        pic.setPixmap(QtGui.QPixmap("logo.jpg"))
        grid.addWidget(pic, 0, 0)

        first = QtGui.QLabel(u'\u0967' + '  Marketing Director')
        second  = QtGui.QLabel(u'\u0968' + ' Promotions and Advertisement Manager')
        third = QtGui.QLabel(u'\u0969' + ' Voice Message')
        
        back = QtGui.QLabel(u'\u0966' + '  Back')           


        grid.addWidget(first,1,0)
        grid.addWidget(second,2,0)
        grid.addWidget(third,3,0)
        grid.addWidget(back,5,0)

        self.addButtons(grid)

        self.setWindowTitle('IVR Solutions')
        self.setGeometry(250,250,500,500)
        self.show()

    def addButtons(self,grid):  

        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.setStyleSheet('QPushButton {color: red;}')
    
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        grid.addWidget(cancelButton,6,0)

    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = InitWindow()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()