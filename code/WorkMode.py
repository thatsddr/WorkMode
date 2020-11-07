import rumps
import settings
from ThreadModule import Thread
from DockModule import customDock
from BackgroundModule import Background
from ApplicationModule import Application

class taskBarApp(rumps.App):
    '''main class'''
    def __init__(self, name):
        super(taskBarApp, self).__init__(name)
        #initialize settings
        self.config={'normalBG': None,
                    'workBG': None,
                    'normalDock' : None,
                    'workDock' : None}
        self.loadSettings()
        #timer config

        self.timerConfig = {
            'interval': 1500,
            "start": "Start Timer",
            "pause": "Pause Timer",
            "continue": "Continue Timer",
            "stop": "Stop Timer"
        }
        self.timer = rumps.Timer(self.on_tick, 1)
        #initialize menu items
        self.work = rumps.MenuItem("Work Mode", callback=self.switchMode, key="M")
        self.saveWM = rumps.MenuItem("Save As Work Mode", callback=self.saveW)
        self.saveNM = rumps.MenuItem("Save As Normal Mode", callback=self.saveN)
        self.osettings = rumps.MenuItem("Open settings.json", callback=self.settingsCallback)
        self.info = rumps.MenuItem("About...", callback=self.showInfo)
        #timer-relevant stuff
        self.playPauseTimer = rumps.MenuItem("Start Timer", callback=self.start_timer)
        self.stopTimer = rumps.MenuItem("Stop Timer", callback=self.stop_timer_callback)
        #menu final structure
        self.menu = [self.work, None, self.playPauseTimer, self.stopTimer, None, {"Preferences": [self.saveNM, self.saveWM, self.osettings]}, None, self.info]
        #initialize the title
        self.title = self.getmode()
        #check if change mode can have a callback
        self.checkSaved()

        self.reset_timer()

    def reset_timer(self):
        self.timer.stop()
        self.timer.count = 0
        self.stopTimer.set_callback(None)
        
    def on_tick(self, sender):
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(title=self.name, subtitle="Take a break", message='')
            self.stop_timer()
            self.stopTimer.set_callback(None)
        else:
            self.stopTimer.set_callback(self.stop_timer_callback)
            self.title = self.getmode() + " - " + '{:02d}:{:02d}'.format(mins, secs)
        sender.count += 1

    def start_timer(self, sender):
        if sender.title.lower().startswith(("start", "continue")):
            if sender.title == self.timerConfig["start"]:
                self.timer.count = 0
                self.timer.end = self.timerConfig['interval']
            self.playPauseTimer.title= self.timerConfig["pause"]
            self.timer.start()
        else:
            self.playPauseTimer.title = self.timerConfig["continue"]
            self.timer.stop()

    def stop_timer(self):
        self.reset_timer()
        self.stopTimer.set_callback(None)
        self.playPauseTimer.title = self.timerConfig["start"]
        self.title = self.getmode()
    
    def stop_timer_callback(self, _):
        self.stop_timer()
    
    def getmode(self):
        '''returns 🔆 if in free mode or 💼 if in workmode'''
        self.mode = settings.getSetting('mode')
        if self.mode == "work":   
            self.work.state = 1
            return "💼"
        else: 
            self.work.state = 0
            return "🔆"

    def showInfo(self, _):
        '''shows info windows'''
        w = rumps.Window(message="WorkMode v0.0.1", default_text="Copyright © 2020 Felix Heilingbrunner & Domenico Di Ruocco, All Rights Reserved.\n\nThis is an alpha version of the product distributed under the Apache-2.0 License.\n\nYou may obtain a copy of the License at:\nhttps://www.apache.org/licenses/LICENSE-2.0", title="About WorkMode", dimensions=(380, 150))
        w._textfield.setSelectable_(False)
        w.run()

    def loadSettings(self):
        '''fetches settings from settings.json file'''
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

    def settingsCallback(self, _):
        '''makes the above function callable by the menu item'''
        settings.openSettings()

    def isSaved(self, type):
        '''checks if the current mode is saved'''
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
    
    def checkSaved(self):
        if self.isSaved("normal") and self.isSaved("work"):
            self.work.set_callback(self.switchMode)
        else:
            self.work.set_callback(None)
    
    def saveW(self, _):
        '''saves the current mode as work mode'''
        self.config["workDock"] = customDock().listAll()
        self.config["workBG"] = Background().getPath()
        self.save()
        #check if change mode can have a callback
        self.checkSaved()
    
    def saveN(self, _):
        '''saves the current mode as normal mode'''
        self.config["normalDock"] = customDock().listAll()
        self.config["normalBG"] = Background().getPath()
        self.save()
        #check if change mode can have a callback
        self.checkSaved()
    
    def save(self):
        '''updates the settings with the mode saved'''
        settings.updtSettings("normalBG", self.config["normalBG"])
        settings.updtSettings("workBG", self.config["workBG"])
        settings.updtSettings("normalDock", self.config["normalDock"])
        settings.updtSettings("workDock", self.config["normalDock"])
    
    #what to do when switching mode and function called from the WorkMode Button

    def start_program(self):
        '''calls everything related to the work mode'''
        self.thread = Thread()
        self.thread.switchMode(self.config['workDock'], self.config['workBG'])
        self.thread.open(True)
        self.thread.web()
        self.title = "💼"
        settings.updtSettings('mode',"work")
        if settings.getSetting('notification')=="True":
            rumps.notification(title=self.name, subtitle="You are now in work mode", message="")
        
    def end_program(self):
        '''calls everything related to the normal mode'''
        self.thread = Thread()
        self.thread.switchMode(self.config['normalDock'], self.config['normalBG'])
        self.thread.open(False)
        self.title = "🔆"
        settings.updtSettings('mode',"free")
        if settings.getSetting('notification')=="True":
            rumps.notification(title=self.name, subtitle="You are now in normal mode", message="")
    
    def switchMode(self, sender):
        '''callable from the menu item, makes the mode switch possible'''
        if self.isSaved('work') and self.isSaved('normal'):
            if sender.state == 0:
                self.start_program()
            elif sender.state == 1:
                self.end_program()
            sender.state = not sender.state
        else:
            rumps.notification(title=self.name, subtitle="Please, set both modes", message=f"Work mode set: {self.isSaved('work')}\nNormal mode set: {self.isSaved('normal')}")

if __name__ == "__main__":
    taskBarApp("WorkMode").run()