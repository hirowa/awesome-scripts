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
input_csv = input("Enter the path to the input CSV file: ").strip().strip('"')
input_csv = os.path.normpath(input_csv)

# API Rate Limits (modify these to suit your usage limits)
REQUESTS_PER_MINUTE = 4800  # 5,000 requests per minute (as per gpt-4o-mini limits)
REQUEST_INTERVAL = 60 / REQUESTS_PER_MINUTE

def call_api(prompt):
    """
    Call the OpenAI API with the provided prompt.
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

    # Check if the required columns are present
    required_columns = [
        'Simple Prompt', 'Efficient Prompt', 'Detailed Prompt', 'Agent Prompt',
        'Simple Ans', 'Efficient Ans', 'Detailed Ans', 'Agent Ans'
    ]

    for col in required_columns:
        if col not in df.columns:
            df[col] = ''  # Add missing columns

    # Process each prompt column
    prompt_columns = ['Simple Prompt', 'Efficient Prompt', 'Detailed Prompt', 'Agent Prompt']
    answer_columns = ['Simple Ans', 'Efficient Ans', 'Detailed Ans', 'Agent Ans']

    for prompt_col, answer_col in zip(prompt_columns, answer_columns):
        for index, row in df.iterrows():
            # Only send API call if answer column is empty
            if pd.isna(row[answer_col]) or row[answer_col] == '':
                prompt = row[prompt_col]
                if pd.notna(prompt) and prompt.strip() != '':
                    print(f"Processing row {index + 1} ({prompt_col}): Sending API request...")
                    response = call_api(prompt)
                    df.at[index, answer_col] = response
                    # Save after each API call to avoid data loss
                    df.to_csv(input_file, index=False)
                    time.sleep(REQUEST_INTERVAL)  # Respect rate limits

    print("Processing complete. Updated CSV saved.")

if __name__ == "__main__":
    process_csv(input_csv)
    print("Script finished execution.")