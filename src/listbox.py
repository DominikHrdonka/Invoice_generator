from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("Client list")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady= 10)


Lb1 = Listbox(window)

Lb1.insert(1, "Jan")
Lb1.insert(2, "Vera")
Lb1.insert(3, "Petr")


window.mainloop()