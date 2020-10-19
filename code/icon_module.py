from PyQt5.QtGui import *

def makeicon(color):
    pic = QPixmap(100,100)
    pic.fill(QColor(color))
    return pic

