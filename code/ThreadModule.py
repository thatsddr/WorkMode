import settings
import webbrowser
from ApplicationModule import Application
from DockModule import customDock
from BackgroundModule import Background
from DNDModule import DND

class Thread():
    
    def open(self, wantToOpen):
        #opens apps (from settings)
        self.paths = settings.getSetting('apps')
        for self.path in self.paths:
            self.app = Application(self.path)
            if wantToOpen:
                self.app.open()
            else:
                self.app.close()
    
    def switchMode(self, d, bg):
        #changes background, dock and DND
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
            pass
        
        self.backg = Background()
        self.backg.change(bg)
        self.dock = customDock()
        self.dock.removeAll()
        self.dock.addMultiple(reversed(d))
        self.dock.save()
    
    def web(self):
        #Opens the Links (in settings) in Webbrowser
        self.links = settings.getSetting('Links')
        for self.link in self.links:
            webbrowser.open_new(self.link)
        
