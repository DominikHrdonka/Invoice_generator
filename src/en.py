import tkinter
from tkinter import ttk
import tkinter.filedialog
from docxtpl import DocxTemplate
from tkinter import messagebox
from date_picker import *
import shared
import json_data
from tkinter import filedialog
from datetime import datetime
from databases import insert_into_db
from listbox import open_client_listbox
import sqlite3



def en():
    def main():

        invoice_list = []
        prices = []
        def add_item():
            lessons = lesson_num_entry.get()
            price= float(price_entry.get())
            prices.append(price)
            formated_price = format_price(price)

            invoice_item = [lessons, formated_price]

            tree.insert('', 0, values=invoice_item)
            clear_item()
            invoice_list.append(invoice_item)
        
        def clear_item():
            lesson_num_entry.delete(0, tkinter.END)
            price_entry.delete(0, tkinter.END)
            

        def new_invoice():
            invoice_num_entry.delete(0, tkinter.END)
            name_entry.delete(0, tkinter.END)
            issued_date_entry.delete(0, tkinter.END)
            due_date_entry.delete(0, tkinter.END)
            clear_item()
            tree.delete(*tree.get_children())
            invoice_list.clear()

        def new_invoice_and_maintain_inv_num():
            new_invoice()
            invoice_num_insert()
        
        def generate_invoice(callback):
            confirmation = messagebox.askyesno("Generate invoice?", "Do you really want to generate the inovice?")
            if confirmation is True:
                doc = DocxTemplate("/root/workspace/github.com/DominikHrdonka/Invoice_generator/templates/INVOICE_template_en.docx")
                invoice_num = invoice_num_entry.get()
                name = name_entry.get()
                issued_date = issued_date_entry.get()
                due_date = due_date_entry.get()


                total_price = sum(prices)
                formated_total_price = format_price(total_price)
                json_data.save_totals(total_price)

                doc.render(
                    {
                        "invoice_num": invoice_num,
                        "name": name,
                        "date": issued_date,
                        "due_date": due_date,
                        "invoice_list": invoice_list,
                        "total_price": formated_total_price
                    }
                )
        
                
                #Dialog to enter the desired location for saving the file
                doc_path = filedialog.askdirectory(
                    parent= window, title='Where do you want to save the invoice?', initialdir= "/mnt/c/Účetnictví/", mustexist=True
                )

                doc_name = "new_invoice_" + name + " - " + invoice_num + "_" + "month.docx"
                doc.save(doc_path+ '/'+ doc_name)
                messagebox.showinfo("Invoice Complete", "Invoice Complete") 
                insert_into_db(invoice_num, '-', issued_date, name, total_price)
                new_invoice()
                json_data.update_next_invoice_num()
                callback()

        def callback_get_issued_date():
            issued_date_entry.insert(0, shared.selected_date)
        
        def callback_get_due_date():
            due_date_entry.insert(0, shared.selected_date)

        def open_calendar_issued_date():
            open_calendar(callback_get_issued_date)
        
        def open_calendar_due_date():
            open_calendar(callback_get_due_date)

        #Insert client in Client field
        def insert_client_callback():
            id = shared.selected_client
            with sqlite3.connect('clients.db') as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT name FROM client_list WHERE id = ?;', (id))
                clients = cursor.fetchall()
            name_entry.delete(0, tkinter.END)
            for client in clients:
                name_entry.insert(0, client[0])

        def insert_client():
            open_client_listbox(insert_client_callback)


        #Update calc_invoice_number asynchronously using callback function
        def invoice_num_insert():
            calc_invoice_number = json_data.current_year + f'-{json_data.stored_shared_data["next_invoice_num"]:04}'
            invoice_num_entry.insert(0, calc_invoice_number)
        
        def gen_invoice_and_update_invoice_number():
            generate_invoice(invoice_num_insert)

        #Modify number format for Czech locale
        def format_price(num):
            formated_number = f'{num:,.2f}'
            formated_number = formated_number.replace(',', ' ').replace('.', ',')
            return formated_number
        
        """
        Function that counts total price based on the given client's hourly rate and number of lessons.
        - it gets executed after clicking on a button to count (next to Price entry???)
        """
        def count_price():
             pass


    # GUI
        window = tkinter.Tk()
        window.title("English invoice generator form")

        frame = tkinter.Frame(window)
        frame.pack(padx=20, pady=10)

        #Labels and entry fields
        invoice_num_label = tkinter.Label(frame, text="Invoice number")
        invoice_num_label.grid(row=0, column=0)
        
        invoice_num_entry = tkinter.Entry(frame)
        invoice_num_entry.grid(row=1, column=0)
        invoice_num_insert()

        name_label = tkinter.Label(frame, text= "Client")
        name_label.grid(row=0, column=1)
        name_entry = tkinter.Entry(frame)
        name_entry.grid(row=1, column=1)

        client_button = tkinter.Button(frame, text="…", command=insert_client)
        client_button.grid(row=1, column=2)

        issued_date_label = tkinter.Label(frame, text="Issued on")
        issued_date_label.grid(row=0, column=3)
        issued_date_entry = tkinter.Entry(frame)
        issued_date_entry.grid(row=1, column=3)
        
        issued_date_button = tkinter.Button(frame, text="…", command=open_calendar_issued_date)
        issued_date_button.grid(row=1, column=4)

        due_date_label = tkinter.Label(frame, text="Due date")
        due_date_label.grid(row=0, column=5)
        due_date_entry = tkinter.Entry(frame)
        due_date_entry.grid(row=1, column=5)

        due_date_button = tkinter.Button(frame, text="…", command=open_calendar_due_date)
        due_date_button.grid(row=1, column=6)

        lesson_num_label = tkinter.Label(frame, text="Lessons")
        lesson_num_label.grid(row=3, column=1)
        lesson_num_entry = tkinter.Entry(frame)
        lesson_num_entry.grid(row=4, column=1)


        price_label = tkinter.Label(frame, text="Price")
        price_label.grid(row=3, column=3)
        price_entry = tkinter.Entry(frame)
        price_entry.grid(row=4, column=3)

        count_price_button = tkinter.Button(frame, text='Count', command=None)
        count_price_button.grid(row=4, column=4)

        # Add item button
        add_item_button = tkinter.Button(frame, text="Add item", command= add_item)
        add_item_button.grid(row=5, column=0, columnspan=6, sticky="news", pady=10)

        # Tree
        columns = ('lessons', 'price')
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.grid(row=6, column=0, columnspan=6, padx=20, pady=10)
        tree.heading("lessons", text="Lessons")
        tree.heading("price", text="Price")

        generate_invoice_button = tkinter.Button(frame, text="Generate invoice", command=gen_invoice_and_update_invoice_number)
        generate_invoice_button.grid(row=7, column=0, columnspan=6, sticky= "news", padx=20, pady=10)

        new_invoice_button = tkinter.Button(frame, text="New Invoice", command = new_invoice_and_maintain_inv_num)
        new_invoice_button.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)



        window.mainloop()
    main()
