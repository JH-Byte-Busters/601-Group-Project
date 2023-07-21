import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox
import create_db
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon

# Main Window Menu
class MainWindow(QDialog):
    # Initialize the main window
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window/main_window.ui", self)
        # Push Button (Start Game) will go to the user login menu
        self.btn_startGame.clicked.connect(self.gotoPlayerMenu)
        self.btn_catQSetup.clicked.connect(self.gotoCategoryMenu)
    
    # Go to the widget to go to the Player Menu
    def gotoPlayerMenu(self):
        # Update the widget menu to point to the Player menu
        widget.setCurrentIndex(widget.currentIndex()+2)
    
    # Go to the widget to go to the Player Menu
    def gotoCategoryMenu(self):
        # Update the widget menu to point to the Player menu
        widget.setCurrentIndex(widget.currentIndex()+3)

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

        # Setting username and password to the input from the user
        username = self.line_username.text()
        password = self.line_password.text()

        # Attach to the correct database by decalring vars
        database.setDatabaseName("trivial_pursuit.db")

        if not database.open():
            print("Could not open the database!")
            return False

        query = QSqlQuery()
        query.prepare("SELECT * FROM Users WHERE username = ? AND password = ?")
        query.addBindValue(username)
        query.addBindValue(password)

        if query.exec():
            if query.next():
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setWindowTitle("Authentication Failed")
                message_box.setText("Invalid username or password.")
                message_box.exec_()

        else:
            print("Error occurred during authentication.")

    # Create the widget to go to the Create account Menu
    def gotoCreateAccount(self):
        # Update the widget menu to point to the Create account menu
        widget.setCurrentIndex(widget.currentIndex()+2)

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

            database.setDatabaseName("trivial_pursuit.db")

            if not database.open():
                print("Could not open the database!")
                return False

            query = QSqlQuery()
            query.prepare("INSERT INTO Users (user_id, username, password, email, created_at, position) "
                            "VALUES (NULL, :username, :password, :email, CURRENT_TIMESTAMP, :position)")
            query.bindValue(":username",  self.line_username.text())
            # Should Probably change this name in the UI tool to not conflict with login
            query.bindValue(":password", self.line_password.text())
            query.bindValue(":email", self.line_email.text())
            query.bindValue(":position", "pushButton_46")  # Default position

            if query.exec():
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Information)
                message_box.setWindowTitle("User Create")
                message_box.setText("User sucessfully created. Please Login")
                message_box.exec_()
            else:
                print("Error occurred while inserting user data.")

            widget.setCurrentIndex(widget.currentIndex()-2)

    # Create the widget to go to back to the main menu
    def gotoUserLogin(self):
        # Update the widget menu to point to the player menu
        widget.setCurrentIndex(widget.currentIndex()-2)

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
        global player_names
        player_names = [
            self.line_playerName1.text(),
            self.line_playerName2.text(),
            self.line_playerName3.text(),
            self.line_playerName4.text()
        ]

