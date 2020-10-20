from setuptools import setup

APP = ['code/main.py']
DATA_FILES = ['code/settings.json']
OPTIONS = {'argv_emulation': True, 'plist': {'LSUIElement': True,}, 'includes':['rumps', 'pyobjc', 'PyQt5','osascript','webbrowser']}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)