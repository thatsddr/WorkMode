from docklib import Dock
import os

#docklib on github: https://github.com/homebysix/docklib/blob/pypi/docklib/docklib.py

class customDock(Dock):
    def __init__(self):
        super().__init__()

    def add(self, path):
        '''add an app to the left side of the dock by specifying the path to an app, or a folder to the right part by specifying the path to a folder'''
        section=""
        if ".app" in path:
            section="persistent-apps"
        else:
            section="persistent-others"
        if path[path.rindex("/"):]:
            self.items[section] = [self.makeDockAppEntry(path.replace("%20", " "))] + self.items[section]
        else:
            print("Not Found")

    def addMultiple(self, paths):
        '''add multiple apps from a list of paths'''
        for path in paths:
            self.add(path)

    def addURL(self, url, label=None):
        '''add one url to the right of the dock'''
        self.items["persistent-others"] = [self.makeDockOtherURLEntry(url, label)] + self.items["persistent-others"]
    
    def addURLs(self,urls):
        '''add multiple urls by a list of objects like this {"url": "string", "label": "string"}'''
        for item in urls:
            self.addURL(item["url"], item["label"])
            
    def remove(self, name, section=None):
        '''remove one item by specifying the name and optionally the section '''
        self.removeDockEntry(name, section)

    def listAll(self, type="apps"):
        '''returns a list of all the apps or others in the dock '''
        if type not in ["apps", "others"]:
            raise Exception
        else:
            li = []
            for i in self.items["persistent-"+type]:
                li.append(i['tile-data']['file-data']['_CFURLString'][7:-1].replace("%20", " "))
            return li
    
    def removeAll(self, type="apps"):
        '''removes everything of one type '''
        if type not in ["apps", "others"]:
            raise Exception
        else:
            items = self.listAll(type)
            for i in items:
                if type=="apps":
                    self.remove(i[i.rindex("/")+1:-4])
                else:
                    self.remove(i[i.rindex("/")+1:])


    