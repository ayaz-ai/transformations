import pandas as pd
import os
import json
import re

# Path to the folder containing JSON files
json_folder = "/home/ayaz/Desktop/i_o/input/json_email_segregation/"  # Replace with the actual path to your JSON folder

# Initialize empty lists and a set to store processed URLs
dataframes_with_email = []
dataframes_without_email = []
processed_urls = set()

# Process each JSON file in the folder
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        json_file_path = os.path.join(json_folder, filename)
        with open(json_file_path, 'r') as f:
            json_data = f.readlines()
            for line in json_data:
                data_dict = json.loads(line)  # Convert JSON string to dictionary
                url = list(data_dict.keys())[0]  # Get the LinkedIn Profile URL
                if url not in processed_urls:  # Check for duplicates
                    data = pd.DataFrame.from_dict(data_dict, orient='index')
                    processed_urls.add(url)  # Add URL to the set of processed URLs
                    if data['email'].values[0] != 'No Email':
                        dataframes_with_email.append(data)
                    else:
                        dataframes_without_email.append(data)

# Combine DataFrames
combined_df_with_email = pd.concat(dataframes_with_email)
combined_df_without_email = pd.concat(dataframes_without_email)

# Extract higher range value from company_size and convert to integer
def extract_company_size(value):
    if value == 'NULL':
         return None
    elif '+' in value:
        return int(re.search(r'\d+', value).group())  # Extract the numeric part
    else:
        return int(value.split('-')[-1].replace(' employees', '').replace(',', ''))

combined_df_with_email['company_size'] = combined_df_with_email['company_size'].apply(extract_company_size)
combined_df_without_email['company_size'] = combined_df_without_email['company_size'].apply(extract_company_size)

# Save DataFrames to CSV files
csv_file_with_email = "/home/ayaz/Desktop/i_o/output/json_email_segregation/output_with_email.csv"  # Replace with the desired path for the CSV output file with email
csv_file_without_email = "/home/ayaz/Desktop/i_o/output/json_email_segregation/output_without_email.csv"  # Replace with the desired path for the CSV output file without email

combined_df_with_email.to_csv(csv_file_with_email, index_label='LinkedIn Profile URL')
combined_df_without_email.to_csv(csv_file_without_email, index_label='LinkedIn Profile URL')

print("CSV files saved:")
print("With Email:", csv_file_with_email)
print("Without Email:", csv_file_without_email)
