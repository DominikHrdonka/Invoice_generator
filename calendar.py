import tkinter
from tkinter import ttk
from tkcalendar import *

root = tkinter.Tk()
root.title("Calendar")
root.geometry("300x300")


select_date_button = tkinter.Button(text="Select date")
select_date_button.pack(pady=10)

root.mainloop()