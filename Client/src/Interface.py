import sys
from PySide import QtGui

class Interface():
	def __init__(self):
		self.application = QtGui.QApplication(sys.argv)
		self.homeWindow = HomeWindow(self)
		self.gamesWindow = GamesWindow(self)

		self.homeWindow.show()

		sys.exit(self.application.exec_())

	def showHomeWindow(self):
		self.gamesWindow.hide()
		self.homeWindow.show()

	def showGamesWindow(self):
		self.homeWindow.hide()
		self.gamesWindow.show()

class HomeWindow(QtGui.QWidget):
	def __init__(self, parent):
		super(HomeWindow, self).__init__()

		self.gridLayout = QtGui.QGridLayout(self)
		self.gridLayout.setSpacing(10)

		self.homeButton = QtGui.QPushButton(self)
		self.homeButton.setText("Home")

		self.gamesButton = QtGui.QPushButton(self)
		self.gamesButton.setText("Games")
		self.gamesButton.clicked.connect(parent.showGamesWindow)

		self.gridLayout.addWidget(self.homeButton, 1, 1)
		self.gridLayout.addWidget(self.gamesButton, 2, 1)

		self.setLayout(self.gridLayout)

class GamesWindow(QtGui.QWidget):
	def __init__(self, parent):
		super(GamesWindow, self).__init__()

		self.gridLayout = QtGui.QGridLayout(self)
		self.gridLayout.setSpacing(10)

		self.homeButton = QtGui.QPushButton(self)
		self.homeButton.setText("Home")
		self.homeButton.clicked.connect(parent.showHomeWindow)

		self.gamesButton = QtGui.QPushButton(self)
		self.gamesButton.setText("Games")

		self.gridLayout.addWidget(self.homeButton, 1, 1)
		self.gridLayout.addWidget(self.gamesButton, 2, 1)

		self.setLayout(self.gridLayout)

if __name__ == "__main__":
	interface = Interface()