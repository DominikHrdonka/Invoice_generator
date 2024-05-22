import tkinter
from tkinter import ttk
from tkcalendar import Calendar
import shared
from datetime import datetime


def open_calendar(callback):
    #Functionality

    def select_date():
        shared.selected_date = cal.get_date()
        root.destroy()
        callback()
        
        

    #GUI
    root = tkinter.Tk()
    root.title("Calendar")
    root.geometry("300x300")

    today = datetime.today()

    cal = Calendar(
        root, selectmode = 'day', date_pattern="dd-mm-yyyy",
                year = today.year, month = today.month,
                day = today.day)

    cal.pack(pady=5)

    select_date_button = tkinter.Button(root, text="Select date", command= select_date)
    select_date_button.pack(pady=10)

    root.mainloop()