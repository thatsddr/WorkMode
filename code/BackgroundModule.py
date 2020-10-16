import osascript
from time import sleep
from os.path import isfile

class Background():
    '''Simple class to change background'''
    def __init__(self):
        '''gets the path of the current background, when it changes the value of the previous background is stored in another variable'''
        self._PREVIOUS = ''
        self._CURRENT = osascript.run('tell application "Finder" to get posix path of (get desktop picture as alias)')[1]

    def change(self, path):
        '''sets the background if the path is to a file '''
        if isfile(path):
            script = '''tell application "Finder"
            set desktop picture to POSIX file "%s"
            END'''
            res = osascript.run(script%path)
            if res[2] != '':
                return Exception
            sleep(1)
            self._PREVIOUS = self._CURRENT
            self._CURRENT = path
        else:
            return Exception