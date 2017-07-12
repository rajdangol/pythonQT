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

        first = QtGui.QLabel(u'\u0967' + '  Marketing   ' + u'\u092e\u093e\u0930\u094d\u0915\u0947\u091f\u093f\u0919\u200b' )
        second = QtGui.QLabel(u'\u0968' + ' Customer Support    ' + u'\u0915\u0938\u094d\u091f\u092e\u0930 \u0938\u092a\u094b\u0930\u094d\u091f\u200b')
        third = QtGui.QLabel(u'\u0969' + '  Technical Support   ' + u'\u091f\u0947\u0915\u094d\u0928\u093f\u0915\u0932 \u0938\u092a\u094b\u0930\u094d\u091f')
        back = QtGui.QLabel(u'\u0966' + '   Previous Menu   '+ u'\u092a\u0941\u0930\u093e\u0928\u094b \u092e\u0947\u0928\u0941')           


        grid.addWidget(first,1,0)
        grid.addWidget(second,2,0)
        grid.addWidget(third,3,0)
        grid.addWidget(back,5,0)

        self.addButtons(grid)

        first.mousePressEvent = self.textClicked

        self.setWindowTitle('IVR Solutions')
        self.setGeometry(250,250,500,500)
        self.show()

    def addButtons(self,grid):  

        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.setStyleSheet('QPushButton {color: red;}')
    
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        grid.addWidget(cancelButton,6,0)

    def textClicked(self,event):
        subprocess.call(['python','specific3.py'])          #calls a different script

def main():
    app = QtGui.QApplication(sys.argv)
    ex = InitWindow()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
