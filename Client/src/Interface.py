import sys

from PySide import QtCore
from PySide import QtGui

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.setGeometry(100, 100, 640, 480)
		self.setWindowTitle("Clementine")
		self.setWindowIcon(QtGui.QIcon("../../Games/Harris/res/icons/001-Weapon01.png"))

		self.gamesFrame = GamesFrame(self)
		self.gamesFrame.show()

		self.show()

	def closeEvent(self, event = QtGui.QCloseEvent):
		response = QtGui.QMessageBox.question(self, "Message", "Are you sure you want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if response == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()