from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - Trivial Compute Game'
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
        Cell1 = QPushButton('Roll\nAgain')
        Cell1.setStyleSheet("background-color:lightblue")
        layout.addWidget(Cell1,0,0)
        
        cell2 = QPushButton('Y')
        cell2.setStyleSheet("background-color:yellow")
        layout.addWidget(cell2,0,1)
        
        cell3 = QPushButton('B')
        cell3.setStyleSheet("background-color:blue")
        layout.addWidget(cell3,0,2)
        
        cell4 = QPushButton('G')
        cell4.setStyleSheet("background-color:green")
        layout.addWidget(cell4,0,3)
        
        cell5 = QPushButton('HQ')
        cell5.setStyleSheet("background-color:red")
        layout.addWidget(cell5,0,4)
        
        cell6 = QPushButton('Y')
        cell6.setStyleSheet("background-color:yellow")
        layout.addWidget(cell6,0,5)
        
        cell7 = QPushButton('B')
        cell7.setStyleSheet("background-color:blue")
        layout.addWidget(cell7,0,6)
        
        cell8 = QPushButton('G')
        cell8.setStyleSheet("background-color:green")
        layout.addWidget(cell8,0,7)
        
        Cell9 = QPushButton('Roll\nAgain')
        Cell9.setStyleSheet("background-color:lightblue")
        layout.addWidget(Cell9,0,8)
        
        # 2nd row:
        cell10 = QPushButton('R')
        cell10.setStyleSheet("background-color:red")
        layout.addWidget(cell10,1,0)
        
        cell14 = QPushButton('Y')
        cell14.setStyleSheet("background-color:yellow")
        layout.addWidget(cell14,1,4)
        
        cell18 = QPushButton('R')
        cell18.setStyleSheet("background-color:red")
        layout.addWidget(cell18,1,8)
        
        # 3rd row:
        cell19 = QPushButton('G')
        cell19.setStyleSheet("background-color:green")
        layout.addWidget(cell19,2,0)
        
        layout.addWidget(QPushButton('PLAYER_1\nEARNED BADGES'),2,2)
        
        cell23 = QPushButton('B')
        cell23.setStyleSheet("background-color:blue")
        layout.addWidget(cell23,2,4)
        
        layout.addWidget(QPushButton('PLAYER_2\nEARNED BADGES'),2,6)
        
        cell27 = QPushButton('Y')
        cell27.setStyleSheet("background-color:yellow")
        layout.addWidget(cell27,2,8)
        
        # 4th row:
        layout.addWidget(QPushButton('28'),3,0)
        layout.addWidget(QPushButton('32'),3,4)
        layout.addWidget(QPushButton('36'),3,8)
        
        # 5th row:
        cell35 = QPushButton('HQ')
        cell35.setStyleSheet("background-color:yellow")
        layout.addWidget(cell35,4,0)
        
        layout.addWidget(QPushButton('38'),4,1)
        layout.addWidget(QPushButton('39'),4,2)
        layout.addWidget(QPushButton('40'),4,3)
        layout.addWidget(QPushButton('41'),4,4)
        layout.addWidget(QPushButton('42'),4,5)
        layout.addWidget(QPushButton('43'),4,6)
        layout.addWidget(QPushButton('44'),4,7)
        
        cell43 = QPushButton('HQ')
        cell43.setStyleSheet("background-color:green")
        layout.addWidget(cell43,4,8)
        
        # 6th row:
        layout.addWidget(QPushButton('46'),5,0)
        layout.addWidget(QPushButton('50'),5,4)
        layout.addWidget(QPushButton('54'),5,8)
        
        # 7th row:
        layout.addWidget(QPushButton('55'),6,0)
        layout.addWidget(QPushButton('PLAYER_3\nEARNED BADGES'),6,2)
        layout.addWidget(QPushButton('59'),6,4)
        layout.addWidget(QPushButton('PLAYER_4\nEARNED BADGES'),6,6)
        layout.addWidget(QPushButton('63'),6,8)
        
        # 8th row:
        layout.addWidget(QPushButton('64'),7,0)
        layout.addWidget(QPushButton('68'),7,4)
        layout.addWidget(QPushButton('72'),7,8)
        
        # 9th row:
        cell73 = QPushButton('Roll\nAgain')
        cell73.setStyleSheet("background-color:lightblue")
        layout.addWidget(cell73,8,0)
        
        layout.addWidget(QPushButton('74'),8,1)
        layout.addWidget(QPushButton('75'),8,2)
        layout.addWidget(QPushButton('76'),8,3)
        
        cell77 = QPushButton('HQ')
        cell77.setStyleSheet("background-color:blue")
        layout.addWidget(cell77,8,4)
        
        layout.addWidget(QPushButton('78'),8,5)
        layout.addWidget(QPushButton('79'),8,6)
        layout.addWidget(QPushButton('80'),8,7)
        
        cell81 = QPushButton('Roll\nAgain')
        cell81.setStyleSheet("background-color:lightblue")
        layout.addWidget(cell81,8,8)
        
        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
