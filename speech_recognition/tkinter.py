# Names: Daniel Calderon, Terra Fenton, Nancy Gomez

# look up what .config does for tk
#if you want to pass in information:
# command =  lambda: func(argument)


from Tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import sys
import webbrowser
import os
import subprocess
from docx import Document
from docx.shared import Inches
import time
r = sr.Recognizer()

# The microphone will be the source of our audio
m = sr.Microphone()

#os.system("say Welcome to speech Recognition")

# here is where all the listening code should go
def listen():

    try:
        os.system("say Adjusting noise levels")

        #warnings.filterwarnings("ignore")

        #sets the threshold to a good value automatically.
        with m as source: r.adjust_for_ambient_noise(source)

        # Sets the sensitivity of the recognizer depending on the noise level of the room
		# (so louder values means there is a louder room)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        os.system("say Listening")
        time.sleep(0.2)
        with m as source: audio = r.listen(source)
        os.system("say Understood. One second while I interpret it")
        time.sleep(0.3)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                os.system("say You said{}".format(value).encode("utf-8"))
                print("You said {}".format(value).encode("utf-8"))
            #Chrome Website
            if ("chrome" in value or "Chrome" in value):
                webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com")
            #Google Search
            if ("Google" in value or "Google search" in value or "google" in value):
                value = format(value).encode("utf-8").replace("Google", "")
                value =format(value).encode("utf-8").replace("search", "")
                value =format(value).encode("utf-8").replace("google", "")
                print("***************")
                print value
                webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://google.com/webhp?hl=en#hl=en&q=" + format(value).encode("utf-8"))
            #Apple Website
            elif (("apple" in value) or ("Apple" in value)):
                webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open("http://apple.com")
            #Yahoo Website
            elif (("yahoo" in value) or ("Yahoo" in value)) :
                webbrowser.open("http://yahoo.com")
            #Disney Store
            elif ("Disney store" in value or "Disney" in value):
                webbrowser.open("http://www.disneystore.com")
            #NotePad
            elif (("word" in value) or ("text" in value)):
                document = Document()
                os.system("say Say whatever you need to say.")
                os.system("say If you wish to restart, please say START AGAIN PYTHON")
                with m as source: audio = r.listen(source)
                try:
                    value = r.recognize_google(audio)
                    if(("Start again python" in value) or ("start again python" in value)):
                        with m as source: audio = r.listen(source)
                        try:
                            value = r.recognize_google(audio)
                            print value
                        except sr.UnknownValueError:
                            os.system("say Didnt catch that")

                    else:
                        document.add_paragraph(value)
                        document.save(value + ".docx")
                        print("******************************")
                        print("Enter name of file")
                        print("******************************")
                        with m as source: audio = r.listen(source)
                        try:
                            value = r.recognize_google(audio)
                            print ("Path is "+ value+".docx")
        
                            path = format(value).encode("utf-8")+".docx"
                            document.save(path)
                            open(path)
                        except sr.UnknownValueError:
                            os.system("say Didnt catch that")

                except sr.UnknownValueError:
                    os.system("say Oops! Didn't catch that")

            #Apple texting
            elif(("message" in value) or ("text message" in value)):
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Messages.app"])
            #Steam
            elif(("Steam" in value) or ("steam" in value)):
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Steam.app"])
            #League
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
            #League
            elif (("LOL" in value) or ("League" in value) or ("League of Legends" in value)):
                subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/League of Legends.app"])
            #Close Code
            elif(("close" in value) or ("exit" in value)):
                raise SystemExit
            else:
                os.system("say Could not find a command")
                time.sleep(.4)

        # if the value (sound) wasn't recognizable, print an error message
        except sr.UnknownValueError:
            os.system("say Oops! Didn't catch that")
        # if there is an error with the actual API, print an error message
        except sr.RequestError as e:
            os.system("say Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

    # this exception takes care of ending the program when the user enters Ctrl + C, doesn't give an error
    except KeyboardInterrupt:
        pass


#window.destroy()

#***************************************************************************************************************

# creates a window
window = Tk()

# Opens the image of a mic for the interface
imag = Image.open('Microphone-icon.png').resize((124,124))
imag = ImageTk.PhotoImage(imag)

# Places the button on the window, gives it a command, and adds the image
B = Button(window, command = listen, image = imag).pack()

# Runs and opens the window
window.mainloop()