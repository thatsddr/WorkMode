import subprocess
import json

def openSettings():
    ''' This function opens the settings.json in textEdit '''
    file = "settings.json"
    subprocess.call(['open', '-a', 'TextEdit', file])

def loadAll():
    '''returns all of the settings'''
    try:
        with open("settings.json", "r") as s:
            res = json.load(s)
            s.close()
        return res
    except:
        with open("settings.json", "w+") as s:
            default = {'normalBG': None, 'workBG': None, 'normalDock' : None, 'workDock' : None, "apps": ["/Applications/Notion.app"], "mode": "free", "notification": "True"}
            json.dump(default, s)
            s.close()
            return default

def getSetting(arg):
    ''' This function takes 1 arg and returns the associated setting item '''
    try:
        with open("settings.json", "r") as s:
            res = json.load(s)
            s.close()
        return res[arg]
    except:
        return None

def updtSettings(arg,data):
    '''updates one setting in the settings,json file'''
    temp = loadAll()
    try:
        temp[arg] = data
    except:
        return
    with open("settings.json", "w") as file:
        json.dump(temp, file)
    file.close()

def updateAll(data):
    '''updates everything in the settings.json file'''
    with open("settings.json", "w") as file:
        json.dump(data, file)
    file.close()

