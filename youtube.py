from Tkinter import *
from pytube import YouTube
import os

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
        yt = YouTube(videoLink.get())
        yt.set_filename(videoName.get())
        video = yt.get(videoType.get(),videoQuality.get())
        video.download(desktopPath)
    end = Button(master,text="Enter(file will download to dekstop)",width =30,command = callback)
    end.pack()
    mainloop()
def run():
    getVideo()
