import json
import os
from datetime import datetime

# Data to be written if json file doesn't exist yet
dictionary = {
	"total_curr_year": 120497.55
}


def save_totals(value):

	current_year = datetime.now().strftime("%Y")
	current_month = datetime.now().strftime("%B")

	totals_dictionary = {}

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

	
