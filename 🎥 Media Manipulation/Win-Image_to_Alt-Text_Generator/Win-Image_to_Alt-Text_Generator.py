import os
import base64
import openai
import requests
import json

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_alt_text(api_key, base64_image):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

    payload = {
      "model": "gpt-4-vision-preview",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What’s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

def process_folder(folder_path, api_key):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"Processing {filename}...")
            image_path = os.path.join(folder_path, filename)
            base64_image = encode_image(image_path)
            alt_text = generate_alt_text(api_key, base64_image)
            text_filename = os.path.splitext(filename)[0] + '.txt'
            with open(os.path.join(folder_path, text_filename), 'w') as text_file:
                text_file.write(alt_text)
            print(f"Completed {filename}.")

def get_api_key():
    api_key_file = 'api_key.txt'
    if os.path.exists(api_key_file):
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
            if api_key:
                return api_key
    return input("Enter your OpenAI API key: ")

# Ask user for the folder path
folder_path = input("Enter the path to the folder containing images: ")

# Get the API key
api_key = get_api_key()

# Process the folder
print("Starting the processing of images...")
process_folder(folder_path, api_key)
print("All images processed.")