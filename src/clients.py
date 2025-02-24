import tkinter
from tkinter import (ttk, messagebox)
import sqlite3
from databases import (fetch_items_from_db)
import summary
import shared

def open_clients():
    def main():

        #Functions

        def update_clients_in_treeview():
                 clients = clients_treeview.get_children()
                 for client in clients:
                      clients_treeview.delete(client)
                 display_clients_in_treeview()

        def new_client():
            

            def add_client_in_DB():
                name = name_entry.get()
                email = email_entry.get()
                hourly_rate = hourly_rate_entry.get()

                with sqlite3.connect(shared.clients_db_path) as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        "INSERT INTO client_list (name, email, hourly_rate) VALUES (?, ?, ?);", (name, email, hourly_rate)
                    )
                messagebox.showinfo(message='Client successfully added.')
                update_clients_in_treeview()
                new_client_root.destroy()
            

                 
        

            new_client_root = tkinter.Tk()
            new_client_root.title('New Client')
            new_client_root.geometry('300x200')

            new_client_frame = ttk.Frame(new_client_root)
            new_client_frame.pack(padx=10, pady=10)

            name_label = tkinter.Label(new_client_frame, text='Name: ')
            name_label.grid(row=0, column=0)
            name_entry = tkinter.Entry(new_client_frame)
            name_entry.grid(row=0, column=1)

            email_label = tkinter.Label(new_client_frame, text='Email: ')
            email_label.grid(row=1, column=0)
            email_entry = tkinter.Entry(new_client_frame)
            email_entry.grid(row=1, column=1)

            hourly_rate_label = tkinter.Label(new_client_frame, text='Hourly rate: ')
            hourly_rate_label.grid(row=2, column=0)
            hourly_rate_entry = tkinter.Entry(new_client_frame)
            hourly_rate_entry.grid(row=2, column=1)

            add_client_button = tkinter.Button(new_client_frame, text='Add Client', command= add_client_in_DB)
            add_client_button.grid(row=3, column=0, columnspan=2, sticky='news', pady=15)

        """
        Function to remove client from DB.
        Client must be selected ---> if selected --> show dialog to confirm --> remove or drop --> update accordingly
        
        """
        def remove_client_from_db():
            client = clients_treeview.selection()
            if client:
                message = messagebox.askyesnocancel(message='Are you sure to remove the client?')
                if message is True:
                    with sqlite3.connect(shared.clients_db_path) as connection:
                        cursor = connection.cursor()
                        cursor.execute('DELETE FROM client_list WHERE id = ?;', (client))
                    messagebox.showinfo(message='Client successfully removed')
                    update_clients_in_treeview()
            else:
                    messagebox.showinfo(message='You must select a client.')

        """
        if client is selected --> open windows with entries of the client --> change values and save 
        """
        def edit_client_in_DB():
            client = clients_treeview.selection()[0]
            
            def save_changes():
                message = messagebox.askyesnocancel(message='Are you sure to edit the client?')
                if message is True:
                    changed_name = name_entry.get()
                    changed_email = email_entry.get()
                    changed_hourly_rate = hourly_rate_entry.get()

                    """
                    Actual change to the client in DB:
                    """
                    with sqlite3.connect(shared.clients_db_path) as connection:
                        cursor = connection.cursor()
                        cursor.execute('UPDATE client_list SET name = ?, email = ?, hourly_rate = ? WHERE id = ?;', (changed_name, changed_email, changed_hourly_rate, client))
                    update_clients_in_treeview()
                    edit_client_root.destroy()

            if client:
                with sqlite3.connect(shared.clients_db_path) as connection:
                    cursor = connection.cursor()
                    cursor.execute('SELECT * FROM client_list WHERE id = ?;', (client))

                client_information = cursor.fetchone()   
                  
                #GUI
                edit_client_root = tkinter.Tk()
                edit_client_root.title('New Client')
                edit_client_root.geometry('300x200')

                edit_client_frame = ttk.Frame(edit_client_root)
                edit_client_frame.pack(padx=10, pady=10)

                name_label = tkinter.Label(edit_client_frame, text='Name: ')
                name_label.grid(row=0, column=0)
                name_entry = tkinter.Entry(edit_client_frame)
                name_entry.grid(row=0, column=1)
                name_entry.insert(0, client_information[1])


                email_label = tkinter.Label(edit_client_frame, text='Email: ')
                email_label.grid(row=1, column=0)
                email_entry = tkinter.Entry(edit_client_frame)
                email_entry.grid(row=1, column=1)
                email_entry.insert(0, client_information[2])

                hourly_rate_label = tkinter.Label(edit_client_frame, text='Hourly rate: ')
                hourly_rate_label.grid(row=2, column=0)
                hourly_rate_entry = tkinter.Entry(edit_client_frame)
                hourly_rate_entry.grid(row=2, column=1)
                hourly_rate_entry.insert(0, client_information[3])

                save_changes_button = tkinter.Button(edit_client_frame, text='Save changes', command= save_changes)
                save_changes_button.grid(row=3, column=0, columnspan=2, sticky='news', pady=15)
            else:
                messagebox.showinfo(message='You must select a client.')



        # Main root GUI
        root = tkinter.Tk()
        root.title("Clients")
        root.geometry("650x370")

        frame = tkinter.Frame(root)
        frame.pack(padx=20, pady=10)

        clients_columns = ('name', 'email', 'hourly_rate')
        clients_treeview = ttk.Treeview(frame, columns=clients_columns, show="headings")
        clients_treeview.grid(row=0, column=0)
        clients_treeview.heading('name', text='Name')
        clients_treeview.heading('email', text='E-mail')
        clients_treeview.heading('hourly_rate', text='Hourly rate')

        new_client_button = tkinter.Button(frame, text="New Client", command=new_client)
        new_client_button.grid(row=1, column=0, padx=5, pady=5, sticky='news')

        remove_client_button = tkinter.Button(frame, text='Remove Client', command=remove_client_from_db)
        remove_client_button.grid(row=2, column=0, padx=5, pady=3, sticky='news')

        edit_client_button = tkinter.Button(frame, text='Edit Client', command=edit_client_in_DB)
        edit_client_button.grid(row=3, column=0, padx=5, pady=3, sticky='news')

        def display_clients_in_treeview():
                clients = fetch_items_from_db(shared.clients_db_path, 'client_list')

                for client in clients:
                    client_id = client[0]
                    clients_treeview.insert('', 0, iid=client_id, values=(client[1], client[2], client[3]))
        
        #Display clients in treeview upon opening the Clients window
        display_clients_in_treeview()

        root.mainloop()
    main()