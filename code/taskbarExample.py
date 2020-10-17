import rumps

#example of taskbar app, the reset butto does not work for some reason

class taskBarApp(rumps.App):
    def __init__(self, name):
        self.config = {
            "app_name": name,
            "break_message": "Time is up! Take a break :)",
            "interval": 7
        }
        super(taskBarApp, self).__init__(name)
        self.timer = rumps.Timer(self.on_tick, 1)
        self.interval = self.config["interval"]
        self.start = rumps.MenuItem("Start", callback = self.startFunc)
        self.reset = rumps.MenuItem("Reset", callback=self.resetFunc)
        self.menu = [self.start, self.reset]
        self.resetFunc()
    
    def resetFunc(self):
        self.timer.count = 0
        self.timer.stop()
        self.title = "🍅"
        self.menu['Start'].title = "Start"
        self.reset.set_callback(None)

    def startFunc(self, sender):
        if sender.title.lower() == 'start':
            self.timer.count = 0
            self.timer.end = self.interval
            self.timer.start()
            sender.title = 'Pause'
        elif sender.title.lower() == 'pause':
            self.timer.stop()
            sender.title = 'Continue'
            self.reset.set_callback(self.resetFunc)
        elif sender.title.lower() == 'continue':
            self.timer.start()
            sender.title = 'Pause'
            self.reset.set_callback(None)
        
    def on_tick(self, sender):
        time_left = sender.end - sender.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        if mins == 0 and time_left < 0:
            rumps.notification(title=self.config["app_name"], subtitle=self.config["break_message"], message='')
            self.resetFunc()
        else:
            '''self.reset.set_callback(None)'''
            self.title = '{:02d}:{:02d}'.format(mins, secs)
        sender.count += 1

if __name__ == "__main__":
    taskBarApp("Helo").run()