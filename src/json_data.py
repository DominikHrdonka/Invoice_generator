import json
import os
from datetime import datetime
import shared

# Data to be written if json file doesn't exist yet
# This will be here only temporarily for the sake of testing the app.
# This is important data, later on IT WILL NOT BE HARDCODED. It will read the data from a safely saved file (cloud??)
totals_dictionary = {
    "2024": {
        "January": 38718.19,
        "February": 24996.23,
        "March": 18293.72,
        "April": 18197.01,
        "May": 46903.23,
        "June": 26942.61,
        "July": 48254.14,
        "August": 67839.98,
        "September": 20000.0,
        "October": 40000.0,
        "total_per_year": 560144.11
    },
    "2025": {
        "January": 28148.88,
        "February": 19150.40,
		"total_per_year": 47299.28
    },
	"total_for_all_years": 607443.39
}

current_year = datetime.now().strftime("%Y")
current_month = datetime.now().strftime("%B")


"""
Function to be called upon opening the program to create give json.files with given source dict.
"""
def create_json_file_if_not_exist(file, source_dictionary):
	if not os.path.exists(file):
		file_object = json.dumps(source_dictionary, indent=4)
	
		with open(file, 'w') as outfile:
			outfile.write(file_object)

# Read data from given file
def read_json_file(file):
	with open(file, 'r') as infile:
		return json.load(infile)

#Creating stored_totals.json if not exist	
create_json_file_if_not_exist(shared.stored_totals_json_path, totals_dictionary)
	

"""
This function below must contain read_json_file function otherwise it would not be able to save data
in it.
"""

def save_totals(value):

	stored_totals_data = read_json_file(shared.stored_totals_json_path)

	#Updating data based on the current year and month key existence
	if current_year not in stored_totals_data:
		stored_totals_data[current_year] = {}
		stored_totals_data[current_year][current_month] = value
		stored_totals_data[current_year]["total_per_year"] = value
		stored_totals_data['total'] = value

	else:
		if current_month in stored_totals_data[current_year]:
			stored_totals_data[current_year][current_month] += value
		else:
			stored_totals_data[current_year][current_month] = value

		stored_totals_data[current_year]["total_per_year"] += value
		stored_totals_data['total_for_all_years'] += value


	#Write back the updated data
	with open(shared.stored_totals_json_path, "w") as outfile:
		json.dump(stored_totals_data, outfile, indent=4)


#Keeping track of invoice and order numbers
# could make this more dynamic. E.G. reset the number once current_year changes.
shared_data_dictionary = {
	"next_invoice_num": 31,
	"next_order_num": 32
}

create_json_file_if_not_exist(shared.shared_data_json_path, shared_data_dictionary)


def update_next_invoice_num():
	stored_shared_data = read_json_file(shared.shared_data_json_path)
	stored_shared_data['next_invoice_num'] += 1
	
	#Writing back the updated date
	with open(shared.shared_data_json_path, 'w') as outfile:
		json.dump(stored_shared_data, outfile, indent=4)

def update_next_order_num():
	stored_shared_data = read_json_file(shared.shared_data_json_path)
	stored_shared_data['next_order_num'] += 1

	#Writing back the updated date
	with open(shared.shared_data_json_path, 'w') as outfile:
		json.dump(stored_shared_data, outfile, indent=4)