import sys,PySide
from PySide import *

class Clementine(QtGui.QMainWindow):##creates the class clementine
    
    def __init__(self):##creates window 
        super(Clementine, self).__init__()

        self.setGeometry(0,35, 1400, 650)
        self.setWindowTitle('Clementine')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.Profile()##calls definition 
        self.Grouplogo()##calls definition
        self.Profilebuttons()##calls definition
        self.title()##calls definition
        self.highScore1()
        self.highScore2()
        self.highScore3()
        self.gameTiles()
        self.ownedGames()
        self.show()
        
    
    def Profile(self):               
        
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
        
        
    def Profilebuttons(self):

        
        profileButton = QtGui.QPushButton('Messages',self)
        profileButton.setStyleSheet("background-color:#CC0066")
        profileButton.setGeometry(30, 200, 250, 30)
        profileButton.setToolTip('Press to view messages') #this brings up info
        #about button when it is highlighted over, but not clicked

        gamesButton = QtGui.QPushButton('Games',self)
        gamesButton.setStyleSheet("background-color:#CC66CC")
        gamesButton.setGeometry(30, 230, 250, 30)
        gamesButton.setToolTip('Press to view owned games')

        highScoresButton = QtGui.QPushButton('Details',self)
        highScoresButton.setStyleSheet("background-color:#FF6699")
        highScoresButton.setGeometry(30, 260, 250, 30)
        highScoresButton.setToolTip('Press to view high scores')

        chatRoomButton = QtGui.QPushButton('Achievements',self)
        chatRoomButton.setStyleSheet("background-color:#99FFFF")
        chatRoomButton.setGeometry(30, 290, 250, 30)
        chatRoomButton.setToolTip('Press to see achievements')
        

        

        
    def Grouplogo(self):
        pixmap = QtGui.QPixmap("logo.png")
        logoImage = QtGui.QLabel(self)
        logoImage.setGeometry(90, 30, 150, 150)
        logoImage.setPixmap(pixmap)

    def title(self):
        title = QtGui.QLabel("<font color=blue size=30>Profile</font>",self)
        title.setGeometry(350, 0, 800, 40)
        title.setStyleSheet("background-color:#E68B4F")
        title.setAlignment(QtCore.Qt.AlignCenter)
    def ownedGames(self):
        owned = QtGui.QLabel("<font color=grey size=25>Owned Games</font>",self)
        owned.setGeometry(631,45,200,40)
        owned.setStyleSheet("background-color:#FFCC33")
        owned.setAlignment(QtCore.Qt.AlignCenter)
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

        tile1 = QtGui.QPixmap("OusmanGame.jpg")
        tileImage1 = QtGui.QLabel(self)
        tileImage1.setGeometry(300, 50, 320, 400)
        tileImage1.setPixmap(tile1)

        tile2 = QtGui.QPixmap("AlexGame.jpg")
        tileImage2 = QtGui.QLabel(self)
        tileImage2.setGeometry(650, 50, 320, 400)
        tileImage2.setPixmap(tile2)

        tile3 = QtGui.QPixmap("MattGame.jpg")
        tileImage3 = QtGui.QLabel(self)
        tileImage3.setGeometry(1000, 50, 320, 400)
        tileImage3.setPixmap(tile3)
        
        
    def highScore1(self): #animal chase
        high1 = QtGui.QLabel("<font color=black size=5>Animal Chase High Score</font>",self)
        high1.setGeometry(300,420,200,20)
        high1.setStyleSheet("background-color:#9999CC")
        high1.setAlignment(QtCore.Qt.AlignCenter)
        high2 = QtGui.QLabel("<font color=black size=5>1.Harris- 25 points</font>",self)
        high2.setGeometry(300,450,200,20)
        high2.setStyleSheet("background-color:#9999CC")
        high2.setAlignment(QtCore.Qt.AlignCenter)
        high3 = QtGui.QLabel("<font color=black size=5>2.Matt- 20 points</font>",self)
        high3.setGeometry(300,472,200,20)
        high3.setStyleSheet("background-color:#9999CC")
        high3.setAlignment(QtCore.Qt.AlignCenter)
        high4 = QtGui.QLabel("<font color=black size=5>3.Alex- 1 point</font>",self)
        high4.setGeometry(300,494,200,20)
        high4.setStyleSheet("background-color:#9999CC")
        high4.setAlignment(QtCore.Qt.AlignCenter)

    def highScore2(self):#planet eater
        high5 = QtGui.QLabel("<font color=black size=5>Planet Eater High Score</font>",self)
        high5.setGeometry(632,420,200,20)
        high5.setStyleSheet("background-color:#FFCCFF")
        high5.setAlignment(QtCore.Qt.AlignCenter)
        high6 = QtGui.QLabel("<font color=black size=5>1.Ousman- 13 points</font>",self)
        high6.setGeometry(632,450,200,20)
        high6.setStyleSheet("background-color:#FFCCFF")
        high6.setAlignment(QtCore.Qt.AlignCenter)
        high7 = QtGui.QLabel("<font color=black size=5>2.Michael- 12 points</font>",self)
        high7.setGeometry(632,472,200,20)
        high7.setStyleSheet("background-color:#FFCCFF")
        high7.setAlignment(QtCore.Qt.AlignCenter)
        high8 = QtGui.QLabel("<font color=black size=5>3.Matt- 5 points</font>",self)
        high8.setGeometry(632,494,200,20)
        high8.setStyleSheet("background-color:#FFCCFF")
        high8.setAlignment(QtCore.Qt.AlignCenter)

    def highScore3(self):
        high9 = QtGui.QLabel("<font color = black size=5> Target Practice High Score</font>",self)
        high9.setGeometry(1000,420,200,20)
        high9.setStyleSheet("background-color:#00FF66")
        high9.setAlignment(QtCore.Qt.AlignCenter)
        high10= QtGui.QLabel("<font color=black size=5>1.Alex- 17 points</font>",self)
        high10.setGeometry(1000,450,200,20)
        high10.setStyleSheet("background-color:#00FF66")
        high10.setAlignment(QtCore.Qt.AlignCenter)
        high11 = QtGui.QLabel("<font color=black size=5>2.Harris- 12 points</font>",self)
        high11.setGeometry(1000,472,200,20)
        high11.setStyleSheet("background-color:#00FF66")
        high11.setAlignment(QtCore.Qt.AlignCenter)
        high12 = QtGui.QLabel("<font color=black size=5>3.Matt- 4 points</font>",self)
        high12.setGeometry(1000,494,200,20)
        high12.setStyleSheet("background-color:#00FF66")
        high12.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        

    
        
    

 
        
def main():
    
    app = QtGui.QApplication(sys.argv) 
    gui = Clementine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
