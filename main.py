import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Invoice generator form")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)




invoice_num_label = tkinter.Label(frame, text="Invoice number")
invoice_num_label.grid(row=0, column=0)
invoice_num_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
invoice_num_spinbox.grid(row=1, column=0)

order_num_label = tkinter.Label(frame, text= "Order number")
order_num_label.grid(row=0, column=1)
order_num_spinbox = tkinter.Spinbox(frame, from_ =1, to=100)
order_num_spinbox.grid(row=1, column=1)

issued_date_label = tkinter.Label(frame, text="Issued on")
issued_date_label.grid(row=0, column=2)
issued_date_entry = tkinter.Entry(frame)
issued_date_entry.grid(row=1, column=2)

due_date_label = tkinter.Label(frame, text="Due date")
due_date_label.grid(row=0, column=3)
due_date_entry = tkinter.Entry(frame)
due_date_entry.grid(row=1, column=3)






window.mainloop()