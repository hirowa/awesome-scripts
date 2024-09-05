import os
import shutil

# Function to create a new folder and move .txt files into it
def organize_txt_files(base_dir, new_folder_name="Transcripts"):
    for root, dirs, files in os.walk(base_dir):
        # Filter out all txt files
        txt_files = [f for f in files if f.endswith('.txt')]
        if txt_files:
            # Create a new folder within the directory where txt files are found
            new_folder_path = os.path.join(root, new_folder_name)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            # Move all txt files to the new folder
            for txt_file in txt_files:
                src_file_path = os.path.join(root, txt_file)
                dst_file_path = os.path.join(new_folder_path, txt_file)
                shutil.move(src_file_path, dst_file_path)
            print(f"Moved {len(txt_files)} .txt files to {new_folder_path}")

def get_user_input(prompt):
    # Allow the user to enter input with quotes
    user_input = input(prompt)
    return user_input.strip("\"' ")

def get_directory_input(prompt):
    while True:
        directory = get_user_input(prompt)
        if os.path.isdir(directory):
            return directory
        else:
            print("The provided directory does not exist. Please enter a valid directory.")

def main():
    while True:
        # Ask the user for the base directory and new folder name
        base_directory = get_directory_input("Enter the base directory to organize .txt files: ")
        new_folder_name_input = get_user_input("Enter a name for the new folder (leave blank to use default 'Transcripts'): ")

        # Use the default folder name "Transcripts" if the user left the input blank
        new_folder_name = new_folder_name_input if new_folder_name_input else "Transcripts"

        organize_txt_files(base_directory, new_folder_name)

        # Ask if the user wants to process more folders
        more = get_user_input("Do you want to process another folder? (yes/no): ").lower()
        if more != "yes":
            break

# Run the script
if __name__ == "__main__":
    main()