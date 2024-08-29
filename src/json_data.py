import json
import os
from datetime import datetime

# Data to be written if json file doesn't exist yet
totals_dictionary = {
	"2024": {
		"January": 38718.19,
		"February": 24996.23,
		"March": 18293.72,
		"April": 18197.01,
		"May": 46903.23,
		"June": 26942.61,
		"July": 68687.44,
		"total_per_year": 252981.79
	}
}

current_year = datetime.now().strftime("%Y")
current_month = datetime.now().strftime("%B")

#If not exist, create json file
if not os.path.exists("stored_totals.json"):
	#creating json object
	stored_totals_obj = json.dumps(totals_dictionary, indent=4)

	# creating json file
	with open("stored_totals.json", "w") as outfile:
		outfile.write(stored_totals_obj)

#Open existing json file
with open("stored_totals.json", "r") as infile:
	stored_totals_data = json.load(infile)


def save_totals(value):

	#Updating data based on the current year and month key existence
	if current_year not in stored_totals_data:
		stored_totals_data[current_year] = {}
		stored_totals_data[current_year][current_month] = value
		stored_totals_data[current_year]["total_per_year"] = value

	else:
		if current_month in stored_totals_data[current_year]:
			stored_totals_data[current_year][current_month] += value
		else:
			stored_totals_data[current_year][current_month] = value

		stored_totals_data[current_year]["total_per_year"] += value


	#Write back the updated data
	with open("stored_totals.json", "w") as outfile:
		json.dump(stored_totals_data, outfile, indent=4)



shared_data_dictionary = {
	"next_invoice_num": 30,
	"next_order_num": 31
}

# If not exists, create json file
if not os.path.exists('shared_data.json'):
	shared_data_obj = json.dumps(shared_data_dictionary, indent=4)

	with open('shared_data.json', 'w') as file:
		file.write(shared_data_obj)

# Open existing json file
with open('shared_data.json', 'r') as infile:
	stored_shared_data = json.load(infile)

def update_next_invoice_num():
	stored_shared_data['next_invoice_num'] += 1
	
	#Writing back the updated date
	with open('shared_data.json', 'w') as outfile:
		json.dump(stored_shared_data, outfile, indent=4)

def update_next_order_num():
	stored_shared_data['next_order_num'] += 1

	#Writing back the updated date
	with open('shared_data.json', 'w') as outfile:
		json.dump(stored_shared_data, outfile, indent=4)