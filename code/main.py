import gui
import taskitem
from multiprocessing import Process

#starts the multithreading

if __name__ == '__main__':
    p1 = Process(target = gui.guipy,args=())
    p1.start()
    p2 = Process(target = taskitem.taskBar,args=())
    p2.start()