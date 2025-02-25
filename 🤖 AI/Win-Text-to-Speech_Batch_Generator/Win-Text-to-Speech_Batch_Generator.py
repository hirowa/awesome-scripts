import time
import os
from openai import OpenAI

def get_voice_input():
    return "alloy"  # Example voice model

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def convert_text_to_speech(api_key, voice, text):
    client = OpenAI(api_key=api_key)  # Initialize OpenAI client
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    return response

def save_to_mp3(response, filename):
    with open(filename, 'wb') as file:
        file.write(response.content)

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Missing OpenAI API key")

    voice = get_voice_input()
    lines = read_lines_from_file('input.txt')

    for i, line in enumerate(lines, 1):
        success = False
        while not success:
            try:
                response = convert_text_to_speech(api_key, voice, line.strip())
                file_name = f"{i}.mp3"
                save_to_mp3(response, file_name)
                success = True
            except Exception as e:
                if '429' in str(e):
                    print("Rate limit reached. Waiting before retrying...")
                    time.sleep(10)
                else:
                    raise

if __name__ == '__main__':
    main()
