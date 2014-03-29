import sys
from PySide import QtGui, QtCore

class Chat(QtGui.QWidget):
    
    def __init__(self):
        super(Chat, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)
        
        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Chat')
        self.show()
        
    def onChanged(self, text):
        
        self.lbl.setText(text)
        self.lbl.adjustSize()        
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Chat()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
