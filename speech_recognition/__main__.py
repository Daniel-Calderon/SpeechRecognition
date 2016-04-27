# Names: Daniel Calderon, Terra Fenton, Nancy Gomez

import speech_recognition as sr
import sys
import webbrowser
import os
import subprocess
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
                #Yahoo
                elif ("yahoo" in value or "Yahoo" in value) :
                    webbrowser.open("http://yahoo.com")
                #Disney Store
                elif ("Disney store" in value or "Disney" in value) :
                    webbrowser.open("http://www.disneystore.com")
                #NotePad
                elif (("word" in value) or ("text" in value)):
                        subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Notes.app"])
                #Apple texting
                elif(("message" in value) or ("text message" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Messages.app"])
                #Steam
                elif(("Steam" in value) or ("steam" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Steam.app"])
                #League of Legends
                elif (("LOL" in value) or ("League" in value) or ("League of Legends" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/League of Legends.app"])
                #Photo Both
                elif(("Booth" in value) or ("booth" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Photo Booth.app"])
                #Pictures
                elif(("Photo" in value) or ("photo" in value) or ("picture" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Photos.app "])
                #Skype
                elif(("Skype" in value) or ("skype" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Skype.app"])
                #iTunes
                elif(("eye Tunes" in value) or ("iTunes" in value) or ("Tunes" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/iTunes.app"])
                #Calculator
                elif(("calculator" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Calculator.app"])
                #Close Code
                elif(("close" in value) or ("Lowe's" in value)):
                    raise SystemExit

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
