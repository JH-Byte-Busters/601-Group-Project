import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import create_db
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window/main_window.ui", self)
        self.pushButton.clicked.connect(self.gotoPlayerMenu)
        self.pushButton.clicked.connect(create_db.create_database)
    
    def gotoPlayerMenu(self):
        player_menu=PlayerMenu()        
        widget.addWidget(player_menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

class PlayerMenu(QDialog):
    def __init__(self):
        super(PlayerMenu, self).__init__()
        loadUi("player_menu/player_menu.ui", self)
        self.pushButton.clicked.connect(self.insertData)
        self.pushButton_2.clicked.connect(self.gotoMenu)
    
    def gotoMenu(self):
        main_app=MainWindow()
        widget.addWidget(main_app)
        widget.setCurrentIndex(widget.currentIndex()-1)

    def insertData(self):
        connection = QSqlDatabase.addDatabase('QSQLITE')
        connection.setDatabaseName('trivial_pursuit.db')
        connection.open()
    
        if not connection.isOpen():
            print('Connection error occurred.')
        else:
            print(connection.tables())

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

        #if query.exec_("SELECT * FROM Player"):
        #    rec = query.record()
        #    while query.next():
        #        for ix in range(rec.count()):
        #            val = query.value(ix)
        #            print(rec.fieldName(ix), val)
        #    else:
        #        print(query.lastError().text())

class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board/board.ui", self)
        self.pushButton_2.clicked.connect(self.gotoMenu)
        self.pushButton_2.clicked.connect(create_db.close_database)
    
    def gotoMenu(self):
        main_app=MainWindow()
        widget.addWidget(main_app)
        widget.setCurrentIndex(widget.currentIndex()-1)

# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main_app=MainWindow()
player_menu=PlayerMenu()
board=Board()
widget.setWindowTitle("TrivialCompute")
widget.addWidget(main_app)
widget.addWidget(player_menu)
widget.addWidget(board)
widget.setFixedHeight(900)
widget.setFixedWidth(880)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")