

# look up what .config does for tk
#if you want to pass in information:
# command =  lambda: func(argument)

from Tkinter import *
from PIL import Image, ImageTk

# creates a window
window = Tk();

# here is where all the listening code should go
def listen():
	window.destroy();

# Opens the image of a mic for the interface
image = Image.open('Microphone-icon.png');
image = ImageTk.PhotoImage(image);

# Places the button on the window, gives it a command, and adds the image
B = Button(window, command = listen, image = image).pack();

# Runs and opens the window
window.mainloop();

