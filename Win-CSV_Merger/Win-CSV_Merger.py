import os
import pandas as pd

# Get the current working directory
directory = os.getcwd()

# List to hold all DataFrames
csv_list = []

# Loop through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        csv_list.append(df)
        print(f"Added file: {filename}")

# Concatenate all DataFrames in the list
merged_df = pd.concat(csv_list, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_csv_path = os.path.join(directory, "merged_output.csv")
merged_df.to_csv(merged_csv_path, index=False)

print(f"All CSV files merged into {merged_csv_path}!")
