from DockModule import customDock
import subprocess
import time
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""
def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)

a = "/System/Library/Desktop Pictures/Mojave.heic"
set_desktop_background(a)

time.sleep(1)

work = ['/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/Xcode.app', '/Applications/zoom.us.app', '/Applications/Discord.app',  '/Applications/Slack.app',  '/System/Applications/Reminders.app', '/Applications/iTerm.app', '/System/Applications/Stocks.app']

dock = customDock()
dock.removeAll()
dock.addMultiple(reversed(work))
dock.save()