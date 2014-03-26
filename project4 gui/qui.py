import sys,PySide
from PySide import *

class Clementine(QtGui.QMainWindow):##creates the class clementine
    
    def __init__(self):##creates window 
        super(Clementine, self).__init__()

        self.setGeometry(0,35, 1400, 650)
        self.setWindowTitle('Clementine')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.Menu()##calls definition 
        self.logo()##calls definition
        self.buttons()##calls definition
        self.title()##calls definition
        self.gameTiles()
        self.show()
        
    
    def Menu(self):               
        
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitMessage)
        self.statusBar()

        fileMenu.addAction(exitAction)

        aboutMenu = menubar.addMenu('&Help')

        about = QtGui.QAction(QtGui.QIcon('about.png'), '&About', self)
        about.setShortcut('Ctrl+A')
        about.setStatusTip('About Us')
        about.triggered.connect(self.aboutMessage)
        self.statusBar()

        aboutMenu.addAction(about)
        
        
    def buttons(self):

        
        profileButton = QtGui.QPushButton('Profile',self)
        profileButton.setStyleSheet("background-color:#AAE64F")
        profileButton.setGeometry(30, 200, 250, 30)
        profileButton.setToolTip('Press to access Profile')

        gamesButton = QtGui.QPushButton('Games',self)
        gamesButton.setStyleSheet("background-color:#E64F69")
        gamesButton.setGeometry(30, 230, 250, 30)
        gamesButton.setToolTip('Press to view the store')

        highScoresButton = QtGui.QPushButton('High Scores',self)
        highScoresButton.setStyleSheet("background-color:#4F9BE6")
        highScoresButton.setGeometry(30, 260, 250, 30)
        highScoresButton.setToolTip('Press to view high scores')

        chatRoomButton = QtGui.QPushButton('Chat Room',self)
        chatRoomButton.setStyleSheet("background-color:#E68B4F")
        chatRoomButton.setGeometry(30, 290, 250, 30)
        chatRoomButton.setToolTip('Press to enter Chat')
        

        settingsButton = QtGui.QPushButton('Settings',self)
        settingsButton.setStyleSheet("background-color:#CE12EC")
        settingsButton.setGeometry(30, 320, 250, 30)
        settingsButton.setToolTip('Press to change settings')

        
    def logo(self):
        pixmap = QtGui.QPixmap("logo.png")
        logoImage = QtGui.QLabel(self)
        logoImage.setGeometry(90, 30, 150, 150)
        logoImage.setPixmap(pixmap)

    def title(self):
        title = QtGui.QLabel("<font color=blue size=30>Welcome to Clementine</font>",self)
        title.setGeometry(350, 30, 800, 40)
        title.setStyleSheet("background-color:#E68B4F")
        title.setAlignment(QtCore.Qt.AlignCenter)
    def exitMessage(self):
       exitResponce = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
       if exitResponce == QtGui.QMessageBox.Yes:
           sys.exit()            
       else:
            False        
    def aboutMessage(self):
        aboutMessage = QtGui.QMessageBox.information(self, 'About Us',
            "We are the best team ever!!!")
    def gameTiles(self):

        tile1 = QtGui.QPixmap("pic.jpeg")
        tileImage1 = QtGui.QLabel(self)
        tileImage1.setGeometry(300, 100, 250, 250)
        tileImage1.setPixmap(tile1)

        tile2 = QtGui.QPixmap("gears.jpg")
        tileImage2 = QtGui.QLabel(self)
        tileImage2.setGeometry(500, 100, 250, 250)
        tileImage2.setPixmap(tile2)

        tile3 = QtGui.QPixmap("gta.jpg")
        tileImage3 = QtGui.QLabel(self)
        tileImage3.setGeometry(700, 100, 250, 250)
        tileImage3.setPixmap(tile3)
        
        tile4 = QtGui.QPixmap("cry.jpg")
        tileImage4 = QtGui.QLabel(self)
        tileImage4.setGeometry(900, 100, 250, 250)
        tileImage4.setPixmap(tile4)

        tile5 = QtGui.QPixmap("fifa.jpg")
        tileImage5 = QtGui.QLabel(self)
        tileImage5.setGeometry(1100, 100, 250, 250)
        tileImage5.setPixmap(tile5)


 
        
def main():
    
    app = QtGui.QApplication(sys.argv) 
    gui = Clementine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
