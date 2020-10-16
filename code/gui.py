from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtGui
import sys 


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        super(Window, self).__init__()
        self.setFixedSize(300, 150)
        # set the title 
        self.setWindowTitle("WorkMode")
        


        # creating a push button 
        self.button = QPushButton("🔆", self) 

        # setting geometry of button 
        self.button.setGeometry(110, 55, 80, 40) 

        # setting checkable to true 
        self.button.setCheckable(True) 
  
        # setting calling method by button 
        self.button.clicked.connect(self.changeColor) 
  
        # setting default color of button to light-grey 
        self.button.setStyleSheet("background-color : red") 
  
        # show all the widgets 
        self.update() 
        self.show() 
  

    def start_program(self):
        ##Fill the other modules and functions here (working mode)
        print("Hello world")
    
    def end_program(self):
        ##Fill the other modules and functions here (back)
        print("Bye world")

    # method called by button 
    def changeColor(self): 
  
        # if button is checked 
        if self.button.isChecked(): 
            self.start_program()
            # setting background color to light-blue 
            self.button.setStyleSheet("background-color : lightgreen")
            self.button.setText("💼")

  
        # if it is unchecked 
        else: 
            self.end_program()
            # set background color back to light-grey 
            self.button.setStyleSheet("background-color : red")
            self.button.setText("🔆")
    
  
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 