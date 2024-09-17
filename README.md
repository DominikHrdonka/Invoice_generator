Invoicing system for creating new invoices according to the customer type and keeping track of issued invoices and overall summary.

GUI is built with tkinter module.

Invoices are generated using .docx templates and docxtpl module.

JSON file is used to store overview data (e.g. invocies issued in given months and years, the total amount of issued invoices etc.)

SQLite is used to manage database of generated invoices with all the relevant data (mainly invoice number, paid/unpaid, clients etc.)
