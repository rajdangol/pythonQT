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

        marketing = QtGui.QLabel("You are at Marketing Menu \t" + u'\u0924\u092a\u093e\u0908\u0902 \u092e\u093e\u0930\u094d\u0915\u0947\u091f\u093f\u0919 \u092e\u0947\u0928\u0941\u092e\u093e \u0939\u0941\u0928\u0941\u0939\u0941\u0928\u094d\u091b \n' +
            '-----------------------------------------------------------------------------------------')
        first = QtGui.QLabel(u'\u0967' + ' Voice Message    ' + u'\u092d\u094d\u0935\u093e\u0907\u0938 \u092e\u0947\u0938\u0947\u091c ')
        second  = QtGui.QLabel(u'\u0968' + ' Promotions and Advertisement Manager   ' + u'\u092a\u094d\u0930\u094b\u092e\u094b\u0936\u0928 \u0930 \u0935\u093f\u091c\u094d\u091e\u093e\u092a\u0928 \u092e\u0947\u0928\u0947\u091c\u0930 ')
        third = QtGui.QLabel(u'\u0969' + '  Marketing Director  ' + u'\u092e\u093e\u0930\u094d\u0915\u0947\u091f\u093f\u0919 \u0921\u093f\u0930\u0947\u0915\u094d\u091f\u0930 ')
        
        back = QtGui.QLabel(u'\u0966' + '   Previous Menu   '+ u'\u092a\u0941\u0930\u093e\u0928\u094b \u092e\u0947\u0928\u0941')                     

        grid.addWidget(marketing,1,0)
        grid.addWidget(first,3,0)
        grid.addWidget(second,4,0)
        grid.addWidget(third,5,0)
        grid.addWidget(back,7,0)

        self.addButtons(grid)

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

        grid.addWidget(cancelButton,8,0)

    def conditional(self,a):
        if (a == 0):
            print("menu is to repeated")
        if (a == 1):
            # subprocess.call(['python','specific1.py'])
            print("You can now record your voice message")
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