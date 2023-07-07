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
        # Push Button (Start Game) will go to the player menu
        self.pushButton.clicked.connect(self.gotoPlayerMenu)
    
    # Create the widget to go to the Player Menu
    def gotoPlayerMenu(self):
        # Initialize the player men
        player_menu=PlayerMenu()
        widget.addWidget(player_menu)
        # Update the widget menu to point to the player menu
        widget.setCurrentIndex(widget.currentIndex()+1)

# Player Menu
class PlayerMenu(QDialog):
    # Initialize the player menu window
    def __init__(self):
        super(PlayerMenu, self).__init__()
        loadUi("player_menu/player_menu.ui", self)
        # Based on the button push perform certain action
        # Load the data and move to the game board
        self.pushButton.clicked.connect(self.insertData)
        self.pushButton.clicked.connect(self.gotoBoard)
        # Go back to the menu if requested by user
        self.pushButton_2.clicked.connect(self.gotoMenu)
    
    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        main_app=MainWindow()
        widget.addWidget(main_app)
        # Update the widget menu to point to the player menu
        widget.setCurrentIndex(widget.currentIndex()-1)

    # Create the widget to go to forward to the board
    def gotoBoard(self):
        board=Board()
        board.setNames()
        widget.addWidget(board)
        # Update the widget menu to point to board
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        query.bindValue(":player_name", self.lineEdit.text())
        query.exec_()
        query.bindValue(":player_name", self.lineEdit_2.text())
        query.exec_()
        query.bindValue(":player_name", self.lineEdit_3.text())
        query.exec_()
        query.bindValue(":player_name", self.lineEdit_4.text())
        query.exec_()

        # Complete the query and close database
        query.finish()
        create_db.close_database(database)

# Board Menu
class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board/board.ui", self)
        # Go back to the player menu if requested by user
        self.pushButton.clicked.connect(self.gotoPlayerMenu)
    
    # Create the widget to go to back to the player menu
    def gotoPlayerMenu(self):
        player_menu=PlayerMenu()
        widget.addWidget(player_menu)
        widget.setCurrentIndex(widget.currentIndex()-1)

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
        self.textBrowser_1.setText(query.value(1))
        query.next()
        self.textBrowser_2.setText(query.value(1))
        query.next()
        self.textBrowser_3.setText(query.value(1))
        query.next()
        self.textBrowser_4.setText(query.value(1))
        
        query.finish()
        create_db.close_database(database)

# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main_app=MainWindow()
widget.setWindowTitle("TrivialCompute")
widget.addWidget(main_app)
widget.setFixedHeight(900)
widget.setFixedWidth(880)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")