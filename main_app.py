import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import create_db
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Main Window Menu
class MainWindow(QDialog):
    # Initialize the main window
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window/main_window.ui", self)
        # Push Button (Start Game) will go to the user login menu
        self.btn_startGame.clicked.connect(self.gotoPlayerMenu)
    
    # Create the widget to go to the Player Menu
    def gotoPlayerMenu(self):
        # Update the widget menu to point to the Player menu
        widget.setCurrentIndex(widget.currentIndex()+2)

class UserLogin(QDialog):
    # Initialize the main window
    def __init__(self):
        super(UserLogin, self).__init__()
        loadUi("login/user_login.ui", self)
        # Go to Main Menu
        self.btn_login.clicked.connect(self.gotoMenu)
        # Push Button (Create Account) will go to the account creation menu
        self.btn_createAct.clicked.connect(self.gotoCreateAccount)

    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Create the widget to go to the Create account Menu
    def gotoCreateAccount(self):
        # Update the widget menu to point to the Create account menu
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAccount(QDialog):
    # Initialize the main window
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("login/user_create.ui", self)
        # Push Button (Start Game) will go to the player menu
        self.btn_playGame.clicked.connect(self.gotoPlayerMenu)
        # Go back to Main Menu
        self.btn_backToMenu.clicked.connect(self.gotoUserLogin)
    
    # Create the widget to go to the Player Menu
    def gotoPlayerMenu(self):
        # Update the widget menu to point to the player menu
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Create the widget to go to back to the main menu
    def gotoUserLogin(self):
        # Update the widget menu to point to the player menu
        widget.setCurrentIndex(widget.currentIndex()-1)

# Player Menu
class PlayerMenu(QDialog):
    # Initialize the player menu window
    def __init__(self):
        super(PlayerMenu, self).__init__()
        loadUi("player_menu/player_menu.ui", self)
        # Based on the button push perform certain action
        # Load the data and move to the game board
        self.btn_playGame.clicked.connect(self.insertData)
        self.btn_playGame.clicked.connect(self.gotoBoard)
        # Go back to the menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMenu)

    # Create the widget to go to forward to the board
    def gotoBoard(self):
        # Initialization of board widget must be done here 
        # to ensure that the board names are properly pulled from
        # the database
        board=Board()
        board.setNames()
        widget.setFixedHeight(980)
        widget.setFixedWidth(1890)
        widget.addWidget(board)
        # Update the widget menu to point to board
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentIndex(widget.currentIndex()-2)

    # Work with the database to add in the written data
    # once the button "Insert Data" is pressed
    def insertData(self):
        # Create the database 
        database = create_db.create_database()
    
        if not database.isOpen():
            print('Connection error occurred.')
        
        # Query the database to load in the text
        # within the user text boxes
        query = QSqlQuery("SELECT * FROM Player")
        query.prepare("INSERT INTO Player (player_name) "
              "VALUES (:player_name)")
        query.bindValue(":player_name", self.line_playerName1.text())
        query.exec_()
        query.bindValue(":player_name", self.line_playerName2.text())
        query.exec_()
        query.bindValue(":player_name", self.line_playerName3.text())
        query.exec_()
        query.bindValue(":player_name", self.line_playerName4.text())
        query.exec_()

        # Complete the query and close database
        query.finish()
        create_db.close_database(database)

# Board Menu
class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board/board.ui", self)
        # Go back to the main menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMainMenu)
    
    # Create the widget to go to back to the main menu
    def gotoMainMenu(self):
        widget.setFixedHeight(900)
        widget.setFixedWidth(880)
        widget.setCurrentIndex(widget.currentIndex()-3)

    # In the board make sure to load up the player names
    # properly to set each text box
    def setNames(self):
        # TODO: Find a way to properly open/close database
        # currently running into some errors with this 
        # as a double connection
        database = QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('trivial_pursuit.db')
        database.open()
    
        if not database.isOpen():
            print('Connection error occurred.')
        
        # Query the database to set the text fields
        query = QSqlQuery("SELECT * FROM Player")

        query.first()
        self.txt_playerName1.setText(query.value(1))
        query.next()
        self.txt_playerName2.setText(query.value(1))
        query.next()
        self.txt_playerName3.setText(query.value(1))
        query.next()
        self.txt_playerName4.setText(query.value(1))
        
        query.finish()
        create_db.close_database(database)

# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
user_login=UserLogin()
create_acct=CreateAccount()
main_app=MainWindow()
player_menu=PlayerMenu()
widget.setWindowTitle("TrivialCompute")
widget.addWidget(user_login)
widget.addWidget(main_app)
widget.addWidget(create_acct)
widget.addWidget(player_menu)
widget.setFixedHeight(900)
widget.setFixedWidth(880)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")