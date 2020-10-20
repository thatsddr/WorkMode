from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QThread, pyqtSignal
import sys 
import musik
import beepy
import settings
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND
from ApplicationModule import Application
import icon_module as im

normalBG = "/System/Library/Desktop Pictures/Catalina.heic"
workBG = "/Users/felixheilingbrunner/Downloads/eBackpack/EXTRAS/#fourthdimension/Rainbow.jpg"

normalDock = ['/Applications/Safari.app',  '/Applications/Notion.app', '/Applications/Slack.app', '/Applications/Discord.app', '/Applications/League of Legends']
workDock = ['/Applications/Google Chrome.app', '/Applications/Slack.app', '/Applications/Visual Studio Code.app', '/Applications/Xcode.app', '/Applications/zoom.us.app',]


class MyThread(QThread):

    #Opens Application -> will turn into for loop that opens all programs from settings.json
    def openApplication(self):
        self.oapp = Application('/Applications/Notion.app')
        self.oapp.open()
 
 #
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
            self.openApplication()
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

        #self.p = self.palette()
        #self.p.setColor(self.backgroundRole(), Qt.red)
        #elf.setPalette(self.p)
        self.setStyleSheet("background : url(image3.png)")

        # creating a push button 
        self.button = QPushButton(" 🔆 ", self) 
        self.settings = QPushButton("⚙️", self)
        # setting geometry of button 
        self.button.setGeometry(110, 55, 80, 40) 
        self.settings.setGeometry(0,0,40,30)

        # setting checkable to true 
        self.button.setCheckable(True) 
  
        # setting calling method by button 
        self.button.clicked.connect(self.changeColor)
        self.settings.clicked.connect(settings.openSettings)
  
        # setting default color of button to light-grey 
        self.button.setStyleSheet("background : url(image2.png); border-style: solid; border-width: 2px; border-color: blue")

        ####Taskbar test

        # Create the icon
        self.icon = QIcon(im.makeicon('yellow'))

# Create the tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

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
            self.button.setStyleSheet("background-image : url(image.png);")
            self.button.setText("💼")
            self.icon = QIcon(im.makeicon('green'))
            self.tray.setIcon(self.icon)

  
        # if it is unchecked 
        else: 
            self.end_program()
            # set background color back to light-grey 
            self.button.setStyleSheet("background : url(image2.png)")
            self.button.setText("🔆")
            self.icon = QIcon(im.makeicon('yellow'))
            self.tray.setIcon(self.icon)
    
    
def guipy(): 
# create pyqt5 app 
    App = QApplication(sys.argv) 
  
# create the instance of our Window 
    window = Window() 
  
# start the app 
    sys.exit(App.exec()) 
