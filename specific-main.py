import sys,os
import subprocess
from PyQt4 import QtGui, QtCore
from time import sleep

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
        second = QtGui.QLabel(u'\u0968' + ' Customer Support    ' + u'\u0915\u0938\u094d\u091f\u092e\u0930 \u0938\u0939\u093e\u092f\u0924\u093e')
        third = QtGui.QLabel(u'\u0969' + '  Technical Support   ' + u'\u091f\u0947\u0915\u094d\u0928\u093f\u0915\u0932 \u0938\u0939\u093e\u092f\u0924\u093e')
        back = QtGui.QLabel(u'\u0966' + '   Repeat Menu   '+ u'\u092e\u0947\u0928\u0941 \u0926\u094b\u0939\u094b\u0930\u094d\u200d\u092f\u093e\u0909\u0928')           

        grid.addWidget(first,1,0)
        grid.addWidget(second,2,0)
        grid.addWidget(third,3,0)
        grid.addWidget(back,5,0)

        self.addButtons(grid)

        # first.mousePressEvent = self.textClicked

        
        
        self.setWindowTitle('IVR Solutions')
        self.setGeometry(350,100,500,500)
        self.show()

        a = 1;
        print("What is the choice?")
        a = input()
        self.conditional(a)

    def addButtons(self,grid):  

        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.setStyleSheet('QPushButton {color: red;}')
    
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        grid.addWidget(cancelButton,6,0)

    def textClicked(self,event):
        subprocess.call(['python','specific3.py'])          #calls a different script

    def conditional(self,a):
        if (a == 0):
            print("menu is to repeated")
        if (a == 1):
        	subprocess.call(['python','specific1.py'])
        if (a == 2):
            print("not made right now")
            # subprocess.call(['python','specific2.py'])
        if (a == 3):
            print("not made right now")
            # subprocess.call(['python','specific3.py'])



def main():
    app = QtGui.QApplication(sys.argv)
    ex = InitWindow()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()
