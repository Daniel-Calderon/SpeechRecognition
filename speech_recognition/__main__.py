# Names: Daniel Calderon, Terra Fenton, Nancy Gomez

import speech_recognition as sr
import webbrowser
import os
import subprocess

r = sr.Recognizer()

# The microphone will be the source of our audio
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    # sets the threshold to a good value automatically.
    with m as source: r.adjust_for_ambient_noise(source)
    
    # Sets the sensitivity of the recognizer depending on the noise level of the room
    # (so louder values means there is a louder room)
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
                #Google Website
                if ("chrome" in value or "Chrome" in value or "Google" in value or "google" in value ):
                    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com")
                #Apple Website
                elif ("apple" in value or "Apple" in value):
                    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://apple.com")
				#Yahoo Website
                elif ("yahoo" in value or "Yahoo" in value) :
                    webbrowser.open("http://yahoo.com")
                #NotePad
                elif (("word" in value) or ("text" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Notes.app"])
                #Apple texting
                elif(("message" in value) or ("text message" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Messages.app"])
                #Steam
                elif("Steam" in value):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Steam.app"])
                    print "Goes here"
                #League
                elif (("LOL" in value) or ("League" in value) or ("League of Legends" in value)):
                    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/League of Legends.app"])
       
        # if the value (sound) wasn't recognizable, print an error message
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        # if there is an error with the actual API, print an error message
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            
# this exception takes care of ending the program when the user enters Ctrl + C, doesn't give an error
except KeyboardInterrupt:
    pass
