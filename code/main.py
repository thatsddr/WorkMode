import rumps
import sys 
import beepy
import settings
import webbrowser
import settings
import json
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND
from ApplicationModule import Application
from PyQt5.QtCore import Qt,QThread, pyqtSignal

#yes, I wanted to import this from gui but for some reason it didn't work

class MyThread(QThread):
    #opens apps (from settings)
    def open(self, wantToOpen):
        self.paths = settings.getSetting('apps')
        for self.path in self.paths:
            self.app = Application(self.path)
            if wantToOpen:
                self.app.open()
            else:
                self.app.close()

    def switchMode(self, d, bg):
        self.DnD = DND()
        self.mode = settings.getSetting('mode')
        if self.mode == "free":
            self.DnD.turnOn()
            d = settings.getSetting('workDock')
            bg = settings.getSetting('workBG')
        elif self.mode == "work":
            self.DnD.turnOff()
            d = settings.getSetting('normalDock')
            bg = settings.getSetting('normalBG')
        else:
            Exception
        
        
        self.dock = customDock()
        self.backg = Background()
        self.backg.change(bg)
        self.dock.removeAll()
        self.dock.addMultiple(reversed(d))
        self.dock.save()
    #Opens the Links (in settings) in Webbrowser
    def web(self):
        self.links = settings.getSetting('Links')
        for self.link in self.links:
            webbrowser.open_new(self.link)
        

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
        self.osettings = rumps.MenuItem("Open Settings", callback=self.settingsCallback)
        self.menu = [self.work, self.saveNM, self.saveWM, self.osettings]
        self.title = self.getmode()
    #The right label is shown now. (after reboot as well) but to get out you first need to enter workmode (again)
    def getmode(self):
        self.mode = settings.getSetting('mode')
        if self.mode == "free":
            self.work.state = 0
            return "🔆"
        else: 
            self.work.state = 1
            return "💼"

    def loadSettigns(self):
        res = None
        try:
            res = settings.loadAll()
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
        
        if not hasattr(res, "mode"):
            settings.updtSettings("mode", "free")
        if not hasattr(res, "Links"):
            settings.updtSettings("mode", [])
        if not hasattr(res, "mode"):
            settings.updtSettings("apps", [])
            
    def settingsCallback(self, _):
        settings.openSettings()

    def isSaved(self, type):
        if type not in ["normal", "work"]:
            raise Exception
        res = None
        try:
            res = settings.loadAll()
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
        settings.updtSettings("normalBG", self.config["normalBG"])
        settings.updtSettings("workBG", self.config["workBG"])
        settings.updtSettings("normalDock", self.config["normalDock"])
        settings.updtSettings("workDock", self.config["normalDock"])
    
    def start_program(self):
        self.thread = MyThread()
        self.thread.switchMode(self.config['workDock'], self.config['workBG'])
        self.thread.open(True)
        self.thread.web()
        self.title = "💼"
        settings.updtSettings('mode',"work")
        rumps.notification(title=self.name, subtitle="You are now in work mode", message="")
        
    def end_program(self):
        self.thread = MyThread()
        self.thread.switchMode(self.config['normalDock'], self.config['normalBG'])
        self.thread.open(False)
        self.title = "🔆"
        settings.updtSettings('mode',"free")
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