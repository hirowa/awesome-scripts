from bs4 import BeautifulSoup
import requests
import re
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
import os

# ANSI escape sequences for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # Resets the color to default.

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def clean_title(title):
    contraband = [':', '/', '\\', '?', '"', '*', '|', '<', '>', '#']
    for c in contraband:
        title = title.replace(c, '')
    return title

def find_youtube_channel_id(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup_str = str(soup)
        search_string = "?channel_id="
        start_index = soup_str.find(search_string)
        if start_index != -1:
            start_index += len(search_string)
            end_index = soup_str.find('"', start_index)
            return soup_str[start_index:end_index]
        return None
    except Exception as e:
        return None

def get_channel_name(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find("meta", property="og:title")
        return title_tag["content"] if title_tag else "UnknownChannel"
    except Exception:
        return "UnknownChannel"

def get_video_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find("meta", property="og:title")
        return title_tag["content"] if title_tag else "Untitled"
    except Exception as e:
        print("------------------------------------------------------------------")
        print(f"{RED}Error fetching title for video ID {video_id}: {e}{RESET}")
        print("------------------------------------------------------------------")
        return "Untitled"

def merge_txt_files_in_folder(folder_path, separator='---'):
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')], key=natural_sort_key)
    if not txt_files:
        print("------------------------------------------------------------------")
        print(f"{RED}No .txt files found in the directory {folder_path}.{RESET}")
        print("------------------------------------------------------------------")
        return None

    merged_contents = ""
    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify encoding here
            contents = file.read()
            merged_contents += f"\n{separator}\n\n{contents}\n"

    if merged_contents.startswith(f"\n{separator}\n"):
        merged_contents = merged_contents[len(f"\n{separator}\n"):]

    output_file_name = f".{os.path.basename(folder_path)}_merged.txt"
    output_file_path = os.path.join(folder_path, output_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file_out:  # Specify encoding here as well
        file_out.write(merged_contents)
    print("------------------------------------------------------------------")
    print(f"{GREEN}Merged .txt files in {folder_path} into {output_file_name}.{RESET}")

    return output_file_path

def download_transcripts(channel_id, base_folder, content_types, channel_name, sleep_duration):
    if channel_id is None:
        print("------------------------------------------------------------------")
        print(f"{RED}Invalid YouTube channel ID.{RESET}")
        return

    base_path = os.path.join(base_folder, channel_name)
    os.makedirs(base_path, exist_ok=True)

    for content_type in content_types:
        videos = list(scrapetube.get_channel(channel_id, content_type=content_type, sleep=sleep_duration))

        if len(videos) == 0:
            print("------------------------------------------------------------------")
            print(f"{RED}No {content_type} found on the channel.{RESET}")
            continue

        print("------------------------------------------------------------------")
        print(f"{MAGENTA}Found {len(videos)} {content_type} on the channel. Starting download...{RESET}")
        print("------------------------------------------------------------------")

        subfolder_path = os.path.join(base_path, content_type.capitalize())
        os.makedirs(subfolder_path, exist_ok=True)

        for video in videos:
            try:
                video_id = video['videoId']
                title = get_video_title(video_id)
                sanitized_title = clean_title(title)  # Ensure title is sanitized

                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                text = [i['text'] for i in transcript]
                block = ' '.join(text)
                print(f"{GREEN}Downloading transcript for: {sanitized_title}{RESET}")
                file_content = f"Title: {sanitized_title}\nURL: https://www.youtube.com/watch?v={video_id}\n\n{block}"
                save_file(os.path.join(subfolder_path, f'{sanitized_title}.txt'), file_content)
            except Exception as e:
                print("------------------------------------------------------------------")
                print(f"{RED}Error with video {video_id}: {e}{RESET}")

        merge_txt_files_in_folder(subfolder_path)

    print("------------------------------------------------------------------")
    print(f"{MAGENTA}Transcript download complete.{RESET}")
    print("------------------------------------------------------------------")

def main():
    print(f"{BLUE}YouTube Transcript Downloader{RESET}")
    channel_url = input(f"{GREEN}Enter the YouTube channel URL: {RESET}")
    channel_id = find_youtube_channel_id(channel_url)
    channel_name = get_channel_name(channel_url)
    base_folder = input(f"{GREEN}Enter the base output folder path (without quotation marks): {RESET}").strip('""')

    print(f"{YELLOW}Select content type to download:{RESET}")
    print("1. Videos")
    print("2. Shorts")
    print("3. Streams")
    print("4. All")
    choice = input(f"{CYAN}Enter your choice (1, 2, 3, or 4): {RESET}")
    print("------------------------------------------------------------------")

    sleep_duration = int(input(f"{CYAN}Enter the sleep duration between requests (in seconds): {RESET}"))

    content_types_map = {
        "1": ["videos"],
        "2": ["shorts"],
        "3": ["streams"],
        "4": ["videos", "shorts", "streams"]
    }
    content_types = content_types_map.get(choice, ["videos", "shorts", "streams"])

    download_transcripts(channel_id, base_folder, content_types, channel_name, sleep_duration)

if __name__ == "__main__":
    while True:
        main()
        repeat = input(f"{YELLOW}Do you want to process another channel? (yes/no): {RESET}").lower()
        if repeat != "yes":
            break
