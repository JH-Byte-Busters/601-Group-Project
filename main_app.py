import sys
import os
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox, QFileDialog,QLabel
import create_db
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
import subprocess
import threading

# Main Window Menu
class MainWindow(QDialog):
    # Initialize the main window
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window/main_window.ui", self)
        # Push Button (Start Game) will go to the player menu
        self.btn_startGame.clicked.connect(self.gotoPlayerMenu)
        self.btn_catQSetup.clicked.connect(self.gotoCategoryMenu)

    # Go to the widget to go to the Player Menu
    def gotoPlayerMenu(self):
        # Update the widget menu to point to the Player menu
        widget.setCurrentWidget(player_menu)

    # Go to the widget to go to the Category Menu
    def gotoCategoryMenu(self):
        # Update the widget menu to point to the Category menu
        widget.setCurrentWidget(category_menu)

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
        # Setting username and password to the input from the user
        username = self.line_username.text()
        password = self.line_password.text()

        # Attach to the correct database by declaring vars
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
                # Update the widget menu to point to the main menu
                widget.setCurrentWidget(main_app)
            else:
                # If error during login post warning message
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
        widget.setCurrentWidget(create_acct)

class CreateAccount(QDialog):
    # Initialize the main window
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi("login/user_create.ui", self)
        # Create user will create a user and go back to login menu
        self.btn_playGame.clicked.connect(self.createUser)
        # Go back to Main User Login Menu
        self.btn_backToMenu.clicked.connect(self.gotoUserLogin)

    # Create the widget to go to the Player Menu
    def createUser(self):
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
        query.bindValue(":position", "pushButton_41")  # Default position

        if query.exec():
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("User Create")
            message_box.setText("User successfully created. Please Login")
            message_box.exec_()
        else:
            print("Error occurred while inserting user data.")

        widget.setCurrentWidget(user_login)

    # Create the widget to go to back to the user login
    def gotoUserLogin(self):
        # Update the widget menu to point to the user login
        widget.setCurrentWidget(user_login)

# Player Menu
class PlayerMenu(QDialog):
    # Initialize the player menu window
    def __init__(self):
        super(PlayerMenu, self).__init__()
        loadUi("player_menu/player_menu.ui", self)
        # Based on the button push perform certain action
        # Load the data and move to the game board
        self.btn_playGame.clicked.connect(self.insertData)
        # Go back to the menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMenu)

    # Create the widget to go to forward to the board
    def gotoBoard(self):
        # Initialization of board widget must be done here
        # to ensure that the board names are properly pulled from
        # the database
        board=Board()
        board.setNames()
        widget.setFixedHeight(950)
        widget.setFixedWidth(1700)
        widget.addWidget(board)
        # Update the widget menu to point to board
        widget.setCurrentWidget(board)

    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentWidget(main_app)

    # Work with the database to add in the written data
    # once the button "Insert Data" is pressed
    def insertData(self):
        # Open database to load player names
        database.setDatabaseName('trivial_pursuit.db')

        if not database.open():
            print("Could not open the database!")
            return False

        # Prepare the values to be written
        values = [self.line_playerName1.text(), self.line_playerName2.text(),
                  self.line_playerName3.text(), self.line_playerName4.text()]
        
        # Check if all text fields are empty
        all_empty = all(value.strip() == "" for value in values)

        if all_empty:
            # If error during login post warning message
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("No Players Entered")
            message_box.setText("Please enter at least one player name.")
            message_box.exec_()
        else:
            # Check if there are at least four rows in the table
            query = QSqlQuery("SELECT COUNT(*) FROM Player")
            query.first()
            row_count = query.value(0)

            # Use the appropriate SQL statement based on the number of existing rows
            if row_count >= 4:
                # If there are four or more rows, update the first four rows with new data
                for i, value in enumerate(values, start=1):
                    query.prepare("UPDATE Player SET player_name = :player_name WHERE user_id = :user_id")
                    query.bindValue(":player_name", value)
                    query.bindValue(":user_id", i)
                    query.exec_()
            else:
                # If there are less than four rows, insert new rows
                query.prepare("INSERT INTO Player (player_name) VALUES (:player_name)")
                for value in values:
                    query.bindValue(":player_name", value)
                    query.exec_()
                        
            self.gotoBoard()

