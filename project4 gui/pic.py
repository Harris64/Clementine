import sys
from PySide import QtCore
from PySide import QtGui
 
app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
 
label = QtGui.QLabel(window)
pixmap = QtGui.QPixmap('pic.jpg')
label.setPixmap(pixmap)
label.resize(pixmap.size())
 
window.setGeometry(100, 100, 900, 700)
window.show()
 
sys.exit(app.exec_())
