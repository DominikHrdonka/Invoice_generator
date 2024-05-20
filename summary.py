import tkinter
from tkinter import ttk
from rws import rws
from en import en
import shared
import json_data

def open_summary():
    root = tkinter.Tk()
    root.title("Summary")
    root.geometry("400x400")

    frame = tkinter.Frame(root)
    frame.pack(padx=20, pady=10)

    this_year_total_invoiced_label = tkinter.Label(frame, text="Invoiced this year:", pady= 5)
    this_year_total_invoiced_label.grid(row=0, column=0)
    this_year_total_invoiced_entry = tkinter.Entry(frame)
    this_year_total_invoiced_entry.grid(row=0, column=1, padx= 10)
    this_year_total_invoiced_entry.insert(0, json_data.stored_totals["total_curr_month"])


    czk_label = tkinter.Label(frame, text="CZK")
    czk_label.grid(row=0, column=2)


    root.mainloop()