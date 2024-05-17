import tkinter
from tkinter import ttk
from tkcalendar import Calendar

root = tkinter.Tk()
root.title("Calendar")
root.geometry("300x300")

cal = Calendar(
    root, selectmode = 'day',
               year = 2024, month = 5,
               day = 17)

cal.pack(pady=20)


select_date_button = tkinter.Button(text="Select date")
select_date_button.pack(pady=10)

root.mainloop()