from DockModule import customDock
from BackgroundModule import Background

b = "/System/Library/Desktop Pictures/Catalina.heic"
a = "/System/Library/Desktop Pictures/Mojave.heic"

normal = ['/Applications/Safari.app', '/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/iTerm.app', '/Applications/Slack.app', '/Applications/Notion.app']
work = ['/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/Xcode.app', '/Applications/zoom.us.app', '/Applications/Discord.app',  '/Applications/Slack.app',  '/System/Applications/Reminders.app', '/Applications/iTerm.app', '/System/Applications/Stocks.app']

def changeMode(d, b):
    dock = customDock()
    back = Background()
    back.change(b)
    dock.removeAll()
    dock.addMultiple(reversed(d))
    dock.save()
    

while True:
    x = input("a = work mode; b = normal mode; q = quit\n")
    if x == "q":
        break
    elif x == "a":
        changeMode(work, a)
    elif x == "b":
        changeMode(normal, b)