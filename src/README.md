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
- create interface to delete a client, edit a client from DB

# Final files
- make it executible file
- automate printing new invoice to PDF

# Fine tuning
- review functions across projects and get rid of redundancies (especially database related functions)

