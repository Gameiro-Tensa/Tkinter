# ich will nochmal Tkinter durchgehen

import tkinter as Tk

from tkinter import *

def anzeige():
    myText.set('Bravo ihr habt geschaft zu klicken')

fen = Tk()

myText = StringVar()
myText.set('Hello Welt')

textLabel = Label(fen, textvariable=myText)
textLabel.pack()

btn = Button(fen, text='klicken Sie hier', command=anzeige())
btn.pack

fen.mainloop()