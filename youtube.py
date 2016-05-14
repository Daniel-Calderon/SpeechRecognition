from Tkinter import *
from pytube import YouTube
import os
import ttk
def getVideo():
    master = Tk()
    desktopPath = os.path.expanduser("~/Desktop")

    videoLink = Entry(master)
    videoLink.pack()
    videoLink.focus_set()
    videoLink.insert(0,"Enter youtube link for video")

    videoQuality  = Entry(master)
    videoQuality.pack()
    videoQuality.focus_set()
    videoQuality.insert(0,"Enter youtube Quality")

    videoType  = Entry(master)
    videoType.pack()
    videoType.focus_set()
    videoType.insert(0,"Enter video type")

    videoName  = Entry(master)
    videoName.pack()
    videoName.focus_set()
    videoName.insert(0,"File name")
    def callback():
        try:
            yt = YouTube(videoLink.get())
            try:
                yt.set_filename(videoName.get())
            except:
                os.system("say could not get file name")
            try:
                video = yt.get(videoType.get(),videoQuality.get())
            except:
                os.system("say Could not find proprt video quality")
            try:
                video.download(desktopPath)
            except:
                os.system("say Could not get donwload path")
        except:
            os.system("say Invaid link")

    end = Button(master,text="Enter(file will download to dekstop)",width =30,command = callback)
    end.pack()
    mainloop()
def run():
    getVideo()
