import pandas as pd
import os

def filter_csv_by_category():
    # Get user input for the csv path
    csv_path = input("Enter the CSV file path: ").strip('"')
    
    # Check if file exists
    if not os.path.exists(csv_path):
        print("Error: The file does not exist.")
        return
    
    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path)
        
        # Ensure the column "Category" is present
        if "Category" not in df.columns:
            print("Error: The CSV file does not contain a 'Category' column.")
            return
        
        # Get the directory of the original CSV file
        output_dir = os.path.dirname(csv_path)
        
        # Group the data by the "Category" column
        grouped = df.groupby("Category")
        
        # Save each category to a new CSV file
        for category, group in grouped:
            # Create a valid filename for the category
            safe_category = str(category).encode('ascii', 'ignore').decode().replace("/", "_")  # Replace any problematic characters
            output_file = os.path.join(output_dir, f"{safe_category}.csv")
            group.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"Saved category '{category}' to '{output_file}'")
        
        print("All categories have been saved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filter_csv_by_category()
