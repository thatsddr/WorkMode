from multiprocessing import Process
#sound generation libary for documentation (https://pypi.org/project/beepy/)
import beepy
import musik

#brings the start of the musik to the multithreading
def func1(url_music,url_work):
    musik.webbrowsers(url_music,url_work)


#func2 makes a extra sound (use at time of blackscreen) (arg: 4:okay, 5:good, 6:best)
def func2(arg):
    arg = int(arg)
    beepy.beep(arg)

#starts the multithreading
if __name__ == '__main__':
    p1 = Process(target = func1,args=("https://www.youtube.com/watch?v=kg-xtouq3oc&list=RDEMB4pXSfqexQjAYE27XBWebA&start_radio=1","http://stackoverflow.com"))
    p1.start()
    p2 = Process(target = func2,args=("6"))
    p2.start()