# ich will nochmal Tkinter durchgehen

from tkinter import *

def anzeige():
    myText.set('Bravo ihr habt geschaft zu klicken')

# creating the tkinter windows
fen = Tk()

# setting the minimun size of windows
fen.minsize(200, 250)

myText = StringVar()
myText.set('Hello Welt')

textLabel = Label(fen, textvariable=myText)
textLabel.pack()

btn = Button(fen, text='klicken Sie hier', command=anzeige)
btn.pack(side= TOP)

fen.mainloop()