import os
import pandas as pd
import shutil
import requests
import re  # Import regex module to sanitize filenames

# Constants for the API
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "<your_api_key_here>"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Function to send a request to the API and get a descriptive summary
def get_summary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        section_content = file.read()

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "<prompt_here>"
            },
            {
                "role": "user",
                "content": section_content
            }
        ],
        "temperature": 0.7,
        "max_tokens": 16383,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.2
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()

        # Extract the generated text
        summary = result['choices'][0]['message']['content'].strip()
        return summary
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return "Error in generating summary."
    except KeyError as e:
        print(f"Key error: {e} in response {result}")
        return "Error in parsing API response."

# Function to sanitize filenames by removing invalid characters
def sanitize_filename(name):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', name)

# Function to process each CSV file
def process_csv(file_path):
    print(f"Processing file: {file_path}")
    df = pd.read_csv(file_path)

    # Create a directory for the CSV
    folder_name = os.path.splitext(os.path.basename(file_path))[0]
    os.makedirs(folder_name, exist_ok=True)

    # Move the CSV file to the folder
    shutil.move(file_path, os.path.join(folder_name, os.path.basename(file_path)))
    print(f"Moved {file_path} to {folder_name}/")

    # Clean up the 'Category' column to handle NaN values
    df['Category'] = df['Category'].fillna('').astype(str).str.strip().str.lower()

    # Stop processing when we encounter an empty 'Course' row
    df = df[df['Course'].notna()]

    # Find unique categories and their starting indices
    category_indices = {}
    unique_categories = []
    
    for i, row in df.iterrows():
        category = row['Category']
        
        if not category:
            continue
        
        if category not in category_indices:
            category_indices[category] = []
            unique_categories.append(category)

        category_indices[category].append(i)

    # Prepare sections based on the unique categories and their ranges
    sections = []
    previous_category = None
    merged_introduction = False
    temp_files = []

    for i, category in enumerate(unique_categories):
        if category == 'introduction':
            # If Introduction, don't add it immediately, but prepare to merge with the next category
            merged_introduction = True
            continue
        
        if category == 'conclusion':
            # Merge Conclusion with the previous unique category
            if previous_category is not None:
                start_index = category_indices[category][0]
                end_index = category_indices[category][-1] + 1
                sections[-1] = (sections[-1][0], pd.concat([sections[-1][1], df.iloc[start_index:end_index]]))
            continue

        # Regular category processing
        if merged_introduction:
            # Merge Introduction with the next unique category
            intro_start_index = category_indices['introduction'][0]
            intro_end_index = category_indices[category][-1] + 1
            sections.append((category, df.iloc[intro_start_index:intro_end_index]))
            merged_introduction = False  # Reset the flag after merging
        else:
            # Normal section without 'Introduction'
            start_index = category_indices[category][0]
            end_index = category_indices[category][-1] + 1
            sections.append((category, df.iloc[start_index:end_index]))
        
        previous_category = category

    # List all sections found
    print("\nSections found:")
    for idx, (category, _) in enumerate(sections):
        print(f"Section {idx + 1}: Category - {category.title() if category else 'Unknown'}")

    # Process each section
    for idx, (category, section_df) in enumerate(sections):
        print(f"\nProcessing section {idx + 1} for category: {category.title() if category else 'Unknown'}")
        section_content = section_df.to_string(index=False, columns=['Course', 'Category', 'Class', 'Transcript'])
        
        # Sanitize the category to create valid filenames
        sanitized_category = sanitize_filename(category if category else 'Unknown')
        
        # Create a sanitized temporary file name for the section
        temp_filename = sanitize_filename(f"temp_{sanitized_category}.txt")
        
        # Ensure the filename is sanitized correctly
        with open(temp_filename, 'w', encoding='utf-8') as temp_file:
            temp_file.write(section_content)
        print(f"Created temporary file: {temp_filename}")

        # Store the temp file name for possible deletion later
        temp_files.append(temp_filename)

        # Call API to get a descriptive summary for this section
        summary = get_summary(temp_filename)
        print(f"Received summary: {summary}")

        # Save API response (summary) to a markdown file
        markdown_filename = os.path.join(folder_name, sanitize_filename(f"{category.title() if category else 'Unknown'}.md"))
        
        with open(markdown_filename, 'w', encoding='utf-8') as md_file:
            md_file.write(summary)
        print(f"Saved markdown file: {markdown_filename}")

    # Comment out the user prompt and deletion of temporary files
    # delete_temp_files = input("Do you want to delete temporary files? (y/n): ").strip().lower()
    
    # if delete_temp_files == 'y':
    #     for temp_file in temp_files:
    #         os.remove(temp_file)
    #         print(f"Deleted temporary file: {temp_file}")
    # else:
    #     print("Temporary files were not deleted.")

# Main script logic
def main():
    current_dir = os.getcwd()
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]

    print(f"Found {len(csv_files)} CSV file(s) in the current directory.")

    for csv_file in csv_files:
        file_path = os.path.join(current_dir, csv_file)
        process_csv(file_path)

    print("Processing complete.")

if __name__ == "__main__":
    main()
