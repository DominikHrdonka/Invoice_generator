import json

# Data to be written
dictionary = {
	"total_curr_month": 120497.55
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
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
	stored_totals[key] = value
	
    # Write the data
	with open("stored_totals.json", "w") as outfile:
		json.dump(stored_totals, outfile, indent=4) 