# Category Menu
class CategoryMenu(QDialog):
    # Initialize the category menu window
    def __init__(self):
        super(CategoryMenu, self).__init__()
        loadUi("category_question/category_question.ui", self)
        # Based on the button push perform certain action
        # Load the data and move to the question menu
        self.btn_questionSetup.clicked.connect(self.insertData)
        # Go back to the menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMenu)

    # Create the widget to go to forward to the question menu
    def gotoQuestions(self):
        question_menu=QuestionMenu()
        question_menu.setCategories()
        widget.addWidget(question_menu)
        # Update the widget menu to point to question menu
        widget.setCurrentWidget(question_menu)

    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentWidget(main_app)

    # Work with the database to add in the written data
    # once the button "Insert Data" is pressed
    def insertData(self):
        # Attach to the correct database by declaring vars
        database.setDatabaseName("trivial_pursuit.db")

        if not database.open():
            print("Could not open the database!")
            return False

        # Prepare the values to be written
        values = [self.line_catHead1.text(), self.line_catHead2.text(),
                  self.line_catHead3.text(), self.line_catHead4.text()]
        
        # Check if all text fields are empty
        all_empty = all(value.strip() == "" for value in values)

        if all_empty:
            # If error during login post warning message
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("No Categories Entered")
            message_box.setText("Please enter four category names.")
            message_box.exec_()
        else:
            # Check if there are at least four rows in the table
            query = QSqlQuery("SELECT COUNT(*) FROM Category")
            query.first()
            row_count = query.value(0)

            # Use the appropriate SQL statement based on the number of existing rows
            if row_count >= 4:
                # If there are four or more rows, update the first four rows with new data
                for i, value in enumerate(values, start=1):
                    print(i)
                    query.prepare("UPDATE Category SET category_name = :category_name WHERE user_id = :user_id")
                    query.bindValue(":category_name", value)
                    query.bindValue(":user_id", i)
                    query.exec_()
            else:
                # If there are less than four rows, insert new rows
                query.prepare("INSERT INTO Category (category_name) VALUES (:category_name)")
                for value in values:
                    query.bindValue(":category_name", value)
                    query.exec_()
                        
            self.gotoQuestions()

