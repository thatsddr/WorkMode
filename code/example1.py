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

a = "/System/Library/Desktop Pictures/Catalina.heic"
set_desktop_background(a)

time.sleep(1)

normal = ['/Applications/Safari.app', '/Applications/Google Chrome.app', '/Applications/Visual Studio Code.app', '/Applications/iTerm.app', '/Applications/Slack.app', '/Applications/Notion.app']

dock = customDock()
dock.removeAll()
dock.addMultiple(reversed(normal))
dock.save()