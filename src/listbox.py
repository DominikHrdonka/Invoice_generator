from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("Client list")
window.geometry("300x300")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady= 10)


Lb1 = Listbox(frame)
Lb1.pack()

Lb1.insert(1, "Jan")
Lb1.insert(2, "Vera")
Lb1.insert(3, "Petr")


window.mainloop()