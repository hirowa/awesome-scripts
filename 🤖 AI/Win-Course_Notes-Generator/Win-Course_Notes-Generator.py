import os
import fitz  # PyMuPDF
import requests
import time

# Constants for API call
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = os.getenv('OPENAI_API_KEY'),
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

DATA_TEMPLATE = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "<put_prompt_here>"
            },
        {
            "role": "user",
            "content": ""
        }
    ],
    "temperature": 0.7,
    "max_tokens": 16383,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.2
}

# Function to convert PDF to text
def pdf_to_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error converting {pdf_path} to text: {e}")
        return None

# Function to make API call
def make_api_call(content):
    data = DATA_TEMPLATE.copy()
    data['messages'][1]['content'] = content
    
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
        return None

# Function to save text to a file
def save_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

# Main function to process PDFs
def process_pdfs(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(foldername, filename)
                print(f"Processing {pdf_path}")

                # Convert PDF to text
                text_content = pdf_to_text(pdf_path)
                if text_content is None:
                    print(f"Skipping {pdf_path} due to conversion error.")
                    continue
                
                # Send content to API
                print(f"Sending content of {pdf_path} to API...")
                api_result = make_api_call(text_content)
                if api_result is None:
                    print(f"Skipping {pdf_path} due to API error.")
                    continue

                # Save API result to a new file
                output_filename = f"{os.path.splitext(filename)[0]}-AI.txt"
                output_path = os.path.join(foldername, output_filename)
                save_text_to_file(output_path, api_result)
                print(f"API result saved to {output_path}")

                # Ensure not to exceed rate limits
                time.sleep(1)  # Delay to avoid rate limit issues

if __name__ == "__main__":
    # Define the root directory to search for PDFs
    root_directory = os.getcwd()
    
    print(f"Starting PDF processing in directory: {root_directory}")
    process_pdfs(root_directory)
    print("Processing completed.")