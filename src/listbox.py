from tkinter import (ttk)
import tkinter

def open_client_listbox(callback):

    def select_client():
        #Save clicked item as selected_client variable in shared.py
        client_listbox_root.destroy()
        callback()

    
    #GUI
    client_listbox_root = tkinter.Tk()
    client_listbox_root.title("Choose client")
    
    frame = tkinter.Frame(client_listbox_root)
    frame.pack(padx=10, pady=10)

    select_client_button = tkinter.Button(frame, text="Select Client", command=select_client)
    select_client_button.grid(row=1, column=0)

    treeview_column = ("client")
    client_treeview = ttk.Treeview(frame, columns=treeview_column, show="headings")
    client_treeview.grid(row=0, column=0, pady=20, padx=10)
    client_treeview.heading('client', text="")

    """
    Inserting clients to the treeview.
    clients list will be replaced by the actualy list of clients from DB
    """
    clients = ["Petr", "Jana", "Vera", "Tom"]
    for client in clients:
        #When the database exists, we need to set the uniqude identifier to be reflected in treeviw
        client_treeview.insert("", 0, values=client)

    client_listbox_root.mainloop()

