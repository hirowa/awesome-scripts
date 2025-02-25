import os
import re

def process_srt_file(filepath):
    """
    Reads an .srt file and extracts only the subtitle text,
    skipping sequence numbers and timestamp lines.
    All lines are combined into one line (with spaces between).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Regex pattern to identify typical SRT timestamp lines.
    timestamp_pattern = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}')
    processed_lines = []

    for line in lines:
        line = line.strip()
        # Skip empty lines, numeric sequence lines, or timestamp lines.
        if not line or line.isdigit() or timestamp_pattern.search(line):
            continue
        processed_lines.append(line)

    # Combine all text into one single line (space-separated).
    return " ".join(processed_lines)

def main():
    # Prompt user for directory path and remove extra quotation marks if present.
    path = input("Enter the directory path: ").strip().strip('"')
    if not os.path.exists(path):
        print("Error: The provided path does not exist.")
        return

    # Walk through the folder and its subfolders.
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".srt"):
                srt_path = os.path.join(root, file)
                result_text = process_srt_file(srt_path)
                # Save the new .txt file in the same folder as the original .srt file.
                txt_filename = os.path.splitext(file)[0] + ".txt"
                txt_path = os.path.join(root, txt_filename)
                with open(txt_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(result_text)
                print(f"Converted '{srt_path}' to '{txt_path}'")

if __name__ == '__main__':
    main()
