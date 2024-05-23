import json
import os
from datetime import datetime

# Data to be written if json file doesn't exist yet
dictionary = {
	"total_curr_year": 120497.55
}

if not os.path.exists("stored_totals.json"):
	#creating json object
	json_object = json.dumps(dictionary, indent=4)

	# creating json file
	with open("stored_totals.json", "w") as outfile:
		outfile.write(json_object)
	

# Modifying json data
def modify_stored_totals(key, value):
	
	# Reading file data
	with open("stored_totals.json", "r") as infile:
		stored_totals = json.load(infile)
	
	#Modify data
	stored_totals[key] += value
	
    # Write the data
	with open("stored_totals.json", "w") as outfile:
		json.dump(stored_totals, outfile, indent=4) 

def save_total_per_month(value):
	current_month = datetime.now().strftime("%B")
	monthly_totals_dictionary = {}

	#If not exist, create json file
	if not os.path.exists("totals_per_month.json"):
		#creating json object
		total_per_month_object = json.dumps(monthly_totals_dictionary, indent=4)

		# creating json file
		with open("totals_per_month.json", "w") as outfile:
			outfile.write(total_per_month_object)

	#Open existing json file
	with open("totals_per_month.json", "r") as infile:
		stored_monthly_totals = json.load(infile)

	#Updating data based on the current month key existence
	if current_month not in stored_monthly_totals:
		stored_monthly_totals[current_month] = value
	else:
		stored_monthly_totals[current_month] += value

	#Write back the updated data
	with open("totals_per_month.json", "w") as outfile:
		json.dump(stored_monthly_totals, outfile, indent=4)

	
