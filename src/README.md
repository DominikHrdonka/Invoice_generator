# Invoice_generator

Invoicing system for creating new invoices according to the customer type and keeping track of issued invoices and overall summary.

GUI is built with tkinter module.

Invoices are generated using .docx templates and docxtpl module.

JSON file is used to store overview data (e.g. invocies issued in given months and years, the total amount of issued invoices etc.)

SQLite is used to manage database of generated invoices with all the relevant data (mainly invoice number, paid/unpaid etc.)


# Things to be done:

# QR
- add function to generate unique QR code
- place the QR code in the document

# Concepts
- make it able to create concepts (storing incomplete files??)

# Overview

# DB
*Create clients DB*
- create new DB table "clients"
- create interface to add a new client, delete a client, edit a client etc.

*Choose clients based on database*
- create interface to add new clients to a DB
- create button to open the listbox (en tab, Client field) + assign function open_client_listbox
- create function to fetch the data from DB (could we use existing fetch function from summary?? --> it could be moved to databases.py and made more reusable)
- create button to pass the selected client into the Client field (en tab)

# Final files
- make it executible file
- automate printing new invoice to PDF

# Fine tuning
- review functions across projects and get rid of redundancies (especially database related functions)

