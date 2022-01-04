# Script needs to read in the module_data csv file and store all module codes in a list
# It then needs to iterate 1000 times, each time it needs to add a random number of module codes from the list into a new list.
# Then, a new csv file needs to be created and in each row, you need to add the module codes selected in the previous section

import csv
import random

# Create a list to store the module codes
MODULE_CODES = []

# Get the module codes from the module_data csv
with open("module_data.csv", "r") as f1:
    csvreader = csv.reader(f1)

    # Get field names
    fields = next(csvreader)

    # Extract the module code from each row
    for row in csvreader:
        MODULE_CODES.append(row[0])


modules = []
# Create a list that will store the random module code choices
for i in range(1000):
    num_modules = random.randint(1, len(MODULE_CODES))
    module_choice_list = random.sample(MODULE_CODES, num_modules)
    modules.append(" | ".join(module_choice_list))


# Write these module choices into a CSV
with open("module_choices.csv", "w") as f2:
    for line in modules:
        f2.write(str(line) + "\n")
