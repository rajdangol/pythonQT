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
		
		self.lcdDisplay = QtGui.QLCDNumber(self)
		self.lcdDisplay.display('0')

		grid.addWidget(self.lcdDisplay,1,0,1,5)

		names = ['1', '2','3',
				'4','5','6',
				'7','8','9',
				'*','0','#',
				]
		positions = [(i,j) for i in range(3,7) for j in range(3)]

		for position, name in zip(positions, names):

			if name == '':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button, *position)
			button.clicked.connect(self.buttonClicked)


		callButton = QtGui.QPushButton("Call")
		callButton.setStyleSheet('QPushButton {color: green;}')
		cancelButton = QtGui.QPushButton("Cancel")
		cancelButton.setStyleSheet('QPushButton {color: red;}')
	
		callButton.clicked.connect(self.handleButton)
		cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

		grid.addWidget(callButton,4,4)
		grid.addWidget(cancelButton,5,4)

	s = ''
	def buttonClicked(self):
		sender = self.sender()
		
		msg = sender.text()
		a = str(msg)
		self.s = self.s + a
		print self.s
		
		self.lcdDisplay.display(self.s)

	def handleButton(self):
		sender = self.sender()
		print (sender.text())
		subprocess.call(['python','hello.py'])			#calls a different script


def main():
	app = QtGui.QApplication(sys.argv)
	ex = InitWindow()
	sys.exit(app.exec_())


if __name__=='__main__':
	main()
