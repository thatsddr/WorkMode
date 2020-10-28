import subprocess
import json

def openSettings():
    ''' This function opens the settings.json in textEdit '''
    file = "settings.json"
    subprocess.call(['open', '-a', 'TextEdit', file])

def loadAll():
    '''returns all of the settings'''
    with open("settings.json", "r") as s:
        res = json.load(s)
        s.close()
    return res

def getSetting(arg):
    ''' This function takes 1 arg and returns the associated setting item '''
    with open("settings.json", "r") as s:
        res = json.load(s)
        s.close()
    return res[arg]

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

