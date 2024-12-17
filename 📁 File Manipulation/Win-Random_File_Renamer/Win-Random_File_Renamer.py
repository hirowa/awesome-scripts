import os
import random
import sys

def rename_files_in_directory(directory_path):
    # Remove quotation marks if present
    directory_path = directory_path.strip('\'"')

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    # Iterate over the files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Generate a unique random number for the new filename
        new_filename = str(random.randint(100000, 999999)) + os.path.splitext(filename)[1]
        new_file_path = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder: ")
    rename_files_in_directory(folder_path)