import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Invoice generator form")

frame = tkinter.Frame(window)
frame.pack()

invoice_num_label = tkinter.Label(frame, text="Invoice number")
invoice_num_label.grid(row=0, column=0)

order_num_label = tkinter.Label(frame, text= "Order number")
order_num_label.grid(row=0, column=1)

issued_date = tkinter.Label(frame, text="Issued on")
issued_date.grid(row=0, column=2)

due_date = tkinter.Label(frame, text="Due date")
due_date.grid(row=1, column=0)


window.mainloop()