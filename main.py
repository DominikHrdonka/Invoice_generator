import tkinter
from tkinter import ttk


def add_item():
    po = int(po_entry.get())
    project = project_entry.get()
    price= float(project_entry.get())



window = tkinter.Tk()
window.title("Invoice generator form")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

#Labels and entry fields
invoice_num_label = tkinter.Label(frame, text="Invoice number")
invoice_num_label.grid(row=0, column=0)
invoice_num_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
invoice_num_spinbox.grid(row=1, column=0)

order_num_label = tkinter.Label(frame, text= "Order number")
order_num_label.grid(row=0, column=1)
order_num_spinbox = tkinter.Spinbox(frame, from_ =1, to=100)
order_num_spinbox.grid(row=1, column=1)

rws_label = tkinter.Label(frame, text="RWS")
rws_label.grid(row=1, column=1)

issued_date_label = tkinter.Label(frame, text="Issued on")
issued_date_label.grid(row=0, column=2)
issued_date_entry = tkinter.Entry(frame)
issued_date_entry.grid(row=1, column=2)

due_date_label = tkinter.Label(frame, text="Due date")
due_date_label.grid(row=0, column=3)
due_date_entry = tkinter.Entry(frame)
due_date_entry.grid(row=1, column=3)

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
add_item_button.grid(row=5, column=0, columnspan=4, sticky="news", pady=10)

# Tree
columns = ('po', 'project', 'price')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.grid(row=6, column=0, columnspan=4, padx=20, pady=10)
tree.heading("po", text="PO")
tree.heading("project", text="Project")
tree.heading("price", text="Price")

generate_invoice_button = tkinter.Button(frame, text="Generate invoice")
generate_invoice_button.grid(row=7, column=0, columnspan=4, sticky= "news", padx=20, pady=10)

new_invoice_button = tkinter.Button(frame, text="Generate Invoice")
new_invoice_button.grid(row=8, column=0, columnspan=4, sticky="news", padx=20, pady=5)



window.mainloop()