from setuptools import setup

APP = ['code/main.py']
DATA_FILES = ['settings.json']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['docklib','pyobjc','PyQt5','osascript','rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)