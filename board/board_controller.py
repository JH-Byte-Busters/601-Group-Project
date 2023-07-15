from PyQt5.QtWidgets import QApplication, QPushButton, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon
from collections import defaultdict
import sys
import os

class BoardWindow(QDialog):
    def __init__(self):
        super().__init__()
        # UI config vars:
        self.windows = []
        self.title = 'Game Board'
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 500

        # Navigation global variables:
        self.cells = []
        self.pointer = 41
        self.category = "NONE"
        
        self.initUI() # Execute GUI window.
        
    def initUI(self):
        # Create and trigger main board window:
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
    
    # CREATE INDIVIDUAL ROWS:
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("TRIVIAL COMPUTE GAME")
        layout = QGridLayout()
        
        # 1st ROW:
        self.cell1 = QPushButton('ROLL')
        self.cell1.setObjectName('1')
        self.cell1.setStyleSheet("background-color:black")
        self.cell1.clicked.connect(self.roll_die)
        layout.addWidget(self.cell1,0,0)
        self.cells.append(self.cell1)
        
        self.cell2 = QPushButton('Y')
        self.cell2.setObjectName('2')
        self.cell2.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell2.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell2,0,1)
        self.cells.append(self.cell2)
        
        self.cell3 = QPushButton('B')
        self.cell3.setObjectName('3')
        self.cell3.setStyleSheet("background-color:blue; color:black;")
        self.cell3.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell3,0,2)
        self.cells.append(self.cell3)

        self.cell4 = QPushButton('G')
        self.cell4.setObjectName('4')
        self.cell4.setStyleSheet("background-color:green; color:black;")
        self.cell4.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell4,0,3)
        self.cells.append(self.cell4)

        self.cell5 = QPushButton('HQ')
        self.cell5.setObjectName('5')
        self.cell5.setStyleSheet("background-color:red; color:black;")
        self.cell5.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell5,0,4)
        self.cells.append(self.cell5)

        self.cell6 = QPushButton('Y')
        self.cell6.setObjectName('6')
        self.cell6.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell6.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell6,0,5)
        self.cells.append(self.cell6)

        self.cell7 = QPushButton('B')
        self.cell7.setObjectName('7')
        self.cell7.setStyleSheet("background-color:blue; color:black;")
        self.cell7.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell7,0,6)
        self.cells.append(self.cell7)

        self.cell8 = QPushButton('G')
        self.cell8.setObjectName('8')
        self.cell8.setStyleSheet("background-color:green; color:black;")
        self.cell8.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell8,0,7)
        self.cells.append(self.cell8)

        self.cell9 = QPushButton('ROLL')
        self.cell9.setObjectName('9')
        self.cell9.setStyleSheet("background-color:black")
        self.cell9.clicked.connect(self.roll_die)
        layout.addWidget(self.cell9,0,8)
        self.cells.append(self.cell9)

        # 2nd ROW:
        self.cell10 = QPushButton('R')
        self.cell10.setObjectName('10')
        self.cell10.setStyleSheet("background-color:red; color:black;")
        self.cell10.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell10,1,0)
        self.cells.append(self.cell10)

        self.cell14 = QPushButton('Y')
        self.cell14.setObjectName('14')
        self.cell14.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell14.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell14,1,4)
        self.cells.append(self.cell14)
        
        self.cell18 = QPushButton('R')
        self.cell18.setObjectName('18')
        self.cell18.setStyleSheet("background-color:red; color:black;")
        self.cell18.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell18,1,8)
        self.cells.append(self.cell18)
        
        # 3rd ROW:
        self.cell19 = QPushButton('G')
        self.cell19.setObjectName('19')
        self.cell19.setStyleSheet("background-color:green; color:black;")
        self.cell19.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell19,2,0)
        self.cells.append(self.cell19)
        
        layout.addWidget(QPushButton('Player1'),2,2)
        
        self.cell23 = QPushButton('B')
        self.cell23.setObjectName('23')
        self.cell23.setStyleSheet("background-color:blue; color:black;")
        self.cell23.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell23,2,4)
        self.cells.append(self.cell23)
        
        layout.addWidget(QPushButton('Player2'),2,6)
        
        self.cell27 = QPushButton('Y')
        self.cell27.setObjectName('27')
        self.cell27.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell27.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell27,2,8)
        self.cells.append(self.cell27)
        
        # 4th ROW:
        self.cell28 = QPushButton('B')
        self.cell28.setObjectName('28')
        self.cell28.setStyleSheet("background-color:blue; color:black;")
        self.cell28.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell28,3,0)
        self.cells.append(self.cell28)
        
        self.cell32 = QPushButton('G')
        self.cell32.setObjectName('32')
        self.cell32.setStyleSheet("background-color:green; color:black;")
        self.cell32.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell32,3,4)
        self.cells.append(self.cell32)

        self.cell36 = QPushButton('B')
        self.cell36.setObjectName('36')
        self.cell36.setStyleSheet("background-color:blue; color:black;")
        self.cell36.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell36,3,8)
        self.cells.append(self.cell36)
        
        # 5th ROW:
        self.cell37 = QPushButton('HQ')
        self.cell37.setObjectName('37')
        self.cell37.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell37.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell37,4,0)
        self.cells.append(self.cell37)
        
        self.cell38 = QPushButton('B')
        self.cell38.setObjectName('38')
        self.cell38.setStyleSheet("background-color:blue; color:black;")
        self.cell38.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell38,4,1)
        self.cells.append(self.cell38)
        
        self.cell39 = QPushButton('G')
        self.cell39.setObjectName('39')
        self.cell39.setStyleSheet("background-color:green; color:black;")
        self.cell39.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell39,4,2)
        self.cells.append(self.cell39)
        
        self.cell40 = QPushButton('R')
        self.cell40.setObjectName('40')
        self.cell40.setStyleSheet("background-color:red; color:black;")
        self.cell40.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell40,4,3)
        self.cells.append(self.cell40)
        
        self.cell41 = QPushButton('START')
        self.cell41.setStyleSheet("background-color:grey; color:black;")
        layout.addWidget(self.cell41,4,4)
        self.cells.append(self.cell41)
        
        self.cell42 = QPushButton('B')
        self.cell42.setObjectName('42')
        self.cell42.setStyleSheet("background-color:blue; color:black;")
        self.cell42.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell42,4,5)
        self.cells.append(self.cell42)
        
        self.cell43 = QPushButton('Y')
        self.cell43.setObjectName('43')
        self.cell43.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell43.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell43,4,6)
        self.cells.append(self.cell43)
        
        self.cell44 = QPushButton('R')
        self.cell44.setObjectName('44')
        self.cell44.setStyleSheet("background-color:red; color:black;")
        self.cell44.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell44,4,7)
        self.cells.append(self.cell44)
        
        self.cell45 = QPushButton('HQ')
        self.cell45.setObjectName('45')
        self.cell45.setStyleSheet("background-color:green; color:black;")
        self.cell45.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell45,4,8)
        self.cells.append(self.cell45)
        
        # 6th ROW:
        self.cell46 = QPushButton('R')
        self.cell46.setObjectName('46')
        self.cell46.setStyleSheet("background-color:red; color:black;")
        self.cell46.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell46,5,0)
        self.cells.append(self.cell46)
        
        self.cell50 = QPushButton('Y')
        self.cell50.setObjectName('50')
        self.cell50.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell50.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell50,5,4)
        self.cells.append(self.cell50)
        
        self.cell54 = QPushButton('R')
        self.cell54.setObjectName('54')
        self.cell54.setStyleSheet("background-color:red; color:black;")
        self.cell54.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell54,5,8)
        self.cells.append(self.cell54)
        
        # 7th ROW:
        self.cell55 = QPushButton('G')
        self.cell55.setObjectName('55')
        self.cell55.setStyleSheet("background-color:green; color:black;")
        self.cell55.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell55,6,0)
        self.cells.append(self.cell55)
        
        layout.addWidget(QPushButton('Player3'),6,2)

        self.cell59 = QPushButton('R')
        self.cell59.setObjectName('59')
        self.cell59.setStyleSheet("background-color:red; color:black;")
        self.cell59.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell59,6,4)
        self.cells.append(self.cell59)
        
        layout.addWidget(QPushButton('Player4'),6,6)

        self.cell63 = QPushButton('Y')
        self.cell63.setObjectName('63')
        self.cell63.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell63.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell63,6,8)
        self.cells.append(self.cell63)
        
        # 8th ROW:
        self.cell64 = QPushButton('B')
        self.cell64.setObjectName('64')
        self.cell64.setStyleSheet("background-color:blue; color:black;")
        self.cell64.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell64,7,0)
        self.cells.append(self.cell64)
        
        self.cell68 = QPushButton('G')
        self.cell68.setObjectName('68')
        self.cell68.setStyleSheet("background-color:green; color:black;")
        self.cell68.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell68,7,4)
        self.cells.append(self.cell68)
        
        self.cell72 = QPushButton('B')
        self.cell72.setObjectName('72')
        self.cell72.setStyleSheet("background-color:blue; color:black;")
        self.cell72.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell72,7,8)
        self.cells.append(self.cell72)
        
        # 9th ROW:
        self.cell73 = QPushButton('ROLL')
        self.cell73.setObjectName('73')
        self.cell73.setStyleSheet("background-color:black")
        self.cell73.clicked.connect(self.roll_die)
        layout.addWidget(self.cell73,8,0)
        self.cells.append(self.cell73)
        
        self.cell74 = QPushButton('Y')
        self.cell74.setObjectName('74')
        self.cell74.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell74.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell74,8,1)
        self.cells.append(self.cell74)
        
        self.cell75 = QPushButton('R')
        self.cell75.setObjectName('75')
        self.cell75.setStyleSheet("background-color:red; color:black;")
        self.cell75.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell75,8,2)
        self.cells.append(self.cell75)
        
        self.cell76 = QPushButton('G')
        self.cell76.setObjectName('76')
        self.cell76.setStyleSheet("background-color:green; color:black;")
        self.cell76.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell76,8,3)
        self.cells.append(self.cell76)
        
        self.cell77 = QPushButton('HQ')
        self.cell77.setObjectName('77')
        self.cell77.setStyleSheet("background-color:blue; color:black;")
        self.cell77.clicked.connect(self.blue_category_clicked)
        layout.addWidget(self.cell77,8,4)
        self.cells.append(self.cell77)
        
        self.cell78 = QPushButton('Y')
        self.cell78.setObjectName('78')
        self.cell78.setStyleSheet("background-color:goldenrod; color:black;")
        self.cell78.clicked.connect(self.yellow_category_clicked)
        layout.addWidget(self.cell78,8,5)
        self.cells.append(self.cell78)
        
        self.cell79 = QPushButton('R')
        self.cell79.setObjectName('79')
        self.cell79.setStyleSheet("background-color:red; color:black;")
        self.cell79.clicked.connect(self.red_category_clicked)
        layout.addWidget(self.cell79,8,6)
        self.cells.append(self.cell79)
        
        self.cell80 = QPushButton('G')
        self.cell80.setObjectName('80')
        self.cell80.setStyleSheet("background-color:green; color:black;")
        self.cell80.clicked.connect(self.green_category_clicked)
        layout.addWidget(self.cell80,8,7)
        self.cells.append(self.cell80)
        
        self.cell81 = QPushButton('ROLL')
        self.cell81.setObjectName('81')
        self.cell81.setStyleSheet("background-color:black")
        self.cell81.clicked.connect(self.roll_die)
        layout.addWidget(self.cell81,8,8)
        self.cells.append(self.cell81)
        
        ########################
        # NAVIGATION CONTROLLER:
        ########################
        layout.addWidget(QPushButton('*'),7,9)
        self.left = QPushButton('LEFT')
        self.left.setStyleSheet("background-color: greenyellow; color:black;")
        self.left.clicked.connect(self.move_left)
        layout.addWidget(self.left,7,10)

        self.up = QPushButton('UP')
        self.up.setStyleSheet("background-color: greenyellow; color:black;")
        self.up.clicked.connect(self.move_up)
        layout.addWidget(self.up,6,11)

        self.roll_dice = QPushButton('QUESTION')
        self.roll_dice.setStyleSheet("background-color:red")
        self.roll_dice.clicked.connect(self.show_question)
        layout.addWidget(self.roll_dice,7,11)

        self.down = QPushButton('DOWN')
        self.down.setStyleSheet("background-color: greenyellow; color:black;")
        self.down.clicked.connect(self.move_down)
        layout.addWidget(self.down,8,11)

        self.right = QPushButton('RIGHT')
        self.right.setStyleSheet("background-color: greenyellow; color:black;")
        self.right.clicked.connect(self.move_right)
        layout.addWidget(self.right,7,12)
        
        self.horizontalGroupBox.setLayout(layout)
        
    ######################
    # Navigation methods:
    ######################
    def move_left(self):
        left_border = [0, 9, 18, 27, 36, 45, 54, 63, 72] # Board left border cells
        self.pointer = self.pointer - 1
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
        print(self.pointer)

    def move_right(self):
        left_border = [10, 19, 28, 37, 46, 55, 64, 73, 82] # Board right border cells
        self.pointer = self.pointer + 1
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
        print(self.pointer)
    
    def move_up(self):
        self.pointer = self.pointer - 9
        allowed = True
        # Enforce border limit:
        if self.pointer < 0:
            allowed = False
        else:
            if not self.getCellObject():
                allowed = False
        
        if not allowed:
            self.pointer = self.pointer + 9
        print(self.pointer)
    
    def move_down(self):
        self.pointer = self.pointer + 9
        allowed = True
        # Enforce border limit:
        if self.pointer < 0:
            allowed = False
        else:
            if not self.getCellObject():
                allowed = False
        
        if not allowed:
            self.pointer = self.pointer - 9
        print(self.pointer)
    
    def getCellObject(self):
        for obj in self.cells:
            if str(self.pointer) == obj.objectName():
                obj.setIcon(QIcon(QIcon(os.path.join('player1.png'))))
                # obj.setStyleSheet("background-color:black; color:white;")
                return True
        return False       
    
    ###########################
    # Question-trigger methods:
    ###########################
    def show_question(self):
        for obj in self.cells:
            if str(self.pointer) != obj.objectName():
                obj.setIcon(QIcon(QIcon(os.path.join(''))))
            else:
                obj.clicked.emit()

    def red_category_clicked(self):
        print("red_category_clicked!")
        self.category = "RED_CATEGORY"
        self.triggerPopup()
    
    def blue_category_clicked(self):
        print("blue_category_clicked!")
        self.category = "BLUE_CATEGORY"
        self.triggerPopup()
    
    def green_category_clicked(self):
        print("green_category_clicked!")
        self.category = "GREEN_CATEGORY"
        self.triggerPopup()
    
    def yellow_category_clicked(self):
        print("yellow_category_clicked!")
        self.category = "YELLOW_CATEGORY"
        self.triggerPopup()

    # https://www.techwithtim.net/tutorials/python-module-walk-throughs/pyqt5-tutorial/messageboxes
    def triggerPopup(self):
        popup = QMessageBox()
        popup.setText(self.category + ":\n\nAre there 10 planets in the solar system?")
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        popup.setDetailedText("More question details")
        popup.setWindowTitle(self.category + "QUESTION!")
        popup.setIcon(QMessageBox.Question)
        popup.exec_()
    
    def roll_die(self):
        print("rolling dice...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BoardWindow()
    sys.exit(app.exec_())
