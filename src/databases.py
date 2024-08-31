import sqlite3
import os
import tkinter
from tkinter import ttk

def insert_into_db(invoice_number, paid, issued_on, client, price):
    #Connect to DB
    with sqlite3.connect('invoices.db') as connection:
    #object of DB that handles all the communication with the DB
        cursor = connection.cursor()
    #insert into DB table
        cursor.execute("INSERT INTO invoices_list (invoice_number, paid, issued_on, client, price) VALUES (?, ?, ?, ?, ?);", (invoice_number, paid, issued_on, client, price))
        connection.commit()

#Fetch items from db to use e.g. for display in trees
def fetch_items_from_db(table):
    with sqlite3.connect('invoices.db') as connection:
        cursor = connection.cursor()

        #Specify which invoices to display
        cursor.execute(
            f"SELECT * from {table} ORDER BY invoice_number DESC LIMIT 10;"
        )

        items = cursor.fetchall()
        return items
    

