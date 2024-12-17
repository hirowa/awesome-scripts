import os
import requests
import time
import json
import re

# Constants
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "<put_your_api_key_here>"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
DATA_TEMPLATE = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Based on the file's context provided by the user, provide a short and descriptive name (Max. 6 words) for that file and nothing else. All new names in English!!"
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    "temperature": 0.0,
    "max_tokens": 50,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

def find_txt_files(directory):
    """Recursively find all .txt files in the given directory."""
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files

def read_characters(file_path, start=0, length=500):
    """Read a specific number of characters starting from a position in a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        file.seek(start)
        return file.read(length)

def send_api_request(file_name, context):
    """Send a POST request to the API and return the response content."""
    data = DATA_TEMPLATE.copy()
    data["messages"][1]["content"] = f"File name: {file_name}\nContent: {context}"
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def sanitize_filename(filename):
    """Sanitize the filename by removing any invalid characters for Windows."""
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def rename_file(file_path, new_name):
    """Rename the file, retry if the name already exists."""
    directory, old_file_name = os.path.split(file_path)
    parent_folder_name = os.path.basename(directory)
    sanitized_new_name = sanitize_filename(new_name)
    new_file_name = f"{parent_folder_name}-{sanitized_new_name}.txt"
    new_file_path = os.path.join(directory, new_file_name)
    
    if not os.path.exists(new_file_path):
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_path}' to '{new_file_path}'")
        return True
    else:
        print(f"File '{new_file_path}' already exists.")
        return False

def log_failed_file(file_path):
    """Log the failed file path to a file."""
    with open('failed_logs.txt', 'a') as log_file:
        log_file.write(f"{file_path}\n")

def main():
    # Get current working directory
    current_directory = os.getcwd()
    
    # Find all .txt files
    txt_files = find_txt_files(current_directory)
    
    for txt_file in txt_files:
        retries = 0
        success = False
        start_position = 0

        while retries < 2 and not success:
            # Read next 500 characters
            file_content = read_characters(txt_file, start=start_position, length=500)
            file_name = os.path.basename(txt_file)
            
            # Send API request and get the new name
            new_name = send_api_request(file_name, file_content)
            
            if new_name:
                # Attempt to rename the file
                success = rename_file(txt_file, new_name)
                if success:
                    break
            
            # Update for the next retry
            retries += 1
            start_position += 500
            
            # Wait for 2 seconds before the next request
            time.sleep(2)
        
        if not success:
            print(f"Failed to rename file '{txt_file}' after {retries} attempts.")
            log_failed_file(txt_file)

if __name__ == "__main__":
    main()
