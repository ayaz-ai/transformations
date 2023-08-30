# /home/ayaz/Desktop/i_o/output/json_email_segregation/output_with_email.csv

import pandas as pd

# Read the CSV file
file_path = "/home/ayaz/Desktop/i_o/output/json_email_segregation/output_with_email.csv"  # Replace with the actual file path
output_file_path = "/home/ayaz/Desktop/i_o/input/proxy_curl/input.csv"  # Replace with the desired output file path
column_names = [
    "LinkedIn Profile URL", "email", "name", "title", "company_name",
    "website", "hq_phone", "industry", "company_size", "headquaters"
]

df = pd.read_csv(file_path, usecols=[0], names=column_names, skiprows=1)

# Extract the "LinkedIn Profile URL" column without header
linkedin_urls = df["LinkedIn Profile URL"]

# Create a new DataFrame with just the "LinkedIn Profile URL" column
output_df = pd.DataFrame({"LinkedIn Profile URL": linkedin_urls})

# Save the new DataFrame to a CSV file without the index column
output_df.to_csv(output_file_path, index=False, header=False)

print(f"LinkedIn Profile URLs saved to {output_file_path}")