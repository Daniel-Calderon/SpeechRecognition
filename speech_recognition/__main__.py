# Names: Daniel Calderon, Terra Fenton, Nancy Gomez

import speech_recognition as sr
#import a
import webbrowser
import os
import subprocess
from docx import Document
from docx.shared import Inches
r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print("You said {}".format(value).encode("utf-8"))
                #Google Websit
                if ("chrome" in value or "Chrome" in value or "Google" in value or "google" in value ):
                    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com")
                #Apple Websit
                elif ("apple" in value or "Apple" in value):
                    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://apple.com")

                elif ("yahoo" in value or "Yahoo" in value) :
                    webbrowser.open("http://yahoo.com")
                #NotePad
                elif (("word" in value) or ("text" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Microsoft Word.app"])
                    #subprocess.kill(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Microsoft\Word.app"])
                    
                #Apple texting
                elif(("message" in value) or ("text message" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Messages.app"])
                #Steam
                elif("Steam" in value):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Steam.app"])
                    print "Goes here"
                elif (("LOL" in value) or ("League" in value) or ("League of Legends" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/League of Legends.app"])
            else: # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
