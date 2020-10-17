from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QThread, pyqtSignal
import sys 
import musik
import beepy
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND

normalBG = "/System/Library/Desktop Pictures/Catalina.heic"
workBG = "/System/Library/Desktop Pictures/Mojave.heic"

normalDock = ['/Applications/Safari.app', '/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/iTerm.app', '/Applications/Slack.app', '/Applications/Notion.app']
workDock = ['/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/Xcode.app', '/Applications/zoom.us.app', '/Applications/Discord.app',  '/Applications/Slack.app',  '/System/Applications/Reminders.app', '/Applications/iTerm.app', '/System/Applications/Stocks.app']


class MyThread(QThread):
    def switchMode(self, d, bg, dndOn):
        self.DnD = DND()
        self.dock = customDock()
        self.back = Background()
        self.back.change(bg)
        self.dock.removeAll()
        self.dock.addMultiple(reversed(d))
        self.dock.save()
        if dndOn:
            self.DnD.turnOn()
        else:
            self.DnD.turnOff()
        #your function

    def web(self):
        musik.webbrowsers("https://www.youtube.com/watch?v=kg-xtouq3oc&list=RDEMB4pXSfqexQjAYE27XBWebA&start_radio=1","http://stackoverflow.com")


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
        
        self.thread = MyThread()
        self.thread.web()
        self.thread.switchMode(workDock, workBG, True)
        
    
    def end_program(self):
        ##Fill the other modules and functions here (back)
        print("Bye world")
        self.thread = MyThread()
        self.thread.switchMode(normalDock, normalBG, False)


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