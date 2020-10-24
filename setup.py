from setuptools import setup

APP = ['code/WorkMode.py']
DATA_FILES = ['settings.json']
OPTIONS = {'argv_emulation': True,
            "iconfile": "icon.icns",
            'plist': {
                'LSUIElement': True,
                'CFBundleName': "WorkMode",
                'CFBundleDisplayName': "WorkMode",
                'CFBundleVersion': "0.1.0",
                'CFBundleShortVersionString': "0.1.0",
                'NSHumanReadableCopyright': "Copyright © 2020, Felix Heilingbrunner, Domenico Di Ruocco, All Rights Reserved"
            },
            'includes':['rumps', 'docklib', 'pyobjc', 'PyQt5', 'osascript', 'webbrowser']
}
            


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)