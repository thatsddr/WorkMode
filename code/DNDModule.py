import subprocess

#IMPORTANT: Apparently killall is already a good alternative in unix-based systems since it sends to the apps that it is going to close a SIGTERM signal, but anyways killing the notification center is fine since it is not as important as the dock

class DND():
    """class to manage the DND status of your mac with methods to:
    turn DND on, 
    turn DND Off (this one is buggy),
    schedule DND to go off at some time
    schedule DND to go on at some time
    unschedule everything
    check the DND status"""

    def turnOn(self):
        '''simple method to turn the DND mode on, no bugs known'''
        if self.check() == 0:
            subprocess.Popen(['defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true'], shell=True)
            subprocess.Popen(['defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturbDate -date "`date -u +\"%Y-%m-%d %H:%M:%S +0000\"`"'], shell=True)
            subprocess.Popen(['killall NotificationCenter'], shell=True)

    def turnOff(self):
        '''method to turn the DND mode off, affected by a really annoying bug that lets the icon stay gray, please prefer a scheduled approach for turning off the DND mode when possible'''
        if self.check() == 1:
            subprocess.Popen(['defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean false'], shell=True)
            subprocess.Popen(['killall NotificationCenter'], shell=True)
            # I tried to kill the system UI server to refresh the notification center icon in the menu bar, but even after the refresh it remains gray

    def offAtTime(self, h,m):
        '''method to schedule the automatic shut down of the DND module, acceots two arguments: hours and minutes, to be intented as the hour and minute of the day in which it has to shut down'''
        subprocess.Popen([f"defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui dndEnd -integer {h*60+m}"], shell=True)
        subprocess.Popen(['killall NotificationCenter'], shell=True)

    def onAtTime(self, h,m):
        '''method to schedule the automatic start of the DND module, acceots two arguments: hours and minutes, to be intented as the hour and minute of the day in which it has to start'''
        subprocess.Popen([f"defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui dndStart -integer {h*60+m}"], shell=True)
        subprocess.Popen(['killall NotificationCenter'], shell=True)

    def unschedule(self):
        '''method to unschedule automatic starts or shutdowns, since that behaviour would repeat itself every day otherwise'''
        try:
            subprocess.Popen(['defaults -currentHost delete ~/Library/Preferences/ByHost/com.apple.notificationcenterui dndStart'], shell=True)
        except:
            pass
        try:
            subprocess.Popen(['defaults -currentHost delete ~/Library/Preferences/ByHost/com.apple.notificationcenterui dndEnd'], shell=True)
        except:
            pass
        subprocess.Popen(['killall NotificationCenter'], shell=True)

    def check(self):
        '''method to check the status of the DND mode. returns 0 if off or 1 if on'''
        a = subprocess.check_output(['defaults -currentHost read ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb'], shell=True)
        return int(a.decode("utf-8"))