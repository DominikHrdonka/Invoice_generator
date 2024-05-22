import json
import os

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
	
# Retrieving json data
with open("stored_totals.json", "r") as infile:
	stored_totals = json.load(infile)

# Modifying json data
def modify_stored_totals(key, value):
	# Reading file data
	with open("stored_totals.json", "r") as infile:
		stored_totals = json.load(infile)
	#Modyfying file data
	stored_totals[key] += value
	
    # Write the data
	with open("stored_totals.json", "w") as outfile:
		json.dump(stored_totals, outfile, indent=4) 

