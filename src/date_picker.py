import tkinter
from tkinter import ttk
from tkcalendar import Calendar
import shared
from datetime import datetime


def open_calendar(callback=None):
    #Functionality

    def select_date():
        shared.selected_date = cal.get_date()
        print("Date selected successfully")
        calendar_root.destroy()
        print("TK window killed successfully")
        if callback:
            callback()
        else:
            print("No callback")
        
    #Getting today's date
    today = datetime.today()

    #GUI
    calendar_root = tkinter.Tk()
    calendar_root.title("Calendar")
    calendar_root.geometry("300x300")

    cal = Calendar(
        calendar_root, selectmode = 'day', date_pattern="dd-mm-yyyy",
                year = today.year, month = today.month,
                day = today.day)

    cal.pack(pady=5)

    select_date_button = tkinter.Button(calendar_root, text="Select date", command= select_date)
    select_date_button.pack(pady=10)

    calendar_root.mainloop()