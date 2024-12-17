import os
import fitz  # PyMuPDF
import requests
import json

# Constants for API call
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "<put_your_api_key_here>"  # Replace with your API key
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

# Function to extract text from a given page or range of pages in a PDF
def extract_text_from_pdf(pdf_path, start_page, end_page=None):
    try:
        doc = fitz.open(pdf_path)
        text = ""

        # Handle both single page and page range
        if end_page is None:
            # Single page case
            page = doc.load_page(start_page - 1)  # Pages are 0-indexed
            text = page.get_text()
        else:
            # Page range case
            for page_num in range(start_page - 1, end_page):  # Page numbers are 0-indexed
                page = doc.load_page(page_num)
                text += page.get_text()

        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

# Function to make the API call and return the "content" from "choices"
def make_api_call(content):
    data = DATA_TEMPLATE.copy()
    data['messages'][1]['content'] = content
    
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        # Extract the "content" field from the "choices"
        raw_content = response_json["choices"][0]["message"]["content"]
        
        # Clean the content by removing the backticks and stripping extra characters
        clean_content = raw_content.strip('```').strip()

        try:
            # Parse the cleaned content as JSON
            return json.loads(clean_content)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
        return None

# Function to save the parsed JSON content to a file
def save_json_to_file(file_path, json_data):
    try:
        # Save the cleaned and parsed content as a JSON file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)
        print(f"JSON file saved: {file_path}")
    except Exception as e:
        print(f"Error saving JSON file {file_path}: {e}")

# Main function to process a PDF and output the cleaned and parsed API content to a JSON file
def process_pdf(pdf_path):
    print(f"Processing {pdf_path}...")

    # Ask the user for page range or single page
    page_input = input("Enter the page number or page range (e.g., 1 or 1-5): ")

    try:
        # Check if it's a range or a single page
        if "-" in page_input:
            start_page, end_page = map(int, page_input.split('-'))
        else:
            start_page = int(page_input)
            end_page = None  # Indicating it's a single page
    except ValueError:
        print("Invalid input. Please enter a valid single page or page range.")
        return
    
    # Extract text from the given pages
    text_content = extract_text_from_pdf(pdf_path, start_page, end_page)
    if text_content is None:
        print(f"Skipping {pdf_path} due to extraction error.")
        return

    # Send the content to the API and get the cleaned and parsed content
    print(f"Sending content from pages {start_page}" +
          (f" to {end_page}" if end_page else "") + f" of {pdf_path} to API...")
    api_content = make_api_call(text_content)
    if api_content is None:
        print(f"Skipping {pdf_path} due to API error.")
        return

    # Save the parsed content to a JSON file
    output_filename = os.path.splitext(os.path.basename(pdf_path))[0] + "_api_content.json"
    output_filepath = os.path.join(os.getcwd(), output_filename)
    save_json_to_file(output_filepath, api_content)

if __name__ == "__main__":
    # Specify the PDF to process (you can modify this as needed)
    root_directory = os.getcwd()
    for filename in os.listdir(root_directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(root_directory, filename)
            process_pdf(pdf_path)
