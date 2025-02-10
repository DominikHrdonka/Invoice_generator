# Things to be done:

# QR
- add function to generate unique QR code
- place the QR code in the document

# Concepts
- make it able to create concepts (storing incomplete files??)

# Clients
- align displayed data in treeview to center

# Summary
- DISPLAY PREVIOUS YEARS' DATA
    - need to create window to view previous years' summaries

- DISPLAYED INVOICES
    - create buttons and functions to edit invoicec??
        - update the data in the DB accordingly
        
- 
- INVOICED PER MONTH --> use Czech format for displaying numbers
- add interface to support monthly summary for different years (past and current)
    - make the Invoiced per month a tree so that it can be easy to switch displayed data (the tree columns - months - stay the same)
    - create buttons to switch the display according to the selected year

- INVOICED THIS YEAR
    - use Czech format for displaying numbers

# json_data
- make shared_data_dictionary more dynamic, so that it resets the next_invoice_num and next_order_num when current_year changes

# Web migration
- transform the program to a web app?
- create a fork -- one stayes dektip program, the other web app

# Final files
- automate printing new invoice to PDF

# Fine tuning
- review functions across projects and get rid of redundancies (especially database related functions)

