import os
import time
import anthropic
import pandas as pd

# API Setup with hardcoded key
API_KEY = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Anthropic(api_key=API_KEY)

def call_api(prompt):
    """
    Call the Anthropic API with the provided prompt.
    """
    try:
        message = client.messages.create(
            model="claude-3-opus-latest",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error calling API: {e}")
        return f"Error: {str(e)}"

def process_csv(input_file):
    """
    Process each row of the CSV, call the API, and save the output.
    """
    try:
        df = pd.read_csv(input_file)
        
        # Check if the required columns are present
        required_columns = [
            'Simple Prompt', 'Efficient Prompt', 'Detailed Prompt', 'Agent Prompt',
            'Simple Ans', 'Efficient Ans', 'Detailed Ans', 'Agent Ans'
        ]
        
        for col in required_columns:
            if col not in df.columns:
                df[col] = ''
        
        # Process each prompt column
        prompt_columns = ['Simple Prompt', 'Efficient Prompt', 'Detailed Prompt', 'Agent Prompt']
        answer_columns = ['Simple Ans', 'Efficient Ans', 'Detailed Ans', 'Agent Ans']
        
        for prompt_col, answer_col in zip(prompt_columns, answer_columns):
            for index, row in df.iterrows():
                if pd.isna(row[answer_col]) or row[answer_col] == '':
                    prompt = row[prompt_col]
                    if pd.notna(prompt) and prompt.strip() != '':
                        print(f"Processing row {index + 1} ({prompt_col}): Sending API request...")
                        response = call_api(prompt)
                        df.at[index, answer_col] = response
                        df.to_csv(input_file, index=False)
                        time.sleep(60 / 4800)  # Rate limit: 4800 requests per minute
        
        print("Processing complete. Updated CSV saved.")
        return True
    
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return False

def main():
    try:
        # Get input file path
        input_csv = input("Enter the path to the input CSV file: ").strip().strip('"')
        input_csv = os.path.normpath(input_csv)
        
        if not os.path.exists(input_csv):
            print(f"Error: File '{input_csv}' does not exist.")
            return
        
        if process_csv(input_csv):
            print("Script finished execution successfully.")
        else:
            print("Script finished with errors.")
    
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()