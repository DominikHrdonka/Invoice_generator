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
    - display relevant data (even invoices from the db)
    - DB
        - we have to fetch and display only invoices FROM THE GIVEN YEAR
            - 1. fetch the invoices using issued_on (specify the year)
            - 2. delete the existing treeview content
            - 3. insert the fetched data
            - 4. include it under the button clicked function
        - also a possibility to display all invoices regardless the year??
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

