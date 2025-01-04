# Step 2: Inspect the structure of the CSV file (headers, delimiters, line endings, etc.)
import csv
file_path = "/home/zethic/Downloads/payin_Ashwajit Kamble_20_12_2024_20_12_2024_RP481813838269.csv"
# Read the first few rows to check for issues with delimiters or formatting
with open(file_path, 'r', newline='') as file:
    lines = file.readlines()

# Analyze the first few rows of the CSV
lines[:10]  # Display the first 10 lines for inspection

print(lines)


# Let's inspect the uploaded CSV file to check for potential issues like encoding, line endings, delimiters, and overall structure.

# file_path = '/mnt/data/payin_Ashwajit Kamble_20_12_2024_20_12_2024_RP559275394362.csv'

# Step 1: Check the encoding of the file
import chardet

with open(file_path, 'rb') as file:
    raw_data = file.read()
    encoding_info = chardet.detect(raw_data)

# print(encoding_info)



# Step 3: Check line endings in the file
import os

# Open the file in binary mode to check for line ending characters
with open(file_path, 'rb') as file:
    raw_data = file.read()

line_endings = raw_data.count(b'\r\n'), raw_data.count(b'\n'), raw_data.count(b'\r')
# print(line_endings)


# Step 4: Validate that all rows have the correct number of fields
validation_results = []

with open(file_path, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    header_length = len(next(reader))  # Get the number of columns in the header row
    
    for row_num, row in enumerate(reader, start=2):  # Start from line 2 (data rows)
        validation_results.append((row_num, len(row) == header_length, row))

# Check for rows that don't match the header column count
invalid_rows = [result for result in validation_results if not result[1]]
# print(header_length, invalid_rows)

