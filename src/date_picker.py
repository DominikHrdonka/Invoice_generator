import tkinter
from tkinter import ttk
from tkcalendar import Calendar
import shared


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

    cal = Calendar(
        root, selectmode = 'day', date_pattern="dd-mm-yyyy",
                year = 2024, month = 5,
                day = 17)

    cal.pack(pady=5)

    select_date_button = tkinter.Button(root, text="Select date", command= select_date)
    select_date_button.pack(pady=10)

    root.mainloop()