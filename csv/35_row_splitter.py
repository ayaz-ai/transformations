import pandas as pd
import os

# Set the path to the input CSV file
input_csv_path = 'temp_csv.csv'

# Create a directory to store the output CSV files
output_dir = '.\\output_csv_files'
os.makedirs(output_dir, exist_ok=True)

# Read the input CSV file in chunks
chunk_size = 35
reader = pd.read_csv(input_csv_path, chunksize=chunk_size)

# Counter for naming the output CSV files
file_counter = 1

for chunk in reader:
    # Generate output CSV file path
    output_csv_path = os.path.join(output_dir, f'output_{file_counter}.csv')

    # Write the chunk to the output CSV file
    chunk.to_csv(output_csv_path, index=False)

    file_counter += 1

print("CSV file splitting completed.")
