from tkinter import *
import tkinter

def open_client_listbox():
    window = tkinter.Tk()
    window.title("Client list")
    

    frame = tkinter.Frame(window)
    frame.pack(padx=10, pady=10)

    select_client_button = tkinter.Button(frame, text="Select Client")
    select_client_button.grid(row=1, column=0)

    Lb1 = Listbox(frame)
    Lb1.grid(row=0, column=0)


    """
    Inserting clients to the listbox.
    clients list will be replaced by the actualy list of clients from DB
    """
    clients = ["Petr", "Jana", "Vera", "Tom"]
    list_order = 0
    for client in clients:
        Lb1.insert(list_order, client)
        list_order+=1

    window.mainloop()

open_client_listbox()