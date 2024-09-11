import tkinter
from tkinter import (ttk)
import sqlite3

def open_clients():
    def main():

        #Functions

        def new_client():
            add_client_root = tkinter.Tk()
            add_client_root.title('New Client')
            add_client_root.geometry('300x200')

            add_client_frame = ttk.Frame(add_client_root)
            add_client_frame.pack(padx=10, pady=10)

            name_label = tkinter.Label(add_client_frame, text=('Name:'))
            name_label.grid(row=0, column=0)
            name_entry = tkinter.Entry(add_client_frame)
            name_entry.grid(row=0, column=1)

            email_label = tkinter.Label(add_client_frame, text='Email: ')
            email_label.grid(row=1, column=0)
            email_entry = tkinter.Entry(add_client_frame)
            email_entry.grid(row=1, column=1)

            hourly_rate_label = tkinter.Label(add_client_frame, text='Hourly rate: ')
            hourly_rate_label.grid(row=2, column=0)
            hourly_rate_entry = tkinter.Entry(add_client_frame)
            hourly_rate_entry.grid(row=2, column=1)

            add_client_button = tkinter.Button(add_client_frame, text='Add Client')
            add_client_button.grid(row=3, column=0, columnspan=2, sticky='news', pady=15)

            



            #Temporary variables
            name = "John"
            email = "John@gmail.com"
            hourly_rate = 350

            with sqlite3.connect('clients.db') as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO client_list (name, email, hourly_rate) VALUES (?, ?, ?);", (name, email, hourly_rate)
                )


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

        new_client_button = tkinter.Button(frame, text="New Client", command=new_client)
        new_client_button.grid(row=1, column=0, padx=5, pady=5, sticky='news')

        root.mainloop()
    main()