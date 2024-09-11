import tkinter
from tkinter import (ttk)
import sqlite3

def open_clients():
    def main():
        
        # GUI
        root = tkinter.Tk()
        root.title("Clients")
        root.geometry("600x300")

        frame = tkinter.Frame(root)
        frame.pack(padx=20, pady=10)

        clients_columns = ('name', 'email', 'hourly_rate')
        clients_treeview = ttk.Treeview(frame, columns=clients_columns, show="headings")
        clients_treeview.grid(row=0, column=0)
        clients_treeview.heading('name', text='Name')
        clients_treeview.heading('email', text='E-mail')
        clients_treeview.heading('hourly_rate', text='Hourly rate')

        add_client_button = tkinter.Button(frame, text="Add Client", command=None)
        add_client_button.grid(row=1, column=0, padx=5, pady=5, sticky='news')

        #Functions

        def add_client(name, email, hourly_rate):
            with sqlite3.connect('clients.db') as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO client_list (name, email, hourly_rate) VALUES (?,?,?);" (name, email, hourly_rate)
                )

        root.mainloop()
    main()