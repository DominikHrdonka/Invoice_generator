import tkinter
from tkinter import ttk
from rws import rws
from en import en

def rws_invoice():
    rws()

def en_invoice():
    en()
        

# GUI
window = tkinter.Tk()
window.title("Invoice generator form")
window.geometry("400x400")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

#Labels and entry fields
rws_invoice_label = tkinter.Label(frame, text="Choose invoice")
rws_invoice_label.grid(row=0, column=0, columnspan=2)
rws_invoice_button = tkinter.Button(frame, text= "RWS Invoice", command= rws_invoice)
rws_invoice_button.grid(row=1, column=0, padx=5)

en_invoice_button = tkinter.Button(frame, text= "English Invoice", command= en_invoice)
en_invoice_button.grid(row=1, column=2)

window.mainloop()