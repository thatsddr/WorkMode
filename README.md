# venus
python mac app for the ID brief

## Requirements

This project requires python 3.8.6, MacOS Catalina 10.15.7 and the libraries cited in the requirements.txt file.

Once you're sure that python 3.8.6 is installed run the command 
`pip3 install -r requirements.txt`

## Testing

At this point you're ready to check if the program runs by running the command
`python3 code/WorkMode.py`
But BE CAREFUL: Save your current configuration with "🔆>Preferences>Save as Normal Mode".
Manually modifying the settings.json file before the first run to remove apps that are not installed on the machine is adviced.

## Building the app

To build the app, first install py2app with the command
`pip3 install py2app`

Then, symply run
`python3 setup.py py2app`

At this point you will be able to run the app with all its functionalities from ./dist/WorkMode.app/Contents/WorkMode, while only the background will change if you open it by clicking on WorkMode.app.


## Problems

For some reason, the app only works properly when launched with sudo privileges, otherwise it won't change the dock. If you have any idea why this happens, please let us know!

### What has been tryed

We’ve tried to use previous versions of python (3.6.x and 3.7.x) as well as older versions of py2app (0.21, 0.20, 0.19 and 0.12) and PyInstaller. Nothing worked.

## Known Issues

When turing off the DnD mode, the icon in the top-right corner of the mac (the Notification Center Icon) doesn not become black again but stays gray.
Having the DnD mode to turn on/off instantly wasn't however our plan, but we planned to have a pomodoro timer and DnD mode synced with it, but that's no longer to be realized in the MVP.

