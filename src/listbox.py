from tkinter import (ttk)
import tkinter
import shared
from databases import fetch_items_from_db

def open_client_listbox(callback):

    def select_client():
        #Save clicked item as selected_client variable in shared.py -- it uses DB iid
        shared.selected_client = client_treeview.selection()
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
    Displaying clients to the treeview.
    clients list will be replaced by the actualy list of clients from DB
    """
    clients = fetch_items_from_db(shared.clients_db_path, 'client_list')

    for client in clients:
        client_id = client[0]
        client_treeview.insert("", 0, iid=client_id, values=(client[1], client[2]))

    client_listbox_root.mainloop()

