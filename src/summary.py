import tkinter
from tkinter import (ttk, messagebox)
from rws import rws
from en import en
from json_data import current_year, read_json_file
from databases import fetch_items_from_db, open_database_and_create_cursor
import sqlite3
from date_picker import *
import shared
import json
from functools import partial


def open_summary():
    def main():
        summary_root = tkinter.Tk()
        summary_root.title("Summary")
        summary_root.geometry("1050x620")

        frame0 = tkinter.Frame(summary_root)
        frame0.pack(side="top")

        frame = tkinter.Frame(summary_root)
        frame.pack(side= "top", fill="y", expand=False, padx=20, pady=5)

        this_year_total_invoiced_label = tkinter.Label(frame, text=f"Invoiced in {current_year}:", pady= 5)
        this_year_total_invoiced_label.grid(row=0, column=0)
        this_year_total_invoiced_entry = tkinter.Entry(frame)
        this_year_total_invoiced_entry.grid(row=0, column=1, padx= 10)
        
        """Opening json file to insert required data"""
        json_data = read_json_file(shared.stored_totals_json_path)

        this_year_total_invoiced_entry.insert(0, json_data[current_year]["total_per_year"])

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

        """
        TODO: we need to unite the logic with the new function handling fetching, updating and displaying
        invoices in invoices_tree
        """

        #Insert fetched data into the overview tree

        def display_invoices(invoices):
            for invoice in invoices:
                #iid = invoice_id says to use this identifier with records instead of defafult id
                invoice_id = invoice[0]
                invoice_tree.insert('', 0, iid = invoice_id, values=(invoice[1], invoice[2], invoice[3], invoice[4], invoice[5]))
        
        

        """
        fetch_items_from_db function is a bit different from the one used for fetching
        relevant year invoices since it is used to fetch data in clients.py as well.

        fetch_relevant_year_invoices is ONLY used here for ONE purpose
        """
        def fetch_and_display(database, table):
            items = fetch_items_from_db(database, table)
            display_invoices(items)
        
        

        """
        Function to fetch invocies based on the year selected.
        """
        def fetch_relevat_year_invoices(year):
            with sqlite3.connect(shared.invoices_db_path) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM invoices_list WHERE issued_on LIKE ?;', (f'%{year}%',)
                )
                items = cursor.fetchall()
                return items
            
        def fetch_and_display_relevant_year_invoices(year):
            items = fetch_relevat_year_invoices(year)
            display_invoices(items)
        
        def update_treeview_relevant_year(year):
            for item in invoice_tree.get_children():
                invoice_tree.delete(item)
            fetch_and_display_relevant_year_invoices(year)

        
        fetch_and_display_relevant_year_invoices(current_year)
        """
        fetch_and_display_relevant_year_invoices
        """

        #Top level function to mark selected invoice as paid in DB
        def mark_as_paid():
            selected_invoice = invoice_tree.selection() #Selecting invoice in the tree
            if selected_invoice:
                open_calendar(callback= lambda: mark_as_paid_callback(selected_invoice)) #lambda here serves to call the mark_as_paid_callback later, not immediately
            else:
                messagebox.showinfo(message="You must select an invoice.", title="Note")
                
        #Marking as paid in DB to be used as callback
        def mark_as_paid_callback(invoice):
            with sqlite3.connect(shared.invoices_db_path) as connection:
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
                fetch_and_display(shared.invoices_db_path, 'invoices_list')

        """
        Functions and GUI for buttons regarding invoices displayed in the treeview
        """
        def delete_invoice():
            selected_invoice = invoice_tree.selection()
            if selected_invoice:
                message = messagebox.askyesnocancel(message="Delete invoice?")
                if message is True:
                    with sqlite3.Connection(shared.invoices_db_path) as connection:
                        cursor = connection.cursor()

                        #Retrieving invoice's month of issue
                        cursor.execute('SELECT issued_on, price FROM invoices_list WHERE id = ?;', (selected_invoice))
                        issued_date, price = cursor.fetchone()
                        
                        #Deleting invoice from DB
                        cursor.execute('DELETE FROM invoices_list WHERE id = ?;', (selected_invoice))
                    
                    update_treeview(invoice_tree)

                    match issued_date[3:5]:
                        case "01":
                            month = 'january'
                        case "02":
                            month = 'february'
                        case "03":
                            month = 'march'
                        case "04":
                            month = 'april'
                        case "05":
                            month = 'may'
                        case "06":
                            month = 'june'
                        case "07":
                            month = 'july'
                        case "08":
                            month = 'august'
                        case "09":
                            month = 'september'
                        case "10":
                            month = 'october'
                        case "11":
                            month = 'november'
                        case "12":
                            month = 'december'
                    """
                    We need to store the subtracted price to the JSON file as well (update it)
                    so that it is properly retrieved upon next opening of Summary
                    """
                    total = float(entry_widgets[month].get()) - float(price)
                    

                    #Now, we need to open json file, update the data and write it back to json
                    stored_totals = read_json_file(shared.stored_totals_json_path)

                    #This is the update itself
                    stored_totals[current_year][month.capitalize()] = total
                    stored_totals[current_year]['total_per_year'] -= price
                    
                    #Saving the udpate to the json
                    with open('stored_totals.json', 'w') as outfile:
                        json.dump(stored_totals, outfile, indent=4)
                    
                    #Here we are updating the value inserted in the given entry_widget
                    entry_widgets[month].delete(0, tkinter.END)
                    changed_month_total = stored_totals[current_year].get(month.capitalize())
                    if changed_month_total is not None:
                        entry_widgets[month].insert(0, changed_month_total)
                    
                    #Update the value of this_year_total_invoiced entry
                    this_year_total_invoiced_entry.delete(0, tkinter.END)
                    changed_year_total = stored_totals[current_year].get('total_per_year')
                    if changed_year_total is not None:
                        this_year_total_invoiced_entry.insert(0, changed_year_total)
                    
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
        frame4.pack(side="top", fill="y", expand=False, padx=20, pady=10)

        invoiced_monthly_label = tkinter.Label(frame4, text='Invoiced per month:')
        invoiced_monthly_label.grid(row=0, column=0, pady=10, columnspan=4)

        """
        Functions to update individual summary window parts according to the year selected
        using the buttons at the top.
        """
        def update_this_year_total_invoiced(year):
            this_year_total_invoiced_label.config(text=f"Invoiced in {year}:")
            stored_totals = read_json_file(shared.stored_totals_json_path)
            this_year_total_invoiced_entry.delete(0, tkinter.END)
            this_year_total_invoiced_entry.insert(0, stored_totals[year]["total_per_year"])


        def update_view_of_relevant_year_data(year):
            update_this_year_total_invoiced(year)
            update_treeview_relevant_year(year)
            batch_delete_month_data()
            batch_insert_month_data(year)

        """
        Dynamic logic of creating buttons according to the previous years.

        TODO:
        - As for button position, we can come up with a logic that will position new buttons
        on a new row so that they don't keep going horizontally
        - move the GUI up to frame0
        """
        #Opening stored_totals.json from which we will be using stored years data

        
        previous_years = read_json_file(shared.stored_totals_json_path)
        row_data = 1
        column_data = 1

        for year in previous_years:
            if year != 'total_for_all_years':
                previous_year_button = tkinter.Button(frame0, text= year, command= partial(update_view_of_relevant_year_data, year))
                previous_year_button.grid(row=row_data, column=column_data, padx = 5, pady=10)
                column_data += 1
        
        """
        Function to fetch and display all the invoices upon clicking all_invoices_button
        
        DESCR.:
        - it updates the invoice_tree with ALL the invoices
        - it changes this_year_total_invoiced_label to 'Invoiced in total: '
        - it loads corresponding data from stored_totals.json
        """
        def fetch_and_display_all_invoices():
            update_treeview(invoice_tree)
            this_year_total_invoiced_label.config(text='Invoiced in total:')

            stored_totals = read_json_file(shared.stored_totals_json_path)

            this_year_total_invoiced_entry.delete(0, tkinter.END)
            this_year_total_invoiced_entry.insert(0, stored_totals['total_for_all_years'])
        
        all_invoices_button = tkinter.Button(frame0, text='All', command= fetch_and_display_all_invoices)
        all_invoices_button.grid(row=1, column=0, padx=5, pady=10)

        

        
        """
        Frame only for the months GUI and data
        """
        frame5 = tkinter.Frame(summary_root)
        frame5.pack(side="top", fill="y", expand=False, padx=20, pady=5)

        january_label = tkinter.Label(frame5, text="January:")
        january_label.grid(row=2, column=0)
        january_entry = tkinter.Entry(frame5)
        january_entry.grid(row=2, column=1)


        february_label = tkinter.Label(frame5, text="February:")
        february_label.grid(row=3, column=0)
        february_entry = tkinter.Entry(frame5)
        february_entry.grid(row=3, column=1)

        march_label = tkinter.Label(frame5, text="March:")
        march_label.grid(row=4, column=0)
        march_entry = tkinter.Entry(frame5)
        march_entry.grid(row=4, column=1)

        april_label = tkinter.Label(frame5, text="April:")
        april_label.grid(row=5, column=0)
        april_entry = tkinter.Entry(frame5)
        april_entry.grid(row=5, column=1)

        may_label = tkinter.Label(frame5, text="May:")
        may_label.grid(row=6, column=0)
        may_entry = tkinter.Entry(frame5)
        may_entry.grid(row=6, column=1)

        june_label = tkinter.Label(frame5, text="June:")
        june_label.grid(row=7, column=0)
        june_entry = tkinter.Entry(frame5)
        june_entry.grid(row=7, column=1)


        july_label = tkinter.Label(frame5, text="July:", padx=10)
        july_label.grid(row=2, column=2)
        july_entry = tkinter.Entry(frame5)
        july_entry.grid(row=2, column=3)

        august_label = tkinter.Label(frame5, text="August:", padx=10)
        august_label.grid(row=3, column=2)
        august_entry = tkinter.Entry(frame5)
        august_entry.grid(row=3, column=3)

        september_label = tkinter.Label(frame5, text="September:", padx=10)
        september_label.grid(row=4, column=2)
        september_entry = tkinter.Entry(frame5)
        september_entry.grid(row=4, column=3)

        october_label = tkinter.Label(frame5, text="October:", padx=10)
        october_label.grid(row=5, column=2)
        october_entry = tkinter.Entry(frame5)
        october_entry.grid(row=5, column=3)

        november_label = tkinter.Label(frame5, text="November:", padx=10)
        november_label.grid(row=6, column=2)
        november_entry = tkinter.Entry(frame5)
        november_entry.grid(row=6, column=3)

        december_label = tkinter.Label(frame5, text="December:", padx=10)
        december_label.grid(row=7, column=2)
        december_entry = tkinter.Entry(frame5)
        december_entry.grid(row=7, column=3)

        #Batch insert of relevant data in each month entry
        
        months = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
            ]
        
        entry_widgets = {
            "january": january_entry,
            "february": february_entry,
            "march": march_entry,
            "april": april_entry,
            "may": may_entry,
            "june": june_entry,
            "july": july_entry,
            "august": august_entry,
            "september": september_entry,
            "october": october_entry,
            "november": november_entry,
            "december": december_entry
        }

        def batch_insert_month_data(year):

            data = read_json_file(shared.stored_totals_json_path)

            for month in months:
                if data[year].get(month) is not None:
                    entry_widget = entry_widgets.get(month.lower())
                    if entry_widget:
                        entry_widget.insert(0, data[year][month])
        
        def batch_delete_month_data():
            for widget in entry_widgets:
                entry_widgets[widget].delete(0, tkinter.END)
            
        batch_insert_month_data(current_year)


        summary_root.mainloop()
    main()