# Question Menu
class QuestionMenu(QDialog):
    # Initialize the question menu window
    def __init__(self):
        super(QuestionMenu, self).__init__()
        loadUi("category_question/question_menu.ui", self)
        # Based on the button push perform certain action
        # Load the data
        self.btn_loadQuestions.clicked.connect(self.insertData)
        # Go back to the menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMenu)
        # When the combo box changes clear all the question fields
        self.comboBox_category.currentIndexChanged.connect(self.clearQandA)

        # Link all load file buttons for questions
        self.buttons = []
        for i in range(1, 12):
            exec(f"self.btn_load{i}.clicked.connect(self.openFile)")
            self.buttons.append(f"self.btn_load{i}")

    def openFile(self):
        # Get the sender (button) that triggered the signal
        sender_btn = self.sender()
        sender_btn_name = "self." + sender_btn.objectName()

        # Open File Dialog
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "JPEG (*.jpg;*.jpeg;*.jpe;*.jiff);;PNG (*.png);;MP4 (*.mp4);;MOV (*.mov);;MP3 (*.mp3)")

        # Output filename to line edit field
        if fname:
            line_edits = [self.line_ques1, self.line_ques2, self.line_ques3, self.line_ques4, self.line_ques5,
                          self.line_ques6, self.line_ques7, self.line_ques8, self.line_ques9, self.line_ques10,
                          self.line_ques11]

            for i, btn_name in enumerate(["self.btn_load1", "self.btn_load2", "self.btn_load3", "self.btn_load4", "self.btn_load5",
                                          "self.btn_load6", "self.btn_load7", "self.btn_load8", "self.btn_load9", "self.btn_load10",
                                          "self.btn_load11"]):
                if sender_btn_name == btn_name:
                    line_edits[i].setText(fname[0])
                    break

    def setCategories(self):
        # Open database
        database.setDatabaseName('trivial_pursuit.db')

        if not database.open():
            print("Could not open the database!")
            return False

        # Query the database to retrieve the first four rows from the "Category" table
        query = QSqlQuery("SELECT * FROM Category LIMIT 4")

        # Set the text fields for the combobox
        row_index = 0
        while query.next():
            self.comboBox_category.setItemText(row_index, query.value(1))
            row_index += 1

    def clearQandA(self):
        for i in range(1, 12):
            line_edit_question_name = f"self.line_ques{i}"
            line_edit_answer_name = f"self.line_answ{i}"

            # Using exec() with precaution
            try:
                exec(f"{line_edit_question_name}.clear()")
                exec(f"{line_edit_answer_name}.clear()")
            except AttributeError:
                print("Line edit box not found:", line_edit_question_name, line_edit_answer_name)

    # Create the widget to go to back to the main menu
    def gotoMenu(self):
        # Update the widget menu to point to the main menu
        widget.setCurrentWidget(main_app)

    def insertData(self):
        # Sample data for multiple questions
        questions_data = [
            # ("Category", "Question Text", "Correct Answer", "Incorrect Answers (comma-separated)", "Difficulty"),
            # Ex. ("Geography", "What is the capital of France?", "Paris", "London, Berlin, Rome", "Easy"),
            (self.comboBox_category.currentText(), self.line_ques1.text(), self.line_answ1.text()),
            (self.comboBox_category.currentText(), self.line_ques2.text(), self.line_answ2.text()),
            (self.comboBox_category.currentText(), self.line_ques3.text(), self.line_answ3.text()),
            (self.comboBox_category.currentText(), self.line_ques4.text(), self.line_answ4.text()),
            (self.comboBox_category.currentText(), self.line_ques5.text(), self.line_answ5.text()),
            (self.comboBox_category.currentText(), self.line_ques6.text(), self.line_answ6.text()),
            (self.comboBox_category.currentText(), self.line_ques7.text(), self.line_answ7.text()),
            (self.comboBox_category.currentText(), self.line_ques8.text(), self.line_answ8.text()),
            (self.comboBox_category.currentText(), self.line_ques9.text(), self.line_answ9.text()),
            (self.comboBox_category.currentText(), self.line_ques10.text(), self.line_answ10.text()),
            (self.comboBox_category.currentText(), self.line_ques11.text(), self.line_answ11.text()),
        ]

        # Loop through the questions data and add each question to the database
        for question_data in questions_data:
            self.add_question_to_database(*question_data)

    # Work with the database to add in the written data
    # once the button "Insert Data" is pressed
    def add_question_to_database(self, category, question_text, correct_answer):
        # Attach to the correct database by declaring vars
        database.setDatabaseName("trivial_pursuit.db")

        if not database.open():
            print("Could not open the database!")
            return False

        # Prepare the SQL query to insert the question into the table
        query = QSqlQuery()
        query.prepare("INSERT INTO Questions (category, question_text, correct_answer) "
                    "VALUES (?, ?, ?)")

        # Bind the values to the placeholders in the query
        query.addBindValue(category)
        query.addBindValue(question_text)
        query.addBindValue(correct_answer)

        # Execute the query
        if not query.exec_():
            print("Error:", query.lastError().text())
        else:
            print("Question added successfully.")

        # Close the database connection
        database.close()

