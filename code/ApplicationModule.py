import os
import osascript
import psutil

class Application():
    '''open and close applications easily with 2 methods:
    open() and close(), after passing the path to the app as only argument'''
    def __init__(self, path):
        if os.path.isdir(path) and path[-4:] == ".app":
            self.path = path
            self.name = path[path.rindex("/") + 1:-4]
        else:
            raise Exception
    
    def isOpen(self):
        return self.name in (p.name() for p in psutil.process_iter())

    def open(self):
        if not self.isOpen():
            os.system("open " + self.path)
    
    def close(self):
        if self.isOpen():
            osascript.run('quit app "' + self.name + '"')