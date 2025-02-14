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
- SUMMARY ACCORDING TO THE SELECTED YEAR
    - DB
        - also a possibility to display all invoices regardless the year
            - make it a DEFAULT OPTION so when opening the summary, this function will be used
            - make it to change the 'Invoiced in' to 'Invoiced totally'
                - need to add new key:value pair in stored_totals.json to reflect total price for
                ALL THE YEARS
            - maybe make a filter or a search bar??? 

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

