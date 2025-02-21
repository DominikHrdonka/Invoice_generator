import tkinter
from tkinter import ttk
from rws import rws
from en import en
from summary import (
    open_summary,
)
from clients import open_clients
import sqlite3
import shared

# GUI
window = tkinter.Tk()
window.title("Invoice generator form")
window.geometry("400x200")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

#Labels and entry fields
choose_invoice_label = tkinter.Label(frame, text="Choose invoice:")
choose_invoice_label.grid(row=0, column=0, columnspan=1)

rws_invoice_button = tkinter.Button(frame, text= "RWS Invoice", command= rws)
rws_invoice_button.grid(row=1, column=0, padx=5)

en_invoice_button = tkinter.Button(frame, text= "English Invoice", command= en)
en_invoice_button.grid(row=1, column=1)

open_summary_button = tkinter.Button(frame, text="Open summary", command= open_summary)
open_summary_button.grid(row=2, column=0, pady=10, sticky="news", columnspan=2)

clients_button = tkinter.Button(frame, text="Clients", command=open_clients)
clients_button.grid(row=3, column=0, pady=10, sticky= "news", columnspan=2)

#Creating database for invoices
with sqlite3.connect(shared.invoices_db_path) as connection:
#object of DB that handles all the communication with the DB
    cursor = connection.cursor()

    #CREATING TABLE in the DB
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS invoices_list (id INTEGER PRIMARY KEY, invoice_number TEXT, paid TEXT, issued_on TEXT, client TEXT, price REAL);"
        )
#Creating database for clients    
with sqlite3.connect(shared.clients_db_path) as connection:
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS client_list (id INTEGER PRIMARY KEY, name TEXT, email TEXT, hourly_rate INTEGER);"
    )

window.mainloop()