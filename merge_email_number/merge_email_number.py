import pandas as pd

# Load the CSV files into dataframes
df1 = pd.read_csv('/home/ayaz/Desktop/i_o/output/json_email_segregation/output_with_email.csv')
df2 = pd.read_csv('/home/ayaz/Desktop/i_o/output/pre_merger/output.csv')

# Merge the dataframes based on the common column "LinkedIn Profile URL"
merged_df = df1.merge(df2, on='LinkedIn Profile URL', how='inner')

# Save the merged dataframe to a new CSV file
merged_df.to_csv('/home/ayaz/Desktop/i_o/output/merged/output.csv', index=False)
