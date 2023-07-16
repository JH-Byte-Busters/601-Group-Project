from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtGui import QIcon
import os

class GamePlayer(QDialog):
    def __init__(self):
        super().__init__()
        self.cells = []
        self.pointer = 41
        self.category = "NONE"

    # Player navigation methods:
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
                obj.setIcon(QIcon(QIcon(os.path.join('chips/player1.png'))))
                # obj.setStyleSheet("background-color:black; color:white;")
                return True
        return False       
    
    # Player question-trigger methods:
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

    # Player question window:
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
