import os
selected_date = None
selected_client = None

base_json_files_path = "/root/workspace/github.com/DominikHrdonka/Invoice_generator/json_files/"
base_databases_path = "/root/workspace/github.com/DominikHrdonka/Invoice_generator/databases/"

stored_totals_json_path = os.path.join(base_json_files_path, 'stored_totals.json')
shared_data_json_path = os.path.join(base_json_files_path, 'shared_data.json')

clients_db_path = os.path.join(base_databases_path, 'clients.db')
invoices_db_path = os.path.join(base_databases_path, 'invoices.db')