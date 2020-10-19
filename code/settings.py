import os
import subprocess

def openSettings():
    file = "settings.json"
    subprocess.call(['open', '-a', 'TextEdit', file])
