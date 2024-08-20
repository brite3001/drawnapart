import os
import csv

# Path to your subfolder
subfolder_path = "asus_timing_data/"

# Get a list of all files in the directory that end with '.txt'
text_files = [f for f in os.listdir(subfolder_path) if f.endswith(".txt")]

# Open a CSV file to write to
with open("asus_timing.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # setup column headers
    column_names = ["label"]
    for i in range(1024):
        column_names.append(f"Feature {i}")

    writer.writerow(column_names)

    # Loop over each file
    for filename in text_files:
        # Construct full file path
        file_path = os.path.join(subfolder_path, filename)

        # Open the file and read its content
        with open(file_path, "r") as file:
            # Read all lines into a list
            lines = file.readlines()

        # Convert each line to a float and write it to the CSV file
        row = [float(line) for line in lines]
        row.insert(0, "asus_laptop")
        writer.writerow(row)
