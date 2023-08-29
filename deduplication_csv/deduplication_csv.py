import pandas as pd

# Read the CSV files
file1 = pd.read_csv('~/Desktop/i_o/input/deduplication_csv/input_1.csv')
file2 = pd.read_csv('~/Desktop/i_o/input/deduplication_csv/input_2.csv')

# Find entries in file2 that are not in file1 based on email
entries_not_in_file1 = file2[~file2['company email'].isin(file1['company email'])]

# Save the filtered entries to a new CSV file
entries_not_in_file1.to_csv('~/Desktop/i_o/output/deduplication_csv/output.csv', index=False)

# Print Console Log
print('Output Generated')