import sys

from PySide import QtCore
from PySide import QtGui

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		menu = self.menuBar()

		fileMenu = menu.addMenu("&File")

		exitAction = QtGui.QAction(QtGui.QIcon("../Games/Harris/res/icons/001-Weapon01.png"), "&Exit", self)
		exitAction.triggered.connect(self.close)

		fileMenu.addAction(exitAction)

		exitButton = QtGui.QPushButton("Exit", self)
		exitButton.clicked.connect(self.close)
		exitButton.resize(exitButton.sizeHint())
		exitButton.move(50, 50)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle("Clementine")
		self.setWindowIcon(QtGui.QIcon("../Games/Harris/res/icons/001-Weapon01.png"))
		self.show()

	def closeEvent(self, event = QtGui.QCloseEvent):
		response = QtGui.QMessageBox.question(self, "Message", "Are you sure you want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if response == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	application = QtGui.QApplication(sys.argv)
	window = Window()
	sys.exit(application.exec_())

if __name__ == '__main__':
	main()