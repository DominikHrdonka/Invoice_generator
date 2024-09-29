import tkinter
from tkinter import (ttk, messagebox)
from rws import rws
from en import en
import json_data
from json_data import current_year
from databases import fetch_items_from_db
import sqlite3
from date_picker import *
import shared



def open_summary():
    def main():
        summary_root = tkinter.Tk()
        summary_root.title("Summary")
        summary_root.geometry("1050x550")

        frame = tkinter.Frame(summary_root)
        frame.pack(side= "top", fill="y", expand=False, padx=20, pady=5)

        this_year_total_invoiced_label = tkinter.Label(frame, text="Invoiced this year:", pady= 5)
        this_year_total_invoiced_label.grid(row=0, column=0)
        this_year_total_invoiced_entry = tkinter.Entry(frame)
        this_year_total_invoiced_entry.grid(row=0, column=1, padx= 10)
        this_year_total_invoiced_entry.insert(0, json_data.stored_totals_data[current_year]["total_per_year"])

        czk_label = tkinter.Label(frame, text="CZK")
        czk_label.grid(row=0, column=2)

        frame2 = tkinter.Frame(summary_root)
        frame2.pack(side='top', fill='both', expand=True)

        invoices_label = tkinter.Label(frame2, text= "Invoices: ", pady= 5)
        invoices_label.grid(row=1, column=0)

        #Tree for displaying invoices in DB
        columns = ('invoice_number', 'paid', 'issued_on', 'client', 'price')
        invoice_tree = ttk.Treeview(frame2, columns=columns, show= 'headings')
        invoice_tree.grid(row=2, column=0, columnspan= 5, padx= 20, pady= 5)
        invoice_tree.heading('invoice_number', text='Invoice number')
        invoice_tree.heading('paid', text='Paid')
        invoice_tree.heading('issued_on', text='Issued on')
        invoice_tree.heading('client', text='Client')
        invoice_tree.heading('price', text='Price')

        #Insert fetched data into the overview tree
        def display_invoices(tree, invoices):
            for invoice in invoices:
                #iid = invoice_id says to use this identifier with records instead of defafult id
                invoice_id = invoice[0]
                tree.insert('', 0, iid = invoice_id, values=(invoice[1], invoice[2], invoice[3], invoice[4], invoice[5]))
        
        def fetch_and_display(tree, database, table):
            items = fetch_items_from_db(database, table)
            display_invoices(tree, items)
        
        fetch_and_display(invoice_tree, 'invoices.db', 'invoices_list')

        #Top level function to mark selected invoice as paid in DB
        def mark_as_paid():
            selected_invoice = invoice_tree.selection() #Selecting invoice in the tree
            if selected_invoice:
                open_calendar(callback= lambda: mark_as_paid_callback(selected_invoice)) #lambda here serves to call the mark_as_paid_callback later, not immediately
            else:
                messagebox.showinfo(message="You must select an invoice.", title="Note")
                
        #Marking as paid in DB to be used as callback
        def mark_as_paid_callback(invoice):
            with sqlite3.connect('invoices.db') as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        "UPDATE invoices_list SET paid = ? WHERE id = ?", (shared.selected_date, invoice[0])
                        )
            #Delete existing treeview items and then fetching and displaying the updated items.        
            update_treeview(invoice_tree)

        #Function to update treeview
        def update_treeview(tree):
            if tree:
                for item in tree.get_children():
                    tree.delete(item)
                fetch_and_display(invoice_tree, 'invoices.db', 'invoices_list')

        """
        Functions and GUI for buttons regarding invoices displayed in the treeview 
        """
        def delete_invoice():
            selected_invoice = invoice_tree.selection()
            if selected_invoice:
                message = messagebox.askyesnocancel(message="Delete invoice?")
                if message is True:
                    with sqlite3.Connection('invoices.db') as connection:
                        cursor = connection.cursor()

                        #Retrieving invoice's month of issue
                        cursor.execute('SELECT issued_on, price FROM invoices_list WHERE id = ?;', (selected_invoice))
                        issued_date, price = cursor.fetchone()
                        
                        #Deleting invoice from DB
                        cursor.execute('DELETE FROM invoices_list WHERE id = ?;', (selected_invoice))
                    
                    update_treeview(invoice_tree)

                    match issued_date[3:5]:
                        case "01":
                            total = float(january_entry.get()) - float(price)
                            january_entry.delete(0, tkinter.END)
                            january_entry.insert(0, total)
                        case "02":
                            pass
                        case "03":
                            pass
                        case "04":
                            pass
                        case "05":
                            pass
                        case "06":
                            pass
                        case "07":
                            pass
                        case "08":
                            pass
                        case "09":
                            total = float(september_entry.get()) - float(price)
                            september_entry.delete(0, tkinter.END)
                            september_entry.insert(0, total)
                        case "10":
                            pass
                        case "11":
                            pass
                        case "12":
                            pass
                    
                    messagebox.showinfo(message='Invoices deleted.')
            else:
                messagebox.showinfo(message='You must select an invoice')

        frame3 = tkinter.Frame(summary_root)
        frame3.pack(side='top')

        mark_as_paid_button = tkinter.Button(frame3, text = 'Mark as paid', command= mark_as_paid)
        mark_as_paid_button.grid(row=0, column=0, padx= 5, pady= 5)

        delete_invoice_button = tkinter.Button(frame3, text = 'Delete', command=delete_invoice)
        delete_invoice_button.grid(row=0, column=1, padx= 5, pady= 5)

        edit_invoice_button = tkinter.Button(frame3, text='Edit', command=None)
        edit_invoice_button.grid(row=0, column=2, padx=5, pady=5)

        

        """
        Frame and GUI for monthly summary of issued invoices in given years.
        """
        frame4 = tkinter.Frame(summary_root)
        frame4.pack(side="bottom", fill="y", expand=False, padx=20, pady=10)

        invoiced_monthly_label = tkinter.Label(frame4, text='Invoiced per month:')
        invoiced_monthly_label.grid(row=0, column=0, pady=10, columnspan=4)

        january_label = tkinter.Label(frame4, text="January:")
        january_label.grid(row=1, column=0)
        january_entry = tkinter.Entry(frame4)
        january_entry.grid(row=1, column=1)


        february_label = tkinter.Label(frame4, text="February:")
        february_label.grid(row=2, column=0)
        february_entry = tkinter.Entry(frame4)
        february_entry.grid(row=2, column=1)

        march_label = tkinter.Label(frame4, text="March:")
        march_label.grid(row=3, column=0)
        march_entry = tkinter.Entry(frame4)
        march_entry.grid(row=3, column=1)

        april_label = tkinter.Label(frame4, text="April:")
        april_label.grid(row=4, column=0)
        april_entry = tkinter.Entry(frame4)
        april_entry.grid(row=4, column=1)

        may_label = tkinter.Label(frame4, text="May:")
        may_label.grid(row=5, column=0)
        may_entry = tkinter.Entry(frame4)
        may_entry.grid(row=5, column=1)

        june_label = tkinter.Label(frame4, text="June:")
        june_label.grid(row=6, column=0)
        june_entry = tkinter.Entry(frame4)
        june_entry.grid(row=6, column=1)



        july_label = tkinter.Label(frame4, text="July:", padx=10)
        july_label.grid(row=1, column=2)
        july_entry = tkinter.Entry(frame4)
        july_entry.grid(row=1, column=3)

        august_label = tkinter.Label(frame4, text="August:", padx=10)
        august_label.grid(row=2, column=2)
        august_entry = tkinter.Entry(frame4)
        august_entry.grid(row=2, column=3)

        september_label = tkinter.Label(frame4, text="September:", padx=10)
        september_label.grid(row=3, column=2)
        september_entry = tkinter.Entry(frame4)
        september_entry.grid(row=3, column=3)

        october_label = tkinter.Label(frame4, text="October:", padx=10)
        october_label.grid(row=4, column=2)
        october_entry = tkinter.Entry(frame4)
        october_entry.grid(row=4, column=3)

        november_label = tkinter.Label(frame4, text="November:", padx=10)
        november_label.grid(row=5, column=2)
        november_entry = tkinter.Entry(frame4)
        november_entry.grid(row=5, column=3)

        december_label = tkinter.Label(frame4, text="December:", padx=10)
        december_label.grid(row=6, column=2)
        december_entry = tkinter.Entry(frame4)
        december_entry.grid(row=6, column=3)

        #Batch insert of relevant data in each month entry
        months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
            ]
        
        entry_widgets = {
            "january_entry": january_entry,
            "february_entry": february_entry,
            "march_entry": march_entry,
            "april_entry": april_entry,
            "may_entry": may_entry,
            "june_entry": june_entry,
            "july_entry": july_entry,
            "august_entry": august_entry,
            "september_entry": september_entry,
            "october_entry": october_entry,
            "november_entry": november_entry,
            "december_entry": december_entry
        }
        for month in months:
            data = json_data.stored_totals_data[current_year].get(month)
            if data is not None:
                entry_widget = entry_widgets.get(f"{month.lower()}_entry")
                if entry_widget:
                    entry_widget.insert(0, data)


        summary_root.mainloop()
    main()