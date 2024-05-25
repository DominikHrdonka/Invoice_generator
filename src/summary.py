import tkinter
from tkinter import ttk
from rws import rws
from en import en
import shared
import json_data
from json_data import current_year



def open_summary():
    root = tkinter.Tk()
    root.title("Summary")
    root.geometry("600x280")

    frame = tkinter.Frame(root)
    frame.pack(side= "top", padx=20, pady=10)

    this_year_total_invoiced_label = tkinter.Label(frame, text="Invoiced this year:", pady= 5)
    this_year_total_invoiced_label.grid(row=0, column=0)
    this_year_total_invoiced_entry = tkinter.Entry(frame)
    this_year_total_invoiced_entry.grid(row=0, column=1, padx= 10)
    this_year_total_invoiced_entry.insert(0, json_data.stored_totals_data[current_year]["total_per_year"])

    czk_label = tkinter.Label(frame, text="CZK")
    czk_label.grid(row=0, column=2)



    frame2 = tkinter.Frame(root)
    frame2.pack(side="bottom", padx=20, pady=10)

    invoiced_monthly_label = tkinter.Label(frame2, text='Invoiced per month:')
    invoiced_monthly_label.grid(row=0, column=0, pady=20, columnspan=4)

    january_label = tkinter.Label(frame2, text="January:")
    january_label.grid(row=1, column=0)
    january_entry = tkinter.Entry(frame2)
    january_entry.grid(row=1, column=1)
   

    february_label = tkinter.Label(frame2, text="February:")
    february_label.grid(row=2, column=0)
    february_entry = tkinter.Entry(frame2)
    february_entry.grid(row=2, column=1)

    march_label = tkinter.Label(frame2, text="March:")
    march_label.grid(row=3, column=0)
    march_entry = tkinter.Entry(frame2)
    march_entry.grid(row=3, column=1)

    april_label = tkinter.Label(frame2, text="April:")
    april_label.grid(row=4, column=0)
    april_entry = tkinter.Entry(frame2)
    april_entry.grid(row=4, column=1)

    may_label = tkinter.Label(frame2, text="May:")
    may_label.grid(row=5, column=0)
    may_entry = tkinter.Entry(frame2)
    may_entry.grid(row=5, column=1)

    june_label = tkinter.Label(frame2, text="June:")
    june_label.grid(row=6, column=0)
    june_entry = tkinter.Entry(frame2)
    june_entry.grid(row=6, column=1)



    july_label = tkinter.Label(frame2, text="July:", padx=10)
    july_label.grid(row=1, column=2)
    july_entry = tkinter.Entry(frame2)
    july_entry.grid(row=1, column=3)

    august_label = tkinter.Label(frame2, text="August:", padx=10)
    august_label.grid(row=2, column=2)
    august_entry = tkinter.Entry(frame2)
    august_entry.grid(row=2, column=3)

    september_label = tkinter.Label(frame2, text="September:", padx=10)
    september_label.grid(row=3, column=2)
    september_entry = tkinter.Entry(frame2)
    september_entry.grid(row=3, column=3)

    october_label = tkinter.Label(frame2, text="October:", padx=10)
    october_label.grid(row=4, column=2)
    october_entry = tkinter.Entry(frame2)
    october_entry.grid(row=4, column=3)

    november_label = tkinter.Label(frame2, text="November:", padx=10)
    november_label.grid(row=5, column=2)
    november_entry = tkinter.Entry(frame2)
    november_entry.grid(row=5, column=3)

    december_label = tkinter.Label(frame2, text="December:", padx=10)
    december_label.grid(row=6, column=2)
    december_entry = tkinter.Entry(frame2)
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


    root.mainloop()