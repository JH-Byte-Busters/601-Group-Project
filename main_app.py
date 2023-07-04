import sys
import typing
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import create_db

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window/main_window.ui", self)
        self.pushButton.clicked.connect(self.gotoBoard)
        self.pushButton.clicked.connect(create_db.create_database)
    
    def gotoBoard(self):
        board=Board()        
        widget.addWidget(board)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board/board.ui", self)
        self.pushButton_2.clicked.connect(self.gotoMenu)
        self.pushButton_2.clicked.connect(create_db.close_database)
    
    def gotoMenu(self):
        main_app=Board()
        widget.addWidget(main_app)
        widget.setCurrentIndex(widget.currentIndex()-1)

# main
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main_app=MainWindow()
board=Board()
widget.setWindowTitle("TrivialCompute")
widget.addWidget(main_app)
widget.addWidget(board)
widget.setFixedHeight(900)
widget.setFixedWidth(880)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")