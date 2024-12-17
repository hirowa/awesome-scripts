import time
import openai  # Import the openai module

def main():
    api_key = read_api_key('api_key.txt')
    voice = get_voice_input()
    lines = read_lines_from_file('input.txt')  # Assuming the file is named 'input.txt'
    
    for i, line in enumerate(lines, 1):
        success = False
        while not success:
            try:
                response = convert_text_to_speech(api_key, voice, line.strip())
                file_name = f"{i}.mp3"
                save_to_mp3(response, file_name)
                success = True  # Mark as successful to break out of the loop
            except Exception as e:  # Catch a general exception
                if '429' in str(e):  # Check if it's a rate limit error by looking for '429' in the error message
                    print("Rate limit reached. Waiting before retrying...")
                    time.sleep(10)  # Wait for 10 seconds before retrying
                else:
                    raise  # Re-raise the exception if it's not a rate limit error

if __name__ == '__main__':
    main()