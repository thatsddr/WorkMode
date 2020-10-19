import os
import subprocess

def openSettings():
    """ This function opens the settings.json in textEdit """
    file = "settings.json"
    subprocess.call(['open', '-a', 'TextEdit', file])

def getSetting(arg):
    """ This function takes 1 arg and returns the associated setting item """
