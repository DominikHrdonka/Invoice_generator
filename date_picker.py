import tkinter
from tkinter import ttk
from tkcalendar import Calendar

def open_calendar():
    def main():

        #Functionality
        date_selected = None

        def select_date():
            date_selected = cal.get_date()
            print(date_selected)
            root.destroy()
        
    

        #GUI
        root = tkinter.Tk()
        root.title("Calendar")
        root.geometry("300x300")

        cal = Calendar(
            root, selectmode = 'day',
                    year = 2024, month = 5,
                    day = 17)

        cal.pack(pady=5)



        select_date_button = tkinter.Button(text="Select date", command= select_date)
        select_date_button.pack(pady=10)

        root.mainloop()
    main()