# Category Menu
class CategoryMenu(QDialog):
    # Initialize the player menu window
    def __init__(self):
        super(CategoryMenu, self).__init__()
        loadUi("category_question/category_question.ui", self)
        # Based on the button push perform certain action
        # Load the data and move to the question menu
        self.btn_playGame.clicked.connect(self.insertData)
        # self.btn_playGame.clicked.connect(self.gotoBoard)
        # Go back to the menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMenu)

    # Create the widget to go to forward to the board
    '''def gotoBoard(self):
        # Initialization of board widget must be done here 
        # to ensure that the board names are properly pulled from
        # the database
        board=Board()
        board.setNames()
        widget.setFixedHeight(980)
        widget.setFixedWidth(1890)
        widget.addWidget(board)
        # Update the widget menu to point to board
        widget.setCurrentIndex(widget.currentIndex()+1)'''
    
    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentIndex(widget.currentIndex()-3)

    # Work with the database to add in the written data
    # once the button "Insert Data" is pressed
    def insertData(self):
        # Create the database 
        database = create_db.create_database()
    
        if not database.isOpen():
            print('Connection error occurred.')
        
        # Query the database to load in the text
        # within the user text boxes
        query = QSqlQuery("SELECT * FROM Category")
        query.prepare("INSERT INTO Category (category_name) "
              "VALUES (:category_name)")
        query.bindValue(":category_name", self.line_catHead1.text())
        query.exec_()
        query.bindValue(":category_name", self.line_catHead2.text())
        query.exec_()
        query.bindValue(":category_name", self.line_catHead3.text())
        query.exec_()
        query.bindValue(":category_name", self.line_catHead4.text())
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

        # Directional button connects
        self.btn_up.clicked.connect(self.move_up)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_down.clicked.connect(self.move_down)
        self.btn_left.clicked.connect(self.move_left)

        # Navigation global variables:
        self.cells = []
        self.pointer = 41
        self.category = "NONE"

        # Create a 2D list to store the button objects
        buttons = [
            [self.btn_1,  self.btn_2,  self.btn_3,  self.btn_4,  self.btn_5,  self.btn_6,  self.btn_7,  self.btn_8,  self.btn_9],
            [self.btn_10, self.btn_14, self.btn_18, self.btn_19, self.btn_23, self.btn_27, self.btn_28, self.btn_32, self.btn_36],
            [self.btn_37, self.btn_38, self.btn_39, self.btn_40, self.btn_41, self.btn_42, self.btn_43, self.btn_44, self.btn_45],
            [self.btn_46, self.btn_50, self.btn_54, self.btn_55, self.btn_59, self.btn_63, self.btn_64, self.btn_68, self.btn_72],
            [self.btn_73, self.btn_74, self.btn_75, self.btn_76, self.btn_77, self.btn_78, self.btn_79, self.btn_80, self.btn_81]
        ]

        # Flatten the 2D list and append the button objects to the cells list
        self.cells = [button for row in buttons for button in row]
    
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

        self.txt_playerName1.setText(player_names[0])
        self.txt_playerName2.setText(player_names[1])
        self.txt_playerName3.setText(player_names[2])
        self.txt_playerName4.setText(player_names[3])

    ######################
    # Navigation methods:
    ######################
    def move_left(self):
        left_border = [0, 9, 18, 27, 36, 45, 54, 63, 72] # Board left border cells
        self.pointer = self.pointer - 1
        self.dial_player1.move(self.dial_player1.x() - 95, self.dial_player1.y())
        allowed = True
        # Enforce border limit:
        for cell in left_border:
            if self.pointer == cell:
                allowed = False
                break
        if allowed and not self.getCellObject():
            allowed = False

        if not allowed:
            self.pointer = self.pointer + 1
            self.dial_player1.move(self.dial_player1.x() + 95, self.dial_player1.y())
        print(self.pointer)

    def move_right(self):
        left_border = [10, 19, 28, 37, 46, 55, 64, 73, 82] # Board right border cells
        self.pointer = self.pointer + 1
        self.dial_player1.move(self.dial_player1.x() + 95, self.dial_player1.y())
        allowed = True
        # Enforce border limit:
        for cell in left_border:
            if self.pointer == cell:
                allowed = False
                break
        if allowed and not self.getCellObject():
            allowed = False

        if not allowed:
            self.pointer = self.pointer - 1
            self.dial_player1.move(self.dial_player1.x() - 95, self.dial_player1.y())
        print(self.pointer)

    def move_up(self):
        self.pointer = self.pointer - 9
        self.dial_player1.move(self.dial_player1.x(), self.dial_player1.y() - 100)
        allowed = True
        # Enforce border limit:
        if self.pointer < 0:
            allowed = False
        else:
            if not self.getCellObject():
                allowed = False

        if not allowed:
            self.pointer = self.pointer + 9
            self.dial_player1.move(self.dial_player1.x(), self.dial_player1.y() + 100)
        print(self.pointer)

    def move_down(self):
        self.pointer = self.pointer + 9
        self.dial_player1.move(self.dial_player1.x(), self.dial_player1.y() + 100)
        allowed = True
        # Enforce border limit:
        if self.pointer < 0:
            allowed = False
        else:
            if not self.getCellObject():
                allowed = False

        if not allowed:
            self.pointer = self.pointer - 9
            self.dial_player1.move(self.dial_player1.x(), self.dial_player1.y() - 100)
        print(self.pointer)

    def getCellObject(self):
        for obj in self.cells:
            if str(self.pointer) == (obj.objectName().split("_")[1]):
                return True
        return False

# main
if __name__ == '__main__':
    database = QSqlDatabase.addDatabase("QSQLITE")
    app = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    user_login=UserLogin()
    create_acct=CreateAccount()
    main_app=MainWindow()
    player_menu=PlayerMenu()
    category_menu=CategoryMenu()
    widget.setWindowTitle("TrivialCompute")
    widget.addWidget(user_login)
    widget.addWidget(main_app)
    widget.addWidget(create_acct)
    widget.addWidget(player_menu)
#    widget.addWidget(category_menu)
    widget.setFixedHeight(900)
    widget.setFixedWidth(880)
    widget.show()
    app.exec_()