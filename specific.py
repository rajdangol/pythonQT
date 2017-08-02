"""yo chai home page """
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

		self.stacked_widget = QtGui.QStackedWidget()
		grid.addWidget(self.stacked_widget)

		QtGui.QFont().setPointSize(55)

		pic = QtGui.QLabel()
		pic.setPixmap(QtGui.QPixmap("logo.jpg"))
		grid.addWidget(pic, 0, 1)

		welcome = QtGui.QLabel('\t \t  ' u'\u0928\u092e\u0938\u094d\u0924\u0947' + "	Welcome to the IVR system	\n" + "You are at the main menu\t \t \t" + u'\u0924\u092a\u093e\u0908 \u092e\u0941\u0916\u094d\u092f \u092e\u0947\u0928\u0941\u092e\u093e \u0939\u0941\u0928\u0941\u0939\u0941\u0928\u091b ')
		grid.addWidget(welcome,1,1)

		self.addButtons(grid)

		self.setWindowTitle('IVR Solutions')
		self.setGeometry(350,100,500,500)
		self.show()

	def addButtons(self,grid):	

		speakButton = QtGui.QPushButton("Speak")
		speakButton.setStyleSheet('QPushButton {color: blue;}')
		cancelButton = QtGui.QPushButton("Cancel")
		cancelButton.setStyleSheet('QPushButton {color: red;}')
	
		speakButton.clicked.connect(self.handleButton)
		cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

		grid.addWidget(speakButton,5,1)
		grid.addWidget(cancelButton,6,1)

	
	def handleButton(self):
		sender = self.sender()
		print (sender.text())
		subprocess.call(['python','specific2.py'])			#calls a different script
		
def main():
	app = QtGui.QApplication(sys.argv)
	ex = InitWindow()
	sys.exit(app.exec_())


if __name__=='__main__':
	main()
