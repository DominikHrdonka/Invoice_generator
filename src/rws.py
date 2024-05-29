import tkinter
from docxtpl import DocxTemplate
from tkinter import (
    ttk,
    messagebox,
    filedialog
)
import shared
from date_picker import open_calendar
import json_data
from datetime import datetime

def rws():
    def main():

        invoice_list = []

        def add_item():
            po = po_entry.get()
            project = project_entry.get()
            price= float(price_entry.get())
            invoice_item = [po, project, price]

            tree.insert('', 0, values=invoice_item)
            clear_item()
            invoice_list.append(invoice_item)
        
        def clear_item():
            po_entry.delete(0, tkinter.END)
            project_entry.delete(0, tkinter.END)
            price_entry.delete(0, tkinter.END)
            

        def new_invoice():
            invoice_num_entry.delete(0, tkinter.END)
            order_num_entry.delete(0, tkinter.END)
            issued_date_entry.delete(0, tkinter.END)
            due_date_entry.delete(0, tkinter.END)
            clear_item()
            tree.delete(*tree.get_children())
            invoice_list.clear()

        def new_invoice_and_maintain_inv_num():
            new_invoice()
            invoice_and_order_num_insert()
        
        def generate_invoice(callback):
            confirmation = messagebox.askyesno("Generate inovice?", "Do you really want to generate the inovice?")
            if confirmation is True:
                doc = DocxTemplate("/root/workspace/github.com/DominikHrdonka/Invoice_generator/templates/INVOICE_template_rws.docx")
                invoice_num = invoice_num_entry.get()
                order_num = order_num_entry.get()
                issued_date = issued_date_entry.get()
                due_date = due_date_entry.get()
                total_price = sum(item[2] for item in invoice_list)
                json_data.save_totals(total_price)

                doc.render(
                    {
                        "invoice_num": invoice_num,
                        "order_num": order_num,
                        "date": issued_date,
                        "due_date": due_date,
                        "invoice_list": invoice_list,
                        "total_price": total_price
                    }
                )

                doc_path = "/mnt/c/Účetnictví/"
                curr_year_folder = datetime.now().strftime("%Y") + "/"
                doc_name = "new_invoice_" + "RWS - "+ invoice_num + "_" + order_num + ".docx"
                doc.save(doc_path+curr_year_folder+doc_name)
                messagebox.showinfo("Invoice Complete", "Invoice Complete") 
                new_invoice()
                json_data.update_next_invoice_num()
                json_data.update_next_order_num()
                callback()
        
        def callback_get_issued_date():
            issued_date_entry.insert(0, shared.selected_date)

        def open_calendar_issued_date():
            open_calendar(callback_get_issued_date)

        def callback_get_due_date():
            due_date_entry.insert(0, shared.selected_date)
        
        def open_calendar_due_date():
            open_calendar(callback_get_due_date)

            
        #Update calc_invoice_number and calc_next_order_num asynchronously
        def invoice_and_order_num_insert():
            calc_invoice_number = json_data.current_year + '-' + str(json_data.stored_shared_data["next_invoice_num"])
            invoice_num_entry.insert(0, calc_invoice_number)
            
            calc_order_num = "RWS" + str(json_data.stored_shared_data["next_order_num"])
            order_num_entry.insert(0, calc_order_num)

        # Use callback function to update per above
        def gen_invoice_and_update_invoice_number():
            generate_invoice(invoice_and_order_num_insert)

    
    

    # GUI
        window = tkinter.Tk()
        window.title("RWS invoice generator form")

        frame = tkinter.Frame(window)
        frame.pack(padx=20, pady=10)

        #Labels and entry fields
        invoice_num_label = tkinter.Label(frame, text="Invoice number")
        invoice_num_label.grid(row=0, column=0)
        invoice_num_entry = tkinter.Entry(frame)
        
        invoice_num_entry.grid(row=1, column=0)

        order_num_label = tkinter.Label(frame, text= "Order number")
        order_num_label.grid(row=0, column=1)
        order_num_entry = tkinter.Entry(frame)
        order_num_entry.grid(row=1, column=1)

        invoice_and_order_num_insert()


        issued_date_label = tkinter.Label(frame, text="Issued on")
        issued_date_label.grid(row=0, column=2)
        issued_date_entry = tkinter.Entry(frame)
        issued_date_entry.grid(row=1, column=2)
        issued_date_button = tkinter.Button(frame, text="…", command= open_calendar_issued_date)
        issued_date_button.grid(row=1, column=3)

        due_date_label = tkinter.Label(frame, text="Due date")
        due_date_label.grid(row=0, column=4)
        due_date_entry = tkinter.Entry(frame)
        due_date_entry.grid(row=1, column=4)
        due_date_button = tkinter.Button(frame, text="…", command= open_calendar_due_date)
        due_date_button.grid(row=1, column=5)

        po_label = tkinter.Label(frame, text="PO")
        po_label.grid(row=3, column=0)
        po_entry = tkinter.Entry(frame)
        po_entry.grid(row=4, column=0)

        project_label = tkinter.Label(frame, text="Project")
        project_label.grid(row=3, column=1)
        project_entry = tkinter.Entry(frame)
        project_entry.grid(row=4, column=1)

        price_label = tkinter.Label(frame, text="Price")
        price_label.grid(row=3, column=2)
        price_entry = tkinter.Entry(frame)
        price_entry.grid(row=4, column=2)

        # Add item button
        add_item_button = tkinter.Button(frame, text="Add item", command= add_item)
        add_item_button.grid(row=5, column=0, columnspan=6, sticky="news", pady=10)

        # Tree
        columns = ('po', 'project', 'price')
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        tree.grid(row=6, column=0, columnspan=6, padx=20, pady=10)
        tree.heading("po", text="PO")
        tree.heading("project", text="Project")
        tree.heading("price", text="Price")

        generate_invoice_button = tkinter.Button(frame, text="Generate invoice", command=gen_invoice_and_update_invoice_number)
        generate_invoice_button.grid(row=7, column=0, columnspan=6, sticky= "news", padx=20, pady=10)

        new_invoice_button = tkinter.Button(frame, text="New Invoice", command = new_invoice_and_maintain_inv_num)
        new_invoice_button.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)



        window.mainloop()
    main()
