import os
import time
from openai import OpenAI
import pandas as pd
import tempfile
import shutil

# API Setup
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.getenv('OPENAI_API_KEY'),
)

# Input CSV file
input_csv = os.path.normpath(input("Enter the path to the input CSV file: "))

# API Rate Limits (modify these to suit your usage limits)
REQUESTS_PER_MINUTE = 4800  # 5,000 requests per minute (as per gpt-4o-mini limits)
REQUEST_INTERVAL = 60 / REQUESTS_PER_MINUTE

def generate_prompt(title, description, category, tags):
    """
    Create the prompt for the API call based on given parameters.
    """
    return f'''
    [Your Prompt Here]
    ---
    [Request]
    Title: {title}
    Description: {description}
    Category: {category}
    Tags: {tags}
    '''

def call_api(prompt):
    """
    Call the OpenAI API with the generated prompt.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=16384,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.2
        )
        return response.choices[0].message.content.strip()
    except client.error.OpenAIError as e:
        print(f"Request failed: {e}")
        return "Error in generating response."
    except KeyError as e:
        print(f"Key error: {e} in response")
        return "Error in parsing API response."
    except Exception as e:
        print(f"Error calling API: {e}")
        return "Error"

def process_csv(input_file):
    """
    Process each row of the CSV, call the API, and save the output.
    """
    df = pd.read_csv(input_file)
    if 'Column 5' not in df.columns:
        df['Column 5'] = ''
    
    def process_row(row):
        if pd.notna(row['Column 5']) and row['Column 5'] != '':
            return row['Column 5']  # Skip already processed rows

        title = row['Column 1']
        description = row['Column 2']
        category = row['Column 4']
        tags = row['Column 3']
        
        prompt = generate_prompt(title, description, category, tags)
        print(f"Processing row {row.name + 1}: Sending API request...")
        response = call_api(prompt)
        # Save CSV after processing each row
        df.at[row.name, 'Column 5'] = response
        df.to_csv(input_file, index=False)
        time.sleep(REQUEST_INTERVAL)  # Respect rate limits
        return response
    
    df.apply(lambda row: process_row(row) if pd.isna(row['Column 5']) or row['Column 5'] == '' else row['Column 5'], axis=1)
    
    

if __name__ == "__main__":
    process_csv(input_csv)
    print("Processing complete. Updated CSV saved.")
