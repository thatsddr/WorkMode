from docklib import Dock
import os

#docklib on github: https://github.com/homebysix/docklib/blob/pypi/docklib/docklib.py

class customDock(Dock):
    def __init__(self):
        super().__init__()

    '''add an app to the left side of the dock by specifying the path to an app, or a folder to the right part by specifying the path to a folder'''
    def add(self, path):
        section=""
        if ".app" in path:
            section="persistent-apps"
        else:
            section="persistent-others"
        if path[path.rindex("/"):]:
            self.items[section] = [self.makeDockAppEntry(path)] + self.items[section]
        else:
            print("Not Found")

    '''add multiple apps from a list of paths'''
    def addMultiple(self, paths):
        for path in paths:
            self.add(path)

    '''add one url to the right of the dock'''
    def addURL(self, url, label=None):
        self.items["persistent-others"] = [self.makeDockOtherURLEntry(url, label)] + self.items["persistent-others"]
    
    '''add multiple urls by a list of objects like this {"url": "string", "label": "string"}'''
    def addURLs(self,urls):
        for item in urls:
            self.addURL(item["url"], item["label"])
            
    '''remove one item by specifying the name and optionally the section '''
    def remove(self, name, section=None):
        self.removeDockEntry(name, section)

    '''removes everything of one type '''
    def removeAll(self, type="apps"):
        if type not in ["apps", "others"]:
            raise Exception
        else:
            for i in self.items["persistent-"+type]:
                del i

    '''returns a list of all the apps or others in the dock '''
    def listAll(self, type="apps"):
        if type not in ["apps", "others"]:
            raise Exception
        else:
            li = []
            for i in self.items["persistent-"+type]:
                li.append(i['tile-data']['file-data']['_CFURLString'][7:])
            return li

    