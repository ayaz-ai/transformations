import pandas as pd
import ast

# Read the CSV file
df = pd.read_csv('/home/ayaz/Desktop/i_o/output/proxy_curl/output.csv')

# Convert the string representation of the list to an actual list
df['Number'] = df['Number'].apply(ast.literal_eval)

# Extract only the first 3 values from the list in the 'Number' column
df['Mobile'] = df['Number'].apply(lambda x: x[0] if len(x) > 0 else None)
df['Mobile2'] = df['Number'].apply(lambda x: x[1] if len(x) > 1 else None)
df['Mobile3'] = df['Number'].apply(lambda x: x[2] if len(x) > 2 else None)

# Drop the original 'Number' column
df.drop('Number', axis=1, inplace=True)

# Save the resulting DataFrame to a new CSV file
df.to_csv('/home/ayaz/Desktop/i_o/output/pre_merger/output.csv', index=False)

print("Output saved to 'output.csv'")
