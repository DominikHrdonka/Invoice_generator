from tkinter import *
import tkinter

def open_client_listbox(callback):

    def select_client():
        #Save clicked item as selected_client variable in shared.py
        client_listbox_root.destroy()
        callback()

    
    #GUI
    client_listbox_root = tkinter.Tk()
    client_listbox_root.title("Client list")
    
    frame = tkinter.Frame(client_listbox_root)
    frame.pack(padx=10, pady=10)

    select_client_button = tkinter.Button(frame, text="Select Client", command=select_client)
    select_client_button.grid(row=1, column=0)

    Lb1 = Listbox(frame, selectmode=BROWSE)
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

    client_listbox_root.mainloop()

