import webbrowser
from time import sleep
import beepy
#url_music = URl for the music 
#url_work = Work website

def webbrowsers(url_music,url_work):
        webbrowser.open_new(url_music)
        beepy.beep(6)
        webbrowser.open_new_tab(url_work)

#ecample call
#webbrowsers("https://www.youtube.com/watch?v=kg-xtouq3oc&list=RDEMB4pXSfqexQjAYE27XBWebA&start_radio=1","http://stackoverflow.com")
