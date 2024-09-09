from tkinter import *
import tkinter


window = tkinter.Tk()
window.title("Client list")
window.geometry("300x300")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady= 10)

Lb1 = Listbox(frame)
Lb1.pack()

"""
Inserting clients to the listbox.
clients list will be replaced by the actualy list of clients from DB
"""
clients = ["Petr", "Jana", "Vera", "Tom"]
order = 0
for client in clients:
    Lb1.insert(order, client)
    order+=1

window.mainloop()