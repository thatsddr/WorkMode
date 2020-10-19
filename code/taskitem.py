import rumps
import settings


"""This is a module that shows a String in the Taskbar (used form gui(main))"""

class taskBarApp(rumps.App):
    def __init__(self, name):
        super(taskBarApp, self).__init__(name)
        self.config={'normalBG': None,
                    'workBG': None,
                    'normalDock' : None,
                    'workDock' : None,
                    'settings' : None}
        self.work = rumps.MenuItem("Work Mode", callback=self.none)
        self.saveWM = rumps.MenuItem("Save As WorkMode", callback=self.none)
        self.saveNM = rumps.MenuItem("Save As NormalMode", callback=self.none)
        self.settings = rumps.MenuItem("Open Settings", callback=self.openSettings)
        self.menu = [self.work, self.saveNM, self.saveWM, self.settings]
        self.title = "🔆"

    def openSettings(self, _):
        settings.openSettings()

    def none(self, _):
        print("no")
    

def taskBar():
    taskBarApp("WorkMode").run()