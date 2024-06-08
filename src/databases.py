import sqlite3
import os

def insert_into_db(invoice_number, paid, issued_on, client, price):
    #Create or connect to DB
    with sqlite3.connect('invoices.db') as connection:
    #object of DB that handles all the communication with the DB
        cursor = connection.cursor()

        #CREATING TABLE in the DB
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS invoices (invoice_number TEXT, paid TEXT, issued_on TEXT, client TEXT, price REAL);"
            )

        cursor.execute("INSERT INTO invoices (invoice_number, paid, issued_on, client, price) VALUES (?, ?, ?, ?, ?);", (invoice_number, paid, issued_on, client, price))
        connection.commit()