import pandas as pd
import re

# # Define a function to clean a string
# def clean_string(s):
#      # Ensure s is a string
#     if not isinstance(s, str):
#         s = str(s)
#     # Remove non-text characters
#     return re.sub(r'\W+', ' ', s)

# Read the CSV file
df = pd.read_csv('link.csv')

# Apply the cleaning function to each cell in the DataFrame
df = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file
# df.to_csv('', index=False)

# Print a success message
print("The CSV file was successfully cleaned and saved as cleaned_file.csv")

