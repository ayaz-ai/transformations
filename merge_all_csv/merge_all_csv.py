import os
import pandas as pd

# Set the path to the folder containing CSV files
folder_path = '..\\Manufacturing\\Batch'

# List to hold DataFrames of all CSV files
dfs = []

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, header=None)
        dfs.append(df)
        # print(dfs)

# Combine all DataFrames into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Set the path for the output merged CSV file
output_csv_path = 'merged_output.csv'

# Write the merged DataFrame to a CSV file
merged_df.to_csv(output_csv_path, index=False, header=False)

print("CSV files merged successfully.")
