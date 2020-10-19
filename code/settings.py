import os
import subprocess
import json

def openSettings():
    """ This function opens the settings.json in textEdit """
    file = "settings.json"
    subprocess.call(['open', '-a', 'TextEdit', file])

def getSetting(arg):
    """ This function takes 1 arg and returns the associated setting item """
    with open("settings.json", "r") as s:
        res = json.load(s)
        s.close()
    return res[arg]

def updtSettings(arg,data):
#Your code here
