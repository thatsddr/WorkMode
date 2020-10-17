import rumps
import sys 
import musik
import beepy
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND
from ApplicationModule import Application
from PyQt5.QtCore import Qt,QThread, pyqtSignal

#yes, I wanted to import this from gui but for some reason it didn't work

class MyThread(QThread):
    def open(self, path, wantToOpen):
        self.path = path
        self.app = Application(self.path)
        if wantToOpen:
            self.app.open()
        else:
            self.app.close()

    def switchMode(self, d, bg, dndOn):
        self.DnD = DND()
        self.dock = customDock()
        self.backg = Background()
        print(bg)
        self.backg.change(bg)
        self.dock.removeAll()
        self.dock.addMultiple(reversed(d))
        self.dock.save()
        if dndOn:
            self.DnD.turnOn()
        else:
            self.DnD.turnOff()
        

    def web(self):
        musik.webbrowsers("https://www.youtube.com/watch?v=kg-xtouq3oc&list=RDEMB4pXSfqexQjAYE27XBWebA&start_radio=1","http://stackoverflow.com")

#from the taskbar icon, change the mode
class taskBarApp(rumps.App):
    def __init__(self, name):
        super(taskBarApp, self).__init__(name)
        self.config={'normalBG' : "/System/Library/Desktop Pictures/Catalina.heic",
                    'workBG' : "/System/Library/Desktop Pictures/Mojave.heic",
                    'normalDock' : ['/Applications/Safari.app', '/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/iTerm.app', '/Applications/Slack.app', '/Applications/Notion.app'],
                    'workDock' : ['/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/Xcode.app', '/Applications/zoom.us.app', '/Applications/Discord.app',  '/Applications/Slack.app',  '/System/Applications/Reminders.app', '/Applications/iTerm.app', '/System/Applications/Stocks.app']}
        self.title = "MacMode"
        self.work = rumps.MenuItem("Work Mode", callback=self.switchMode)
        self.menu = [self.work]
        self.title = "🔆"
    
    def start_program(self):
        self.thread = MyThread()
        #self.thread.web()
        self.thread.switchMode(self.config['workDock'], self.config['workBG'], True)
        self.thread.open('/Applications/Notion.app', True)
        self.title = "💼"
        
    def end_program(self):
        self.thread = MyThread()
        self.thread.switchMode(self.config['normalDock'], self.config['normalBG'], False)
        self.thread.open('/Applications/Notion.app', False)
        self.title = "🔆"
    
    def switchMode(self, sender):
        if sender.state == 0:
            self.start_program()
        elif sender.state == 1:
            self.end_program()
        sender.state = not sender.state

if __name__ == "__main__":
    taskBarApp("MacMode").run()