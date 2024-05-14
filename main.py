import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Invoice generator form")

frame = tkinter.Frame(window)
frame.pack()

# Program labels:
invoice_num_label = tkinter.Label(frame, text="Invoice number")
invoice_num_label.grid(row=0, column=0)

order_num_label = tkinter.Label(frame, text= "Order number")
order_num_label.grid(row=0, column=1)

issued_date_label = tkinter.Label(frame, text="Issued on")
issued_date_label.grid(row=0, column=2)

due_date_label = tkinter.Label(frame, text="Due date")
due_date_label.grid(row=0, column=3)

#Program entry fields:

invoice_num_entry = tkinter.Entry(frame)
invoice_num_entry.grid(row=1, column=0)

order_num_entry = tkinter.Entry(frame)
order_num_entry.grid(row=1, column=1)

issued_date_entry = tkinter.Entry(frame)
issued_date_entry.grid(row=1, column=2)

due_date_entry = tkinter.Entry(frame)
due_date_entry.grid(row=1, column=3)

window.mainloop()