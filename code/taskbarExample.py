import rumps
import sys 
import musik
import beepy
import settings
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND
from ApplicationModule import Application
from PyQt5.QtCore import Qt,QThread, pyqtSignal
import json

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
        self.config={'normalBG': None,
                    'workBG': None,
                    'normalDock' : None,
                    'workDock' : None}
        self.loadSettigns()
        self.work = rumps.MenuItem("Work Mode", callback=self.switchMode)
        self.saveWM = rumps.MenuItem("Save As WorkMode", callback=self.saveW)
        self.saveNM = rumps.MenuItem("Save As NormalMode", callback=self.saveN)
        self.osettings = rumps.MenuItem("Open Settings", callback=settings.openSettings)
        self.menu = [self.work, self.saveNM, self.saveWM, self.osettings]
        self.title = "🔆"
    
    def loadSettigns(self):
        res = None
        try:
            with open("settings.json", "r") as s:
                res = json.load(s)
            s.close()
            for t in ["normal", "work"]:
                if self.isSaved(t):
                    self.config[t+"Dock"] = res[t+"Dock"]
                    self.config[t+"BG"] = res[t+"BG"]
                else:
                    self.config[t+"Dock"] = None
                    self.config[t+"BG"] = None
        except:
            self.config["normalBG"] = None
            self.config["workBG"] = None
            self.config["normalDock"] = None
            self.config["workDock"] = None

    def isSaved(self, type):
        if type not in ["normal", "work"]:
            raise Exception
        res = None
        try:
            with open("settings.json", "r") as s:
                res = json.load(s)
            s.close()
            if res[type + "BG"] and res[type + "Dock"]:
                return True
            else:
                return False
        except:
            return False
    
    def saveW(self, _):
        self.config["workDock"] = customDock().listAll()
        self.config["workBG"] = Background().getPath()
        self.save()
    
    def saveN(self, _):
        self.config["normalDock"] = customDock().listAll()
        self.config["normalBG"] = Background().getPath()
        self.save()
    
    def save(self):
        with open("settings.json", "w") as file:
            json.dump(self.config, file)
        file.close()
    
    def start_program(self):
        self.thread = MyThread()
        #self.thread.web()
        self.thread.switchMode(self.config['workDock'], self.config['workBG'], True)
        self.thread.open('/Applications/Notion.app', True)
        self.title = "💼"
        rumps.notification(title=self.name, subtitle="You are now in work mode", message="")
        
    def end_program(self):
        self.thread = MyThread()
        self.thread.switchMode(self.config['normalDock'], self.config['normalBG'], False)
        self.thread.open('/Applications/Notion.app', False)
        self.title = "🔆"
        rumps.notification(title=self.name, subtitle="You are now in normal mode", message="")
    
    def switchMode(self, sender):
        if self.isSaved('work') and self.isSaved('normal'):
            if sender.state == 0:
                self.start_program()
            elif sender.state == 1:
                self.end_program()
            sender.state = not sender.state
        else:
            rumps.notification(title=self.name, subtitle="Please, set both modes", message=f"Work mode set: {self.isSaved('work')}\nNormal mode set: {self.isSaved('normal')}")

if __name__ == "__main__":
    taskBarApp("MacMode").run()