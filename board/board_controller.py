import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    # CREATE INDIVIDUAL ROWS:
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Trivial Compute Game")
        layout = QGridLayout()
        
	# 1st row:
        rollCell1 = QPushButton('Roll\nAgain')
        rollCell1.setStyleSheet("background-color:lightblue")
        layout.addWidget(rollCell1,0,0)
        
        cell1 = QPushButton('Y')
        cell1.setStyleSheet("background-color:yellow")
        layout.addWidget(cell1,0,1)
        
        cell2 = QPushButton('B')
        cell2.setStyleSheet("background-color:blue")
        layout.addWidget(cell2,0,2)
        
        cell3 = QPushButton('G')
        cell3.setStyleSheet("background-color:green")
        layout.addWidget(cell3,0,3)
        
        cell4 = QPushButton('R')
        cell4.setStyleSheet("background-color:red")
        layout.addWidget(cell4,0,4)
        
        cell5 = QPushButton('Y')
        cell5.setStyleSheet("background-color:yellow")
        layout.addWidget(cell5,0,5)
        
        cell6 = QPushButton('B')
        cell6.setStyleSheet("background-color:blue")
        layout.addWidget(cell6,0,6)
        
        cell7 = QPushButton('G')
        cell7.setStyleSheet("background-color:green")
        layout.addWidget(cell7,0,7)
        
        rollCell2 = QPushButton('Roll\nAgain')
        rollCell2.setStyleSheet("background-color:lightblue")
        layout.addWidget(rollCell2,0,8)
        
        # 2nd row:
        cell8 = QPushButton('R')
        cell8.setStyleSheet("background-color:red")
        layout.addWidget(cell8,1,0)
        
        cell12 = QPushButton('Y')
        cell12.setStyleSheet("background-color:yellow")
        layout.addWidget(cell12,1,4)
        
        cell16 = QPushButton('R')
        cell16.setStyleSheet("background-color:red")
        layout.addWidget(cell16,1,8)
        
        # 3rd row:
        cell17 = QPushButton('G')
        cell17.setStyleSheet("background-color:green")
        layout.addWidget(cell17,2,0)
        
        layout.addWidget(QPushButton('PLAYER_1\nEARNED BADGES'),2,2)
        
        cell21 = QPushButton('B')
        cell21.setStyleSheet("background-color:blue")
        layout.addWidget(cell21,2,4)
        
        layout.addWidget(QPushButton('PLAYER_2\nEARNED BADGES'),2,6)
        
        cell25 = QPushButton('Y')
        cell25.setStyleSheet("background-color:yellow")
        layout.addWidget(cell25,2,8)
        
        # 4th row:
        layout.addWidget(QPushButton('10'),3,0)
        layout.addWidget(QPushButton('11'),3,4)
        layout.addWidget(QPushButton('12'),3,8)
        
        # 5th row:
        layout.addWidget(QPushButton('10'),4,0)
        layout.addWidget(QPushButton('11'),4,1)
        layout.addWidget(QPushButton('12'),4,2)
        layout.addWidget(QPushButton('10'),4,3)
        layout.addWidget(QPushButton('11'),4,4)
        layout.addWidget(QPushButton('12'),4,5)
        layout.addWidget(QPushButton('10'),4,6)
        layout.addWidget(QPushButton('11'),4,7)
        layout.addWidget(QPushButton('12'),4,8)
        
        # 6th row:
        layout.addWidget(QPushButton('10'),5,0)
        layout.addWidget(QPushButton('11'),5,4)
        layout.addWidget(QPushButton('12'),5,8)
        
        # 7th row:
        layout.addWidget(QPushButton('7'),6,0)
        layout.addWidget(QPushButton('PLAYER_3\nEARNED BADGES'),6,2)
        layout.addWidget(QPushButton('8'),6,4)
        layout.addWidget(QPushButton('PLAYER_4\nEARNED BADGES'),6,6)
        layout.addWidget(QPushButton('9'),6,8)
        
        # 8th row:
        layout.addWidget(QPushButton('10'),7,0)
        layout.addWidget(QPushButton('11'),7,4)
        layout.addWidget(QPushButton('12'),7,8)
        
        # 9th row:
        rollCell3 = QPushButton('Roll\nAgain')
        rollCell3.setStyleSheet("background-color:lightblue")
        layout.addWidget(rollCell3,8,0)
        
        layout.addWidget(QPushButton('11'),8,1)
        layout.addWidget(QPushButton('12'),8,2)
        layout.addWidget(QPushButton('10'),8,3)
        layout.addWidget(QPushButton('11'),8,4)
        layout.addWidget(QPushButton('12'),8,5)
        layout.addWidget(QPushButton('10'),8,6)
        layout.addWidget(QPushButton('11'),8,7)
        
        rollCell4 = QPushButton('Roll\nAgain')
        rollCell4.setStyleSheet("background-color:lightblue")
        layout.addWidget(rollCell4,8,8)
        
        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
