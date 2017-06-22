"""yo chai home page ma click garexi aauxa...ya chai aba specific functions haru
jastai bank ko lagi matra milne functions haru tala lekhya hunxa 
jasle garda repsonse dina lai sajilo hunxa
tya edit box ko sato chai euta figure rakhne tyo sound ko waveform jasto"""

import sys
import subprocess
from PyQt4 import QtGui, QtCore

class InitWindow(QtGui.QWidget):
	def __init__(self):
		super(InitWindow, self).__init__()
		self.initUI()

	def initUI(self):
	
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		first = QtGui.QLabel('1. Customer Services')
		second = QtGui.QLabel('2. Sales and Marketing')
		third = QtGui.QLabel('3. Tech Support')
		forth = QtGui.QLabel('4. Reception')

		edit = QtGui.QLineEdit()

		grid.addWidget(edit,0,0,1,4)

		grid.addWidget(first,1,0)
		grid.addWidget(second,2,0)
		grid.addWidget(third,3,0)
		grid.addWidget(forth,4,0)

		self.addButtons(grid)

		self.setWindowTitle('IVR Solutions')
		self.setGeometry(250,250,300,300)
		self.show()

	def addButtons(self,grid):	

		keyButton = QtGui.QPushButton("Keypad")
		keyButton.setStyleSheet('QPushButton {color: green;}')
		speakButton = QtGui.QPushButton("Speak")
		speakButton.setStyleSheet('QPushButton {color: blue;}')
		cancelButton = QtGui.QPushButton("Cancel")
		cancelButton.setStyleSheet('QPushButton {color: red;}')
	
		keyButton.clicked.connect(self.handleButton)
		cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

		grid.addWidget(keyButton,5,0)
		grid.addWidget(speakButton,5,3)
		grid.addWidget(cancelButton,6,1)

	
	def handleButton(self):
		sender = self.sender()
		print (sender.text())
		subprocess.call(['python','first.py'])			#calls a different script


def main():
	app = QtGui.QApplication(sys.argv)
	ex = InitWindow()
	sys.exit(app.exec_())


if __name__=='__main__':
	main()