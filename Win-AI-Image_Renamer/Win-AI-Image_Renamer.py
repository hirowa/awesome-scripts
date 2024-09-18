import os
import base64
import requests
import time

# Constants for API call
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "<your_api_key_here>"  # Add your API key here
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Function to encode the image in base64
def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image {image_path}: {e}")
        return None

# Function to send an image to OpenAI API and get a response
def send_image_to_api(encoded_image, image_name):
    prompt = f"This is an image called {image_name}. What should be its new filename?"
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI that specializes in recognizing images and suggesting suitable filenames for them. Provide only the name, do not include extension nor the word 'memoji', nothing else!"
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
                    }
                ]
            }
        ],
        "max_tokens": 100,
        "temperature": 0.2
    }
    
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
        return None

# Function to process all images in the directory
def process_images(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(directory, filename)
            print(f"Processing {image_path}")

            # Encode the image in base64
            base64_image = encode_image(image_path)
            if not base64_image:
                continue

            # Send the encoded image to the API and get the suggested filename
            suggested_name = send_image_to_api(base64_image, filename)
            if suggested_name:
                # Sanitize the suggested name (e.g., remove invalid characters for file systems)
                sanitized_name = "".join(c for c in suggested_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
                new_filename = f"{sanitized_name}{os.path.splitext(filename)[1]}"
                new_filepath = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(image_path, new_filepath)
                print(f"Renamed {image_path} to {new_filepath}")
            else:
                print(f"Failed to get a new name for {image_path}")

            # Add delay to avoid rate limits
            time.sleep(1)

if __name__ == "__main__":
    # Define the directory where the images are stored (current working directory)
    directory = os.getcwd()
    
    print(f"Starting image processing in directory: {directory}")
    process_images(directory)
    print("Processing completed.")
