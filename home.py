"""Yo chai home page jasto...first page IVR system ko
esma chai aba options haru hunxa ani tya click garexi siddhai call janxa
ani tespaxi uta bata response aauxa
"""
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

		self.addButtons(grid)

		self.setWindowTitle('IVR Solutions')
		self.setGeometry(250,250,300,300)
		self.show()

	def addButtons(self,grid):
		
		names = ['Emergency','NTC/Ncell','Banks','ISP',
				'Shopping Centres','Others'
				]
		positions = [(i,j) for i in range(3) for j in range(3)]

		for position, name in zip(positions, names):

			if name == '':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button, *position)
		

		keyButton = QtGui.QPushButton("Keypad")
		keyButton.setStyleSheet('QPushButton {color: green;}')
		cancelButton = QtGui.QPushButton("Cancel")
		cancelButton.setStyleSheet('QPushButton {color: red;}')
	
		keyButton.clicked.connect(self.handleButton)
		cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

		grid.addWidget(keyButton,4,0)
		grid.addWidget(cancelButton,4,2)

	
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