# Board Menu
class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board/board.ui", self)

        # current player
        self.current_player = "player1"

        # Open database
        database.setDatabaseName('trivial_pursuit.db')

        if not database.open():
            print("Could not open the database!")
            return False

        # Query the database to retrieve the first row from the "Player" table
        query = QSqlQuery("SELECT * FROM Player LIMIT 1")
        query.next()
        self.txt_currentPlayer.setText(query.value(1))
        self.txt_currentPlayer.setAlignment(QtCore.Qt.AlignCenter)

        # Go back to the main menu if requested by user
        self.btn_backToMenu.clicked.connect(self.gotoMainMenu)

        # Die image on load-up
        image = QPixmap("board/dice-1.png")
        self.die_image.setPixmap(image)
        # Prompt question upon "OK" move
        self.btn_ok.clicked.connect(self.confirmMove)
        self.btn_ok.clicked.connect(self.promptQuestion)
        # Switch turns when incorrect answers
        self.btn_incorrectAnsw.clicked.connect(self.changePlayer)
        # Check location when correct
        self.btn_correctAnsw.clicked.connect(self.checkHQButton)

        # Directional button connects
        self.btn_up.clicked.connect(self.move_up)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_down.clicked.connect(self.move_down)
        self.btn_left.clicked.connect(self.move_left)

        #roll dice connnect
        self.btn_rollDie.clicked.connect(self.rolltheDice)

        # Navigation global variables:
        self.cells = []

        self.pointer_player1 = 41
        self.pointer_player2 = 41
        self.pointer_player3 = 41
        self.pointer_player4 = 41
        
        self.player_active = [0,0,0,0] 
        
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

        # Instructions
        self.current_instr = 'Roll Die'

        # Set current instruction name in text box
        self.txt_currentInstruct.setText(self.current_instr)
        self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    # Create the widget to go to back to the main menu
    def gotoMainMenu(self):
        widget.setFixedHeight(900)
        widget.setFixedWidth(880)
        widget.setCurrentWidget(main_app)

    # In the board make sure to load up the player and category names
    # properly to set each text box
    def setNames(self):
        # Query the database to retrieve the first four rows from the "Player" table
        query = QSqlQuery("SELECT * FROM Player LIMIT 4")

        # Set the text fields for the player names
        player_num = 1
        while query.next():
            player_name = query.value(1)
            if player_name is not None and str(player_name).strip() != "":
                self.player_active[player_num - 1] = 1           
            exec(f"self.txt_playerName{player_num}.setText('{str(player_name)}')")
            exec(f"self.txt_playerName{player_num}.setAlignment(QtCore.Qt.AlignCenter)")
            player_num += 1

        # Query the database to retrieve the first four rows from the "Category" table
        query = QSqlQuery("SELECT * FROM Category LIMIT 4")

        # Set the text fields for the category names
        cat_num = 1
        while query.next():
            exec(f"self.txt_catName{cat_num}.setText('{str(query.value(1))}')")
            exec(f"self.txt_catName{cat_num}.setAlignment(QtCore.Qt.AlignCenter)")
            cat_num += 1

    ######################
    # Navigation methods:
    ######################
    def move_left(self):
        if self.current_instr == 'Move Chip':
            left_border = [0, 9, 18, 27, 36, 45, 54, 63, 72] # Board left border cells

            player_pointer = getattr(self, f"pointer_{self.current_player}")
            player_pointer = player_pointer - 1
            setattr(self, f"pointer_{self.current_player}", player_pointer)
            exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x() - 95, self.dial_{self.current_player}.y())")
            allowed = True
            # Enforce border limit:
            for cell in left_border:
                if player_pointer == cell:
                    allowed = False
                    break
            if allowed and not self.getCellObject():
                allowed = False

            if not allowed:
                player_pointer = player_pointer + 1
                setattr(self, f"pointer_{self.current_player}", player_pointer)
                exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x() + 95, self.dial_{self.current_player}.y())")

            print(player_pointer)

    def move_right(self):
        if self.current_instr == 'Move Chip':
            right_border = [10, 19, 28, 37, 46, 55, 64, 73, 82] # Board right border cells

            player_pointer = getattr(self, f"pointer_{self.current_player}")
            player_pointer = player_pointer + 1
            setattr(self, f"pointer_{self.current_player}", player_pointer)
            exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x() + 95, self.dial_{self.current_player}.y())")
            allowed = True
            # Enforce border limit:
            for cell in right_border:
                if player_pointer == cell:
                    allowed = False
                    break
            if allowed and not self.getCellObject():
                allowed = False

            if not allowed:
                player_pointer = player_pointer - 1
                setattr(self, f"pointer_{self.current_player}", player_pointer)
                exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x() - 95, self.dial_{self.current_player}.y())")

            print(player_pointer)

    def move_up(self):
        if self.current_instr == 'Move Chip':
            player_pointer = getattr(self, f"pointer_{self.current_player}")
            player_pointer = player_pointer - 9
            setattr(self, f"pointer_{self.current_player}", player_pointer)
            exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x(), self.dial_{self.current_player}.y() - 100)")
            allowed = True
            # Enforce border limit:
            if player_pointer < 0:
                allowed = False
            else:
                if not self.getCellObject():
                    allowed = False

            if not allowed:
                player_pointer = player_pointer + 9
                setattr(self, f"pointer_{self.current_player}", player_pointer)
                exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x(), self.dial_{self.current_player}.y() + 100)")

            print(player_pointer)

    def move_down(self):
        if self.current_instr == 'Move Chip':
            player_pointer = getattr(self, f"pointer_{self.current_player}")
            player_pointer = player_pointer + 9
            setattr(self, f"pointer_{self.current_player}", player_pointer)
            exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x(), self.dial_{self.current_player}.y() + 100)")
            allowed = True
            # Enforce border limit:
            if player_pointer < 0:
                allowed = False
            else:
                if not self.getCellObject():
                    allowed = False

            if not allowed:
                player_pointer = player_pointer - 9
                setattr(self, f"pointer_{self.current_player}", player_pointer)
                exec(f"self.dial_{self.current_player}.move(self.dial_{self.current_player}.x(), self.dial_{self.current_player}.y() - 100)")

            print(player_pointer)

    def getCellObject(self):
        for obj in self.cells:
            player_pointer = getattr(self, f"pointer_{self.current_player}")
            if player_pointer == int(obj.objectName().split("_")[1]):
                return True
        return False

    def rolltheDice(self):
        if (self.current_instr == 'Roll Die') or (self.current_instr == 'Roll Again!'):
            image = QPixmap("board/dice-1.png")
            self.die_image.setPixmap(image)

            die = random.randint (1,6)
            image2 = QPixmap("board/dice-"+str(die)+".png")
            self.die_image.setPixmap(image2)

            # Change State
            self.current_instr = 'Move Chip'
            # Set current instruction name in text box
            self.txt_currentInstruct.setText(self.current_instr)
            self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    def changePlayer(self):
        if self.current_instr == 'Vote Answer':
            players = ["player1", "player2", "player3", "player4"]
            current_index = players.index(self.current_player)

            # Query the database to retrieve the first four rows from the "Player" table
            query = QSqlQuery("SELECT * FROM Player LIMIT 4")

            # Set the text fields for current player box
            player_names = []
            while query.next():
                player_names.append(query.value(1))

            # Set current player name in text box
            while self.player_active[(current_index + 1) % len(players)] == 0:
                current_index = current_index + 1

            self.current_player = players[(current_index + 1) % len(players)]

            self.txt_currentPlayer.setText(player_names[(current_index + 1) % len(players)])
            self.txt_currentPlayer.setAlignment(QtCore.Qt.AlignCenter)

            # Change State
            self.current_instr = 'Roll Die'
            # Set current instruction name in text box
            self.txt_currentInstruct.setText(self.current_instr)
            self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    def confirmMove(self):
        rollAgain = [1, 9, 73, 81]
        player_pointer = getattr(self, f"pointer_{self.current_player}")

        if self.current_instr == 'Move Chip':
            # Change State
            if player_pointer in rollAgain:
                self.current_instr = 'Roll Again!'
            else:
                self.current_instr = 'Answer Question'
            # Set current instruction name in text box
            self.txt_currentInstruct.setText(self.current_instr)
            self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    def promptQuestion(self):
        if self.current_instr == 'Answer Question':
            cat1_positions = [5, 10, 18, 40, 44, 46, 54, 59, 75, 79]
            cat2_positions = [3,  7, 23, 28, 36, 38, 42, 64, 72, 77]
            cat3_positions = [2,  6, 14, 27, 37, 43, 50, 63, 74, 78]
            cat4_positions = [4,  8, 19, 32, 39, 45, 55, 68, 76, 80]
            center_position = [41]

            player_pointer = getattr(self, f"pointer_{self.current_player}")

            database.setDatabaseName("trivial_pursuit.db")

            if not database.open():
                print("Could not open the database!")
                return False

            query = QSqlQuery("SELECT category_name FROM Category LIMIT 4")

            categories = []  # Create an empty list to store the category names

            while query.next():
                category_name = query.value(0)
                categories.append(category_name)

            string_categories = [str(item) for item in categories]

            # Now you have the first 4 category names in the "categories" list
            # Access them using index like categories[0], categories[1], etc.

            cat1 = string_categories[0]
            cat2 = string_categories[1]
            cat3 = string_categories[2]
            cat4 = string_categories[3]

            if player_pointer in cat1_positions:
                query = QSqlQuery("SELECT question_text, correct_answer,category FROM Questions  WHERE category = ?  AND used = 0 ORDER BY RANDOM() LIMIT 1 ")
                query.addBindValue(cat1)
                if query.exec():
                    if query.next():
                        question_text = query.value(0)
                        correct_answer_text = query.value(1)
                        category = query.value(2)
                        updateQuery = QSqlQuery("UPDATE Questions SET used = 1 WHERE question_text = ?")
                        updateQuery.addBindValue(question_text)
                        updateQuery.exec()
            elif player_pointer in cat2_positions:
                query = QSqlQuery("SELECT question_text, correct_answer,category FROM Questions  WHERE category = ?  AND used = 0 ORDER BY RANDOM() LIMIT 1 ")
                query.addBindValue(cat2)
                if query.exec():
                    if query.next():
                        question_text = query.value(0)
                        correct_answer_text = query.value(1)
                        category = query.value(2)
                        updateQuery = QSqlQuery("UPDATE Questions SET used = 1 WHERE question_text = ?")
                        updateQuery.addBindValue(question_text)
                        updateQuery.exec()
            elif player_pointer in cat3_positions:
                query = QSqlQuery("SELECT question_text, correct_answer,category FROM Questions  WHERE category = ?  AND used = 0 ORDER BY RANDOM() LIMIT 1 ")
                query.addBindValue(cat3)
                if query.exec():
                    if query.next():
                        question_text = query.value(0)
                        correct_answer_text = query.value(1)
                        category = query.value(2)
                        updateQuery = QSqlQuery("UPDATE Questions SET used = 1 WHERE question_text = ?")
                        updateQuery.addBindValue(question_text)
                        updateQuery.exec()
            elif player_pointer in cat4_positions:
                query = QSqlQuery("SELECT question_text, correct_answer,category FROM Questions  WHERE category = ? AND used = 0 ORDER BY RANDOM() LIMIT 1 ")
                query.addBindValue(cat4)
                if query.exec():
                    if query.next():
                        question_text = query.value(0)
                        correct_answer_text = query.value(1)
                        category = query.value(2)
                        updateQuery = QSqlQuery("UPDATE Questions SET used = 1 WHERE question_text = ?")
                        updateQuery.addBindValue(question_text)
                        updateQuery.exec()
            elif player_pointer in center_position:
                for category in string_categories:
                    message_box = QMessageBox()
                    message_box.setIcon(QMessageBox.Question)
                    message_box.setText(f"Do you want to proceed with {category}?")
                    message_box.setWindowTitle("Confirmation")
                    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

                    result = message_box.exec_()

                    if result == QMessageBox.Yes:
                        query = QSqlQuery("SELECT question_text, correct_answer,category FROM Questions  WHERE category = ? ORDER BY RANDOM() LIMIT 1 ")
                        query.addBindValue(f"{category}")
                        if query.exec():
                            if query.next():
                                question_text = query.value(0)
                                correct_answer_text = query.value(1)
                        category = query.value(2)
                        print('{category}')
                        break
                    elif result == QMessageBox.No:
                        print("No")
            else:
                print("No rows found for the specified category.")

            media_extensions = ['.mp4', '.mp3', '.png', '.jpeg', '.jpg', '.jpe', '.jiff']

            file_extension = os.path.splitext(question_text)[-1].lower()

            if file_extension in media_extensions:
                video_thread = threading.Thread(target=lambda: subprocess.Popen(['start', '', question_text], shell=True))
                video_thread.start()
            else:
                message_box = QMessageBox()
                message_box.setIcon(QMessageBox.Question)
                message_box.setWindowTitle("Please Answer the Question")
                message_box.setText(question_text)
                message_box.setStandardButtons(QMessageBox.Open)
                message_box.setInformativeText("Press 'Open' to reveal answer")
                message_box.exec_()

            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle("Correct Answer")
            message_box.setText(correct_answer_text)
            message_box.exec_()

            # Change State
            self.current_instr = 'Vote Answer'
            # Set current instruction name in text box
            self.txt_currentInstruct.setText(self.current_instr)
            self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    def checkHQButton(self):
        if self.current_instr == 'Vote Answer':
            hq_positions = [5, 37, 45, 77, 41]
            player_pointer = getattr(self, f"pointer_{self.current_player}")

            if player_pointer in hq_positions:
                # Category 1 (Red)
                if player_pointer == 5:
                    exec(f"self.btn_HQ_{self.current_player}_cat1.setStyleSheet('background-color: rgb(255, 0, 77)')")
                # Category 2 (Yellow)
                elif player_pointer == 37:
                    exec(f"self.btn_HQ_{self.current_player}_cat2.setStyleSheet('background-color: rgb(255, 236, 39)')")
                # Category 3 (Green)
                elif player_pointer == 45:
                    exec(f"self.btn_HQ_{self.current_player}_cat3.setStyleSheet('background-color: rgb(0, 228, 54)')")
                # Category 4 (Blue)
                elif player_pointer == 77:
                    exec(f"self.btn_HQ_{self.current_player}_cat4.setStyleSheet('background-color: rgb(41, 173, 255)')")
                # Center trivial compute button
                elif player_pointer == 41:
                    # Define the colors as RGB tuples
                    colors_to_check = [
                        (255, 0, 77),   # Color for 'cat1' - Red
                        (255, 236, 39), # Color for 'cat2' - Yellow
                        (0, 228, 54),   # Color for 'cat3' - Green
                        (41, 173, 255)  # Color for 'cat4' - Blue
                    ]

                    # Get the colors for each category using checkColor method
                    colors = [self.checkColor(category) for category in ['cat1', 'cat2', 'cat3', 'cat4']]

                    # Check if all the colors match the desired colors and say winner
                    if all(color == target_color for color, target_color in zip(colors, colors_to_check)):
                        message_box = QMessageBox()
                        message_box.setIcon(QMessageBox.Information)

                        players = ["player1", "player2", "player3", "player4"]
                        current_index = players.index(self.current_player)

                        # Query the database to retrieve the first four rows from the "Player" table
                        query = QSqlQuery("SELECT * FROM Player LIMIT 4")

                        # Set the text fields for current player box
                        player_names = []
                        while query.next():
                            player_names.append(query.value(1))

                        # Set current player name in text box
                        player_name = player_names[(current_index) % len(players)]

                        message_box.setWindowTitle("Winner")
                        message_box.setText(f"{player_name} Wins!")
                        message_box.exec_()

            # Change State
            self.current_instr = 'Roll Die'
            # Set current instruction name in text box
            self.txt_currentInstruct.setText(self.current_instr)
            self.txt_currentInstruct.setAlignment(QtCore.Qt.AlignCenter)

    def checkColor(self, category):
        # Get the palette of the button
        button_palette = getattr(self, f"btn_HQ_{self.current_player}_{category}").palette()
        # Get the background color of the button
        backgroundRole = getattr(self, f"btn_HQ_{self.current_player}_{category}").backgroundRole()
        button_color = button_palette.color(backgroundRole)
        # Print the color (in RGB format)
        r, g, b, _ = button_color.getRgb()

        return r, g, b

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
    widget.addWidget(category_menu)
    widget.setFixedHeight(900)
    widget.setFixedWidth(880)
    widget.show()
    app.exec_()
