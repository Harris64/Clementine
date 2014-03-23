import sys

from PySide import QtGui
from Interface import Window

def main():
	application = QtGui.QApplication(sys.argv)
	window = Window()
	sys.exit(application.exec_())

if __name__ == '__main__':
	main()