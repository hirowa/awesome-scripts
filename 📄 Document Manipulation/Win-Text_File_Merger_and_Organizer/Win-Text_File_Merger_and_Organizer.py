import os
import re
import shutil

def natural_sort_key(s):
    # This key function will convert the text into a list of integers and strings
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def merge_txt_files_in_folder(folder_path, root_transcripts_folder, separator='---'):
    # Find all txt files in the current directory
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')], key=natural_sort_key)
    if not txt_files:
        # No txt files in this folder, so nothing to merge
        return None

    # Merge the contents of the txt files
    merged_contents = ""
    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            contents = file.read()
            merged_contents += f"\n{separator}\n\n{contents}\n"

    # Remove the first separator if it exists
    if merged_contents.startswith(f"\n{separator}\n"):
        merged_contents = merged_contents[len(f"\n{separator}\n"):]

    # Use the parent directory name for the output file name
    parent_folder_name = os.path.basename(os.path.dirname(folder_path))
    output_file_name = f"{parent_folder_name}.txt"

    # Create the 'Merged' folder if it does not exist
    merged_folder_path = os.path.join(folder_path, "Merged")
    os.makedirs(merged_folder_path, exist_ok=True)

    # The merged file path in the 'Merged' folder
    output_file_path = os.path.join(merged_folder_path, output_file_name)
    with open(output_file_path, 'w') as file_out:
        file_out.write(merged_contents)
    print(f"Merged .txt files in {folder_path} into {output_file_name}.")

    # Copy the merged file to the root transcripts folder
    root_transcripts_file_path = os.path.join(root_transcripts_folder, output_file_name)
    shutil.copy(output_file_path, root_transcripts_file_path)
    print(f"Copied {output_file_name} to {root_transcripts_folder}")

    return output_file_path

def merge_txt_files_in_directory(directory_path):
    directory_path = directory_path.strip('"')  # Ensure any surrounding quotes are removed
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return
    
    # Create the '0. Transcripts' folder in the root directory if it does not exist
    transcripts_folder = os.path.join(directory_path, "0. Transcripts")
    os.makedirs(transcripts_folder, exist_ok=True)
    print(f"Created or verified '0. Transcripts' folder in {directory_path}")

    for root, dirs, files in os.walk(directory_path):
        # Check if there are any txt files in the current root
        if any(file.endswith('.txt') for file in files):
            merged_file_path = merge_txt_files_in_folder(root, transcripts_folder)
            if merged_file_path:
                # Move the merged file into the "Merged" folder
                merged_folder_path = os.path.join(root, "Merged")
                os.makedirs(merged_folder_path, exist_ok=True)
                shutil.move(merged_file_path, os.path.join(merged_folder_path, os.path.basename(merged_file_path)))
                print(f"Moved merged file to {merged_folder_path}")

def main():
    while True:
        directory_path = input("Enter the root directory path where the .txt files are located: ")
        merge_txt_files_in_directory(directory_path)

        # Ask the user if they want to process more folders
        another = input("Do you want to process another folder? (yes/no): ").lower()
        if another != 'yes':
            break

# Run the main function
main()