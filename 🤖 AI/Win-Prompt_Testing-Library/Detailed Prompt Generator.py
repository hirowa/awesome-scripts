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

def generate_prompt(title):
    """
    Create the prompt for the API call based on given parameters.
    """
    return f'''
    Convert the [User Agent Prompt] into a normal prompt. 
    ALWAYS in 3 80-word-paragraphs with as much information as possible. Make it readable.
    ALWAYS start your response with the following string: "Act as"
    Always end your response with the following string in a completely new line: "Answer with a leading assistance question something like, e.g. 'As a teacher, how can I help you today?'"
    ---
    [User Agent Prompt]
    {title}
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
            max_tokens=6384,
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
    if 'Column 2' not in df.columns:
        df['Column 2'] = ''
    
    def process_row(row):
        if pd.notna(row['Column 2']) and row['Column 2'] != '':
            return row['Column 2']  # Skip already processed rows

        title = row['Column 1']
        
        prompt = generate_prompt(title)
        print(f"Processing row {row.name + 1}: Sending API request...")
        response = call_api(prompt)
        # Save CSV after processing each row
        df.at[row.name, 'Column 2'] = response
        df.to_csv(input_file, index=False)
        time.sleep(REQUEST_INTERVAL)  # Respect rate limits
        return response
    
    df.apply(lambda row: process_row(row) if pd.isna(row['Column 2']) or row['Column 2'] == '' else row['Column 2'], axis=1)
    
if __name__ == "__main__":
    process_csv(input_csv)
    print("Processing complete. Updated CSV saved